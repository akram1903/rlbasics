
# Agent Maze Solver using Value Iteration and Policy Iteration GUI

This Python script implements a maze-solving agent with a graphical user interface (GUI) using Tkinter. The agent employs both value iteration and policy iteration algorithms to navigate through the maze. The GUI allows users to visualize the maze, generate a new maze with obstacles, and solve the maze using either value iteration or policy iteration.



## Instructions
___Maze Generation:___

_Follow these steps in order to use the GUI successfully:_

***1-Enter Maze Size (N):***  

Input the desired maze size (N) in the designated entry field.  
***2-Select Algorithm:***

Choose either "Value Iteration" or "Policy Iteration" using the radio buttons.  
***3-Generate Maze:***

    -Click the "Generate Maze" button to create a new maze.
    -The console will prompt you to enter the probability of barriers (obstacles) in the maze.
    -Input the barrier probability in the console and press Enter.
***4-Maze Generation Confirmation:***

After entering the barrier probability, the maze will be generated successfully.  
You will see the maze displayed _randomly_ in the GUI.

___Maze Solving:___

After generating the maze, click the "Solve" button to find the optimal path from the start (S) to the goal (E) using the selected algorithm (value iteration or policy iteration).  
  
    -Each iteration will be displayed in the Console.  
    -The _solved path ,Cost and running time_ will be displayed in Console.     
    -The agent's movement will be animated on both the GUI and Console.  
  
## Maze Representation

    -S (Start): Represented by the letter 'S', the starting position of the agent.  
    -E (End/Goal): Represented by the letter 'E', the goal position that the agent must reach.  
    -Obstacles: Represented by a monster icon, obstacles are barriers that the agent must navigate around (1).  
    -Agent: Represented by a walking sprite, the agent's current position is indicated in the maze (2).  


## Image Assets

    -Walking sprites for the agent facing different directions (up, down, left, right) are used for visual representation.  
    -A monster icon is used to represent obstacles in the maze.
## Dependencies
*The script uses Tkinter for GUI.*
To install Tkinter in python follow tho following steps:  
To Check python:  

    python --version
To check pip:  

    pip -V
Install Tkinter:

    pip install tk  
*Ensure that the required image assets are available in the specified file paths.*
## Acknowledgements
-This script is based on the concepts of value iteration and policy iteration in reinforcement learning.  
___Feel free to explore, generate mazes, and observe the agent's navigation in the provided GUI!___


## Authors
- [@SaifSeddik](https://github.com/SaifSeddik)
- [@RanaZay](https://github.com/RanaZay)
- [@akram1903](https://github.com/akram1903)



## Github Repo - Link

- [Github Repository](https://github.com/akram1903/rlbasics)

