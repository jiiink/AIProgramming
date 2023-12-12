from HillClimber import HillClimber
import numpy as np

class FirstChoiceHillClimber(HillClimber):
    def fit(self):
        self.current_solution = self.initial_solution_generator()
        for _ in range(self.max_iter):
            new_solution = self.generate_neighbor(solution=self.current_solution, step_size=self.step_size)
            new_score = self.objective_function(new_solution)
            
            if new_score < self.best_score:
                self.best_score = new_score
                self.best_solution = new_solution
                self.current_solution = new_solution
                
        return self.best_solution
    pass

def generate_neighbor(solution, step_size):
    new_solution = solution + np.random.uniform(-step_size, step_size, len(solution))
    return new_solution

def objective_function(x):
    return (x[0] - 2) ** 2 + 5 * (x[1] - 5) ** 2 + 8 * (x[2] + 8) ** 2 + 3 * (x[3] + 1) ** 2 + 6 * (x[4] - 7) ** 2

def initial_solution_generator():
    return [np.random.uniform(-30, 30) for _ in range(5)]


# Test the FirstChoiceHillClimber class
first_choice_hill_climber = FirstChoiceHillClimber(
    generate_neighbor=generate_neighbor,
    objective_function=objective_function,
    initial_solution_generator=initial_solution_generator,
    step_size=0.1,
    max_iter=10000
)
first_choice_hill_climber.fit()
print(f"First Choice Hill Climber Best Solution: {first_choice_hill_climber.predict()}")
print(f"First Choice Hill Climber Best Score: {first_choice_hill_climber.score():.5f}")