#DONE: Make a function to pick an empty node
def find_empty_node(board):
    #length of board
    for row in range(len(board)):
        #length of row
        for column in range(len(board[0])):
            if board[row][column] == 0:
                #return row, column
                return (row, column)
    return None
            

#DONE: Make a function to find if the number is valid in the current board
def check_validity(board, insertion, location):
    # We need to check the row, column, and square
    # return FALSE for duplicate, TRUE if we are certain it is valid

    # Check row
    for i in range(len(board[0])):
        if board[location[0]][i]  == insertion and location[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        
            #Checks if any other is equal to the one we just added and that we arent checking the same position twice
        if board[i][location[1]]  == insertion and location[0] != i:
            return False

    # Check 3x3 box
    # This is the value of the rows and columns in each of the 9 quadrants
    # 
    # [00,01,02]  
    # [10,11,12]
    # [20,21,22]
    box_Row = location[1] // 3
    box_Column = location[0] // 3

    for i in range(box_Column * 3, box_Column*3 + 3):
        for j in range(box_Row * 3, box_Row*3 + 3):
            #Checks if any other is equal to the one we just added and that we arent checking the same position twice
            if board[i][j] == insertion and (i,j) != location:
                return False
    return True

# DONE:Implement the backtracking algorithm to solve the board
def solve_Sudoku(board):
    # recursive backtracking algorithm
    find = find_empty_node(board)
    # Base Case: if we reach this point, we are at the last iteration possible
    if not find:
        return True
    #otherwise it would have returned a row and a column and should repeat
    else:
        row, column = find 
    
    #not open ended as numbers are finite
    for i in range(1, 10):
        if check_validity(board, i, (row,column)):
            #simply add it in if valid  
            board[row][column] = i

            #RECURSION ALERT
            if solve_Sudoku(board):
                return True    
            #reset last value if it doesnt work then rerun
            board[row][column] = 0
    return False 
         


# This funtion prints the board
def print_board(board):
    #TODO refactor code from i and j to rows and columns to be more clear
    for i in range(len(board)):
        # Prints 8 dashes every 3 rows but not at the start or finish
        if i % 3==0 and i != 0:
            print(" - " * 8)
        
        for j in range(len(board)):
            # Prints a line after every 3 rows except the first and last
            if j % 3==0 and j != 0:
                print(" | ", end="")

            # Used to print
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

if __name__ == "__main__":
    # creating 9x9 sudoku board using a 2D array

    # creating a 2D array for the grid 
    board = [[0 for x in range(9)] for y in range(9)] 

    #Create board to solve
    board = [
            [0,0,0,9,0,1,6,0,0], 
            [5,0,8,0,0,0,0,0,0],
            [0,0,7,6,0,0,0,5,0], 
            [0,0,0,0,0,4,0,0,0],
            [0,0,0,0,0,0,8,0,1],
            [9,0,6,0,0,0,0,0,0],
            [0,0,5,0,0,0,4,0,0],
            [0,0,0,7,0,0,0,0,0],
            [0,3,0,0,0,9,1,6,2],
        ]

    #Testing
    print_board(board)
    solve_Sudoku(board)
    print("", end="\n")
    print("NEW LINE" * 10)  
    print("", end="\n")
    print_board(board)

    pass