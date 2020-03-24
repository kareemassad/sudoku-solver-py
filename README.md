# Sudoku Solver

A program that uses the backtracking algorithm to solve a sudoku board.

## The Algorithm

1) Locate the empty space in the project. To start we will be using the number 0 to place them as Sudoku only uses numbers between 1-9.
2) Attempt to place numbers 1-9 in the place of the 0.
3) Check if the digit is valid in the current spot based on the current board.
   1) If valid, recursivly attempt to fill the board.
   2) If invalid, reset the entry just filled and try again.
4) Once the board is full, the puzzle is solved.
