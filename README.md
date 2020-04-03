# Sudoku Solver

A program that uses the backtracking algorithm and Selenium to solve an expert sudoku board live on sudoku.com.

## How to run

1) Install all packages in your project directory
`$ pip install -r requirements.txt`

2) Run selen.py using
`$ py selen.py`

## Implementation

### Solving the board

This program will use the backtracking algorithm to solve the puzzle

1) Locate the empty space in the project. To start we will be using the number 0 to place them as Sudoku only uses numbers between 1-9.
2) Attempt to place numbers 1-9 in the place of the 0.
3) Check if the digit is valid in the current spot based on the current board.
   1) If valid, recursivly attempt to fill the board.
   2) If invalid, reset the entry just filled and try again.
4) Once the board is full, the puzzle is solved.

### Interfacing with Sudoku.com

The current plan is to use Selenium and the Selenium WebDriver to interface with sudoku.com. Ideally, the program will be able to read the given puzzle on sudoku.com/expert/ and organize it into a 2D array. The implementation mentioned above would then be implemented to solve it. After it is solved Selenium will be used to input the values on the website.
