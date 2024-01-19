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
                if i != 0 or j != 0:
                    if np.random.rand() < self.barrier_prob:
                        self.maze[i, j] = -1  # 1 represents a barrier
        global my_maze
        my_maze = self.maze
        print("//------initial maze with barier------\\\\")
        print(self.maze)

    def is_solvable(self):
        visited = set()

        def dfs(x, y):
            if not (0 <= x < self.size and 0 <= y < self.size) or my_maze[x, y] == -1 or (x, y) in visited:
                return False

            visited.add((x, y))

            if (x, y) == self.terminal_state:
                return True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                if dfs(x + dx, y + dy):
                    return True

            return False

        return dfs(*self.start_state)                   
                    

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.maze[x, y] == 0

    def policy_iteration(self, discount_factor=0.9, max_iterations=1000):
        # Initialize value function arbitrarily
        value_function = np.zeros((self.size, self.size))

        for iteration in range(max_iterations):

            # Policy Evaluation
            value_function = self.evaluate_policy(value_function, discount_factor)

            # Policy Improvement
            new_policy = self.improve_policy(value_function, discount_factor)

            # Check if the policy has converged
            if np.array_equal(new_policy, self.policy):
                print("Policy Converged!")
                break
            # printing Vk for the Random Policy and the greedy policy w.t.r to Vk
            print(f"\nPolicy Iteration - Iteration {iteration + 1}:\n")
            self.print_maze_value(value_function)
            self.policy = new_policy
            print(f"\ngreedy policy w.t.r to Iteration {iteration + 1}:\n")
            self.print_maze(self.policy)


    def evaluate_policy(self, value_function, discount_factor):
        # Perform policy evaluation using iterative policy evaluation
        for _ in range(1000):  # You can adjust the number of iterations
            for i in range(self.size):
                for j in range(self.size):
                    # if barrier, skip
                    if self.maze[i, j] == -1:
                        continue

                    action = self.policy[i, j]
                    next_x, next_y = self.get_next_position(i, j, action)

                    if self.is_valid_move(next_x, next_y):
                        reward = 0
                        if (i, j) == self.terminal_state:
                            reward = 10

                        # Update value function based on policy
                        value_function[i, j] = reward + discount_factor * value_function[next_x, next_y]

        return value_function

    def improve_policy(self, value_function, discount_factor):
        # Perform policy improvement
        new_policy = np.zeros((self.size, self.size))

        for i in range(self.size):
            for j in range(self.size):
                if self.maze[i, j] == -1:
                    # represent the barier by -1 in the policy array of actions
                    new_policy[i,j] = -1
                    continue

                # Try all possible actions and choose the one with the highest expected value
                max_action = None
                max_value = float('-inf')

                for action in range(4):
                    next_x, next_y = self.get_next_position(i, j, action)

                    if self.is_valid_move(next_x, next_y):
                        reward = 0
                        if (i, j) == self.terminal_state:
                            reward =10

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
                # if (i, j) == self.start_state:
                #     print("S    |", end="")
                if (i, j) == self.terminal_state:
                    print("E    |", end="")
                elif self.maze[i, j] == -1:
                    print("B    |", end="")
                else:
                    action_str = "↑" if policy[i, j] == 0 else "→" if policy[i, j] == 1 else "↓" if policy[i, j] == 2 else "←"
                    print(f"{action_str}    |", end="")
            print()
    # def print_maze_value(self, values):
    #     for i in range(self.size):
    #         for j in range(self.size):
    #             if (i, j) == self.start_state:
    #                 print("S    |", end="")

    #             elif self.maze[i, j] == -1:
    #                 print("B    |", end="")
    #             else:
    #                 print(f"{values[i, j]:.2f} |", end="")
    #         print()
    def print_maze_value(self, values):
        for i in range(self.size):
            for j in range(self.size):
                # to make it clean for the print we will create cell variable to be a box
                # so the spacing will not depend on a uniqe value all will be the same
                # S for start state , B for terminal state
                cell = "S" if (i, j) == self.start_state else "B" if self.maze[i, j] == 1 else f"{values[i, j]:.2f}"
                print(f"{cell:6} |", end="")
            print()

def find_optimal_path_with_values(value_array):
    rows, cols = value_array.shape
    optimal_path = []

    current_position = (0, 0)
    terminal_state = (rows - 1, cols - 1)

    while current_position != terminal_state:
        i, j = current_position
        if value_array[i,j] == 0:
            direction = 'U'
            next_position = (i-1,j)
            optimal_path.append(direction)
        elif value_array[i,j] == 1:
            direction = 'R'
            next_position = (i,j+1)
            optimal_path.append(direction)
        elif value_array[i,j] == 2:
            next_position = (i+1,j)
            direction = 'D'
            optimal_path.append(direction)
        elif value_array[i,j] == -1:
                return -1
        else:
            direction = 'L'
            next_position = (i,j-1)
            optimal_path.append(direction)



        # Move to the next position
        current_position = next_position

    return optimal_path

if __name__ == "__main__":
    size = int(input("Enter the size of the maze: "))
    barrier_prob = float(input("Enter the probability of barriers (0.0 to 1.0): "))
    maze_solver = MazeSolver(size, barrier_prob)


    # pas = find_optimal_path_with_values(maze_solver.policy)
    solvable = maze_solver.is_solvable()
    if(solvable):
        print("Maze:")
        maze_solver.print_maze(maze_solver.maze)

        print("\nPolicy Iteration:")
        maze_solver.policy_iteration()
        pas = find_optimal_path_with_values(maze_solver.policy)
        print("path to goal staring from state(0,0):") 
        print(pas)
        print(f"cost of path: {len(pas)}") 
    else:
        print("Maze is not solvable")


