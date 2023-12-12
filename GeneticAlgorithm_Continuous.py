import numpy as np

class GeneticAlgorithm:
  def __init__(
    self, fitness_function, initial_population_generator,
        selection_function, crossover_function, mutation_function,
        population_size=100, num_generations=1000,
        crossover_probability=0.99,
        mutation_probability=None
    ):
    self.fitness_function = fitness_function
    self.initial_population_generator = initial_population_generator

    self.selection = selection_function
    self.crossover = crossover_function
    self.mutation = mutation_function

    self.population_size = population_size
    self.num_generations = num_generations

    self.crossover_probability = crossover_probability
    self.mutation_probability = mutation_probability if mutation_probability is not None else 1 / self.population_size

    self.population = None
    self.best_solution = None
    self.best_score = float('inf')

  def fit(self):
    self.population = self.initial_population_generator(population_size=self.population_size)
    for generation in range(self.num_generations):
      fitness_scores = [self.fitness_function(solution=individual) for individual in self.population]
      best_idx = np.argmin(fitness_scores)

      if fitness_scores[best_idx] < self.best_score:
        self.best_score = fitness_scores[best_idx]
        self.best_solution = self.population[best_idx]
        if generation == self.num_generations - 1: break

      new_population = []
      for _ in range(self.population_size):
        # Selection
        parents_indices = self.selection(fitness_scores, 2)
        parent1, parent2 = self.population[parents_indices[0]], self.population[parents_indices[1]]
        # Crossover
        if np.random.rand() < self.crossover_probability:
          child = self.crossover(parent1, parent2)
        else:
          child = parent1.copy()
        # Mutation
        mutated_child = self.mutation(child, self.mutation_probability)
        new_population.append(mutated_child)
      self.population = new_population

    return self.best_solution

  def predict(self):
      return self.best_solution

  def score(self):
      return self.best_score
  
  
# ------------------------------------------

import math

def griewank_function(x):
  sum_term = sum(xi ** 2 for xi in x) / 4000
  prod_term = math.cos(x[0])
  for i, xi in enumerate(x[1:], start=2):
      prod_term *= math.cos(xi / math.sqrt(i))
  return 1 + sum_term - prod_term

def convex_function(x):
   return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) **2

def ackley_function(x):
   term1 = -20 * math.exp(-0.2 * math.sqrt(sum(xi ** 2 for xi in x) / len(x)))
   term2 = -math.exp(sum(math.cos(2 * math.pi * xi) for xi in x) / len(x))
   return 20 + math.e + term1 + term2

from functools import partial

def binary_to_real(binary, min_val=-30, max_val=30):
  decimal = int("".join(str(int(bit)) for bit in binary), 2)
  max_decimal = 2**len(binary) - 1
  real_value = min_val + (max_val - min_val) * decimal / max_decimal
  return real_value

def fitness_func(f, solution, n_splits=5):
  # Splitting the binary_solution into 5 segments of 12 bits each
  split_solution = np.split(solution, n_splits)
  real_values = [binary_to_real(segment, -30, 30) for segment in split_solution]
  return f(real_values)

def initial_population_generator(population_size, gene_length=60):
  return np.random.randint(2, size=(population_size, gene_length))

fitness_func = partial(fitness_func, f=griewank_function)


def select(fitness_scores, num_parents, tournament_size=3):
  parents_indices = []
  parents_indices.append(np.argmin(fitness_scores))
  parents_indices.append(np.random.randint(0, len(fitness_scores)))
  return parents_indices

def crossover(parent1, parent2):
  rand_index = np.random.randint(0, len(parent1))
  
  child = np.concatenate((parent1[:rand_index], parent2[rand_index:]))
  return child

def mutate(individual, mutation_rate):
  if (mutation_rate < np.random.uniform(0, 1)):
    rand_index = np.random.randint(0, len(individual))
    individual[rand_index] = np.random.randint(2)

  return individual

ga = GeneticAlgorithm(
    fitness_function=fitness_func,
    initial_population_generator=initial_population_generator,
    selection_function=select,
    crossover_function=crossover,
    mutation_function=mutate,
    population_size=30,
    num_generations=1000,
    crossover_probability=0.99,
    mutation_probability=None
)

best_solution = ga.fit()
print("best_solution: ", best_solution)
print("best_score: ", fitness_func(solution=best_solution))