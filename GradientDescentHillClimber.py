from HillClimber import HillClimber
import numpy as np

class GradientDescentHillClimber(HillClimber):
    def __init__(self, generate_neighbor, objective_function, initial_solution_generator, step_size=0.1, num_neighbors=1, learning_rate=0.01, max_iter=1000, mode='min', num_restarts=10):
      super().__init__(generate_neighbor=generate_neighbor, 
                       objective_function=objective_function, 
                       initial_solution_generator=initial_solution_generator, 
                       step_size=step_size, 
                       max_iter=max_iter, 
                       )
      self.learning_rate = learning_rate
      self.num_neighbors = num_neighbors
      self.num_restarts = num_restarts
      
    def fit(self):
      self.current_solution = self.initial_solution_generator()
      
      for _ in range(self.max_iter):
        new_solution = self.generate_neighbor(self.current_solution, self.objective_function, self.learning_rate)
        new_score = self.objective_function(new_solution)
        
        if new_score < self.best_score:
          self.best_score = new_score
          self.best_solution = new_solution
          self.current_solution = new_solution
          
      return self.best_solution
      
      
def generate_neighbor(solution, f, learning_rate):
  h = 1e-5
  new_solution = []
  np_solution = solution
  fx = f(np_solution)
  
  for i in range(len(solution)):
    np_solution_h = np_solution.copy()
    np_solution_h[i] += h
    fx_h = f(np_solution_h)
    
    gradient = (fx_h - fx) / h
    new_solution.append(np_solution[i] - learning_rate*gradient)
    
  return new_solution  


def objective_function(x):
    return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) ** 2

def initial_solution_generator(n=5):
    return [np.random.uniform(-30, 30) for _ in range(n)]


hill_climber = GradientDescentHillClimber(
    generate_neighbor=generate_neighbor,
    objective_function=objective_function,
    initial_solution_generator=initial_solution_generator,
)

hill_climber.fit()

print(f"Gradient Descent Hill Climber Best Solution: {hill_climber.predict()}")
print(f"Gradient Descent Hill Climber Best Score: {hill_climber.score():.5f}")