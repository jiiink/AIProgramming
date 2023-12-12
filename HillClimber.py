import numpy as np

class HillClimber:
    def __init__(self, generate_neighbor, objective_function, initial_solution_generator, step_size=0.01, max_iter=100000):
        self.initial_solution_generator = initial_solution_generator
        self.generate_neighbor = generate_neighbor
        self.objective_function = objective_function
        self.current_solution = None
        self.step_size = step_size
        self.max_iter = max_iter
        self.best_solution = None
        self.best_score = float('inf')



    def fit(self):
        self.current_solution = self.initial_solution_generator()
        for _ in range(self.max_iter):
            new_solution = self.generate_neighbor(self.current_solution, self.step_size)
            new_score = self.objective_function(*new_solution)
            if new_score < self.best_score:
                self.best_solution = new_solution
                self.best_score = new_score
                self.current_solution = new_solution

        return self.best_solution

    def predict(self):
        return self.best_solution
    
    def score(self):
        return self.best_score
    
    
def convex_function(*x):
    return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) ** 2

def generate_neighbor(current_solution, step_size):
    return current_solution + np.random.uniform(-step_size, step_size, len(current_solution))

def initial_solution_generator():
    return [np.random.uniform(-30, 30) for _ in range(5)]
    
step_size = 0.1
# print(np.random.uniform(-step_size, step_size, 5))
# print([np.random.uniform(-step_size, step_size) for _ in range(5)])
hill = HillClimber(generate_neighbor, convex_function, initial_solution_generator)
hill.fit()
# print(f"Hill Climber Best Solution: {hill.predict()}")
# print(f"Hill Climber Best Score: {hill.score():.5f}")