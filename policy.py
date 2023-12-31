import numpy as np

class MazeSolver:
    def __init__(self, size, barrier_prob):
        self.size = size
        self.barrier_prob = barrier_prob
        self.maze = np.zeros((size, size))  # 0 represents an empty cell
        self.generate_maze()

        # Start state at top-left corner
        self.start_state = (0, 0)
        # Terminal state at bottom-right corner
        self.terminal_state = (size - 1, size - 1)

        # Initialize policy arbitrarily
        self.policy = np.random.randint(0, 4, size=(size, size))  # 0: Up, 1: Right, 2: Down, 3: Left

    def generate_maze(self):
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if np.random.rand() < self.barrier_prob:
                    self.maze[i, j] = 1  # 1 represents a barrier

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.maze[x, y] == 0

    def policy_iteration(self, discount_factor=0.9, max_iterations=1000):
        # Initialize value function arbitrarily
        value_function = np.zeros((self.size, self.size))

        for iteration in range(max_iterations):
            print(f"\nPolicy Iteration - Iteration {iteration + 1}:\n")

            # Policy Evaluation
            value_function = self.evaluate_policy(value_function, discount_factor)

            # Policy Improvement
            new_policy = self.improve_policy(value_function, discount_factor)

            # Check if the policy has converged
            if np.array_equal(new_policy, self.policy):
                print("Policy Converged!")
                break

            self.policy = new_policy

            self.print_maze(self.policy)

    def evaluate_policy(self, value_function, discount_factor):
        # Perform policy evaluation using iterative policy evaluation
        for _ in range(1000):  # You can adjust the number of iterations
            for i in range(self.size):
                for j in range(self.size):
                    # if barrier, skip
                    if self.maze[i, j] == 1:
                        continue

                    action = self.policy[i, j]
                    next_x, next_y = self.get_next_position(i, j, action)

                    if self.is_valid_move(next_x, next_y):
                        reward = 0
                        if (next_x, next_y) == self.terminal_state:
                            reward = 1

                        # Update value function based on policy
                        value_function[i, j] = reward + discount_factor * value_function[next_x, next_y]

        return value_function

    def improve_policy(self, value_function, discount_factor):
        # Perform policy improvement
        new_policy = np.zeros((self.size, self.size))

        for i in range(self.size):
            for j in range(self.size):
                if self.maze[i, j] == 1:
                    continue

                # Try all possible actions and choose the one with the highest expected value
                max_action = None
                max_value = float('-inf')

                for action in range(4):
                    next_x, next_y = self.get_next_position(i, j, action)

                    if self.is_valid_move(next_x, next_y):
                        reward = 0
                        if (next_x, next_y) == self.terminal_state:
                            reward = 1

                        expected_value = reward + discount_factor * value_function[next_x, next_y]

                        if expected_value > max_value:
                            max_value = expected_value
                            max_action = action

                if max_action is not None:
                    new_policy[i, j] = max_action

        return new_policy

    def get_next_position(self, x, y, action):
        if action == 0:  # Up
            return x - 1, y
        elif action == 1:  # Right
            return x, y + 1
        elif action == 2:  # Down
            return x + 1, y
        elif action == 3:  # Left
            return x, y - 1

    def print_maze(self, policy):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.start_state:
                    print("S    |", end="")
                elif (i, j) == self.terminal_state:
                    print("E    |", end="")
                elif self.maze[i, j] == 1:
                    print("X    |", end="")
                else:
                    action_str = "↑" if policy[i, j] == 0 else "→" if policy[i, j] == 1 else "↓" if policy[i, j] == 2 else "←"
                    print(f"{action_str}    |", end="")
            print()
if __name__ == "__main__":
    size = 7
    barrier_prob = 0.3
    maze_solver = MazeSolver(size, barrier_prob)

    print("Maze:")
    maze_solver.print_maze(maze_solver.maze)

    print("\nPolicy Iteration:")
    maze_solver.policy_iteration()