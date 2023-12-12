from HillClimber import HillClimber
import numpy as np

class SimulatedAnnealingHillClimber(HillClimber):
  def __init__(self, generate_neighbor, objective_function, initial_solution_generator, step_size=0.1, num_neighbors=1, max_iter=10000, num_restarts=10, temperature=1.0, alpha=1.0):
    super().__init__(generate_neighbor=generate_neighbor, 
                     objective_function=objective_function, 
                     initial_solution_generator=initial_solution_generator, 
                     step_size=step_size, 
                     max_iter=max_iter, 
                     )
    self.temperature = temperature
    self.alpha = alpha
    self.num_neighbors = num_neighbors
    self.num_restarts = num_restarts

  def _acceptance_probability(self, cur_cost, new_cost):
    return np.exp(-(new_cost - cur_cost) / (self.temperature + 1e-2))

  def _cooling_schedule(self, k):
    self.temperature *= (1.0 - ((k + 1.0) / self.max_iter))

  def fit(self):
    self.current_solution = self.initial_solution_generator()
    
    for k in range(self.max_iter):
      self._cooling_schedule(k)
      neighbors = self.generate_neighbor(solution=self.current_solution, step_size=self.step_size, num_neighbors=self.num_neighbors)
      neighbors_scores = [self.objective_function(neighbor) for neighbor in neighbors]
      best_neighbor_index = np.argmin(neighbors_scores)
      best_neighbor = neighbors[best_neighbor_index]

      if neighbors_scores[best_neighbor_index] < self.best_score:
        self.best_solution = best_neighbor
        self.best_score = neighbors_scores[best_neighbor_index]
        self.current_solution = best_neighbor
      elif self._acceptance_probability(self.best_score, neighbors_scores[best_neighbor_index]) >= np.random.uniform(0, 1):
        neighbors = self.generate_neighbor(solution=self.current_solution, step_size=self.step_size, num_neighbors=self.num_neighbors)
        neighbors_scores = [self.objective_function(neighbor) for neighbor in neighbors]
        best_neighbor_index = np.argmin(neighbors_scores)
        best_neighbor = neighbors[best_neighbor_index]

    return self.best_solution

from functools import partial

def objective_function(x):
    return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) ** 2


def continuous_generate_neighbor(solution, step_size, num_neighbors):
    neighbors = []
    for _ in range(num_neighbors):
        neighbors.append(solution + np.random.uniform(-step_size, step_size, len(solution)))
    return neighbors


def initial_solution_generator(n=5):
    return [np.random.uniform(-30, 30) for _ in range(n)]


hill_climber = SimulatedAnnealingHillClimber(
    generate_neighbor=continuous_generate_neighbor,
    objective_function=objective_function,
    initial_solution_generator=initial_solution_generator,
)

hill_climber.fit()

print(f"Simulated Annealing Hill Climber Best Solution: {hill_climber.predict()}")
print(f"Simulated Annealing Hill Climber Best Score: {hill_climber.score():.5f}")