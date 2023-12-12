from HillClimber import HillClimber
import numpy as np

class SteepestAscentHillClimber(HillClimber):
    def __init__(self, generate_neighbor, objective_function, initial_solution_generator, max_iter, num_neighbors, step_size):
        super().__init__(generate_neighbor=generate_neighbor,
                         objective_function=objective_function,
                         initial_solution_generator=initial_solution_generator,
                         max_iter=max_iter,
                         step_size=step_size
                         )
        self.num_neighbors = num_neighbors
    def fit(self):
        self.current_solution = self.initial_solution_generator()

        for _ in range(self.max_iter):
            new_solutions = self.generate_neighbor(self.current_solution, self.step_size, self.num_neighbors)
            new_scores = [self.objective_function(new_solution) for new_solution in new_solutions]
            best_index = np.argmin(new_scores)
            new_score = new_scores[best_index]
            new_solution = new_solutions[best_index]
            
            if new_score < self.best_score:
                self.best_score = new_score
                self.best_solution = new_solution
                self.current_solution = new_solution
        
        return self.best_solution
  
  
    
def generate_neighbors(solution, step_size, num_neighbors):
    new_solutions = []
    
    for _ in range(num_neighbors):
        new_solution = solution + np.random.uniform(-step_size, step_size, len(solution))
        new_solutions.append(new_solution)
    return new_solutions

def initial_solution_generator():
    return [np.random.uniform(-30, 30) for _ in range(5)]

def objective_function(x):
    return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) ** 2

initial_solution = initial_solution_generator()

hill_climber = SteepestAscentHillClimber(
    generate_neighbor=generate_neighbors,
    objective_function=objective_function,
    initial_solution_generator=initial_solution_generator,
    max_iter=10000,
    num_neighbors=10,
    step_size=0.1,
  )

hill_climber.fit()

print(f"Steepest Hill Climber Best Solution: {hill_climber.predict()}")
print(f"Steepest Hill Climber Best Score: {hill_climber.score():.5f}")