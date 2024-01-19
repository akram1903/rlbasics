
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

    def generate_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.rand() < self.barrier_prob:
                    self.maze[i, j] = 1  # 1 represents a barrier
        self.maze[self.size-1, self.size-1] = 0  #to make sure that the termnal state is not barrier
        global my_maze
        my_maze = self.maze
        print("//------initial maze with barier------\\\\")
        self.print_initial_maze()

    def is_solvable(self):
        visited = set()

        def dfs(x, y):
            if not (0 <= x < self.size and 0 <= y < self.size) or my_maze[x, y] == 1 or (x, y) in visited:
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

    def value_iteration(self, discount_factor=0.9, theta=0.3, max_iterations=1000):
        # The value function is initialized to zeros for all states.
        value_function = np.zeros((self.size, self.size))
        for iteration in range(max_iterations):
            print(f"\nValue Iteration - Iteration {iteration + 1}:\n")

            delta = 0
            for i in range(self.size):
                for j in range(self.size):
                    # if barier skip
                    if self.maze[i, j] == 1:
                        continue
                    v = value_function[i, j]
                    # Value Iteration Updates based on 1 step lookahed
                    value_function[i, j] = self.calculate_max_value(i, j, value_function, discount_factor)
                    delta = max(delta, abs(v - value_function[i, j]))
            
            self.print_maze(value_function)

            if delta < theta:
                print('\n=========================================\n')
                return value_function

    def calculate_max_value(self, x, y, value_function, discount_factor):
        max_value = float('-inf')
        # get the max value from the 4 actions
        for action in range(4):
            next_x, next_y = self.get_next_position(x, y, action)
            if self.is_valid_move(next_x, next_y):
                # The formula for updating the value function is consistent
                # with the one-step lookahead approach. It considers the reward 
                # for the current state-action pair plus the discounted expected value of the next state.
                if x == self.size-1 and y == self.size-1:
                    reward = 1
                else:
                    reward = 0

                max_value = max(max_value,reward + discount_factor * value_function[next_x, next_y])

        return max_value

        
    def get_next_position(self, x, y, action):
        if action == 0:  # Up
            return x - 1, y
        elif action == 1:  # Right
            return x, y + 1
        elif action == 2:  # Down
            return x + 1, y
        elif action == 3:  # Left
            return x, y - 1

    def print_maze(self, values):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.start_state:
                    print("S    |", end="")
                elif self.maze[i, j] == 1:
                    print("B    |", end="")
                else:
                    print(f"{values[i, j]:.2f} |", end="")
            print()

    def print_initial_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == (0,0):
                    print("S    |", end="")
                elif my_maze[i, j] == 1:
                    print("B    |", end="")
                else:
                    print(f"{my_maze[i, j]:.2f} |", end="")
            print()

    def getCommands(self):
        # calling the value function to solve the maze 
        values = self.value_iteration()
        commands = []
        i,j=0,0
        nexti,nextj = 0,0
        while i!=self.size-1 or j!=self.size-1:
            max = float('-inf')
            maxDir = None
            nexti=i
            nextj=j
            if i-1>0 and max<values[i-1][j]:
                max = values[i-1][j]
                maxDir='u'
                nexti=i-1
            if i+1<self.size and max<values[i+1][j]:
                max = values[i+1][j]
                maxDir='d'
                nexti=i+1
            if j-1>0 and max<values[i][j-1]:
                max = values[i][j-1]
                maxDir='l'
                nextj=j-1
                nexti=i
            if j+1<self.size and max<values[i][j+1]:
                max = values[i][j+1] 
                maxDir='r'
                nextj=j+1
                nexti=i

            if maxDir is not None:
                commands.append(maxDir)
                i=nexti
                j=nextj

            
        return commands
 
    
if __name__ == "__main__":
    size = 7
    barrier_prob = 0.3
    maze_solver = MazeSolver(size, barrier_prob)
    solvable = maze_solver.is_solvable()
    if(solvable):
        optimal_path = maze_solver.getCommands()
        print(optimal_path)
        print("path to goal staring from state(0,0):") 
        print(f"cost of path: {len(optimal_path)}") 
    else:

        print("Maze is not solvable")
