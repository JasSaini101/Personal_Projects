# 💻 Personal Projects!

A small collection of other, smaller projects I have worked on over the years outside of school to learn and have fun!

## 🐴 Knights Tour

<div style="display: flex; flex-direction: row;">
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/476ee3a4-d0ca-4dc4-a0f0-bdf604a9a4f3" alt="Image 1" width="25%">
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/6687dd50-4346-4700-902d-45159752daf3" alt="Image 2" width="65%">
</div>

### 📝 Preface
A chess knight is unique in the way it moves as it jumps multiple squares (2 in one direction and 1 in another perpendicular direction) to form an "L-Shaped Move." A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once. 

### 🔍 Algorithms
There are multiple approaches to solve the knight's tour, the most efficient being Warnsdorff's Algorithm, in which the knight is instructed to go to the square with the least amount of qualifying neighbors. The least efficient approach is a simple brute force method.

### 💻 My Code
I built both programs to compare the efficiency between these two approaches to see how much of a difference the algorithm really makes.

Just pick your algorithm, input the board size, and the starting square for the knight. Just beware, not all boards have solutions; all arguments for the functions affect whether or not the board is solvable.



## 🧩 Maze Solvers

Maze solvers are a common coding project because of the valuable insights they offer. Creating code that can find the path for any solvable maze is both fun and a bit challenging for beginners. I created two maze solvers: a simpler one in Python when I was learning about data structures, and a more complex one in Java when I was understanding classes and learning the language.

### 📜 Python Version

A Python implementation of the maze solver algorithm, inspired by a project from my course 181. This script uses a queue to explore all possible paths in the maze until it finds the exit.

<p align="center">
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/fca0a960-1b1b-424a-b117-4e36ea79bced" width="300" />
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/704d16de-926c-4b4c-9545-f74d7e231656" width="250" />
</p>

This project creates a maze and then finds a path from the start to the exit using breadth-first search (BFS). The maze is represented as a 2D list, where `#` represents walls, `O` represents the starting point, and `X` represents the exit.

#### 🔍 How It Works

The maze solver uses a queue to store all possible paths and explores them in a breadth-first manner. For each position, it checks the validity of moves (left, right, up, down) and prints the path when it finds the exit.

#### 🎯 Features
- **Create Maze**: Generates a maze using a 2D list.
- **Print Maze**: Displays the maze with the path taken.
- **Validate Moves**: Checks if a move is within the maze boundaries and not hitting a wall.
- **Find End**: Determines if the current path reaches the exit.
- **Breadth-First Search**: Uses BFS to find the shortest path from start to exit.

This script is relatively simple and has its limitations, but it introduces beginners to essential concepts such as data structures and algorithms. A great step I took outside of school to improve my computer science skills and knowledge!
 
### 📜 Java Verison

A Java implementation of a maze-solving algorithm that began as a project for my CISC181 'Intro to Programming II' course. This project contains multiple classes to handle different components of the maze solution, such as the path, the maze, the squares in the maze, and more. Utilizing a breadth-first search approach, it explores all possible paths until either an exit is found or the runtime exceeds a predetermined limit.

<p align="center">
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/79180453-3f8b-44c2-a8fb-92511a89e351" width="300" />
  <img src="https://github.com/JasSaini101/Personal_Projects/assets/83828348/33a9e4e5-12d2-41ee-8906-91f1e3a29aa8" width="500" />
</p>

This project creates a maze and finds a path from the start to the exit using a path evaluation algorithm. The maze is represented as a 2D list where 'B' represents walls, 'S' represents the starting point, and 'E' represents the exit.

#### 🔍 How It Works

The maze solver chooses the next square in its path by picking the valid square that gives the smallest result when plugged into a custom evaluation function, determining how far it is from the solution. For each move it makes, it prints the path it is currently on, both in terms of direction ('L', 'R', 'D', 'U') and coordinates in the list.

#### 🎯 Features

- **Create Maze**: Custom create your own mazes.
- **Print Paths**: Displays the paths being tested.
- **Validate Moves**: Checks if a move is within the maze boundaries and not hitting a wall.
- **Find End**: Determines if the current path reaches the exit.
- **Custom Evaluation**: Uses a distance algorithm to find the shortest path from start to exit.

This project not only demonstrates basic pathfinding algorithms but also offers a foundation for understanding more complex maze-solving techniques. Feel free to explore and customize the maze to test different scenarios and improve the algorithm!

## Poker Game

## PyGame

## Snake Game
