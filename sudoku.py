#DONE: Make a function to pick an empty node
def find_empty_node(board):
    """
    Iterates through the board to find an empty node outlined by a 0
    
    Parameters: 

        board (2D List): Contains the board going to be solved.

    Returns:

        None
    """

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
    """
    Iterates through the board to check if a certain insertion is valid at the current location
    
    Parameters: 

        board (2D list): Contains the board going to be solved.
        insertion (int) : Contains the number being inserted to the empty node
        location (tuple) : Contains the coordinate location where the number is being inserted as (row,column)
    
    Returns:

        False: if the number being inserted is invalid
        True: if the number is valid

    """
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
    """
    Uses the backtracking algorithm to solve the puzzle
    
    Parameters: 

        board (2D list): Contains the board going to be solved.
    
    Returns:

        True: The solved board

    """
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