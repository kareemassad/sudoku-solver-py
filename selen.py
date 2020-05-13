# TODO: Create a function to print the completed board in console.
# TODO: Create a function that tracks the total time the program is running. This stat will differ based on system but would be interesting to see.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# importing sudoku.py
from sudoku import find_empty_node, solve_Sudoku, check_validity

### PARAMS THAT COULD BECOME PART OF A GUI IN THE FUTURE
# Change this to equal the number of Sudoku boards you want solved.
numberToSolve = 1
# Change to True if you want the browser to close after
closeBrowser = True
# Change to True of you want it to display number of boards solved
printSolved = True
# Change to True if you want Time Elapsed information printed in console.
# timeCount = True

# if timeCount:
#     timeStart = time.process_time()
#     pass

#pick browser
driver = webdriver.Chrome('chromedriver\chromedriver.exe')
#pick site being used
driver.get("https://sudoku.com/expert/")
#confirm the title has sudoku in it to check for correct page.
assert "sudoku" in driver.title

# not sure if this is necessary tbh
count = 0
while count != numberToSolve:
    count = count + 1

    time.sleep(2)
    #returns an exception if element "game-table" is not located
    gameBoard = WebDriverWait(driver,8).until(
        EC.presence_of_element_located((By.CLASS_NAME, "game-table"))
        )
    gameCells = gameBoard.find_elements_by_class_name("game-cell")

    #get the initial values of the board given at sudoku.com
    i = 0
    sudokuTable = [[]]

    for x, cell in enumerate(gameCells):
        if x % 9 == 0 and x != 0:
            sudokuTable.append([])
            i = i + 1
        value = cell.find_element_by_class_name("cell-value")
        try:
            text = value.find_element_by_tag_name("svg")
        except:
            sudokuTable[i].append(0)
            continue

        width, height = (text.get_attribute("width"), text.get_attribute("height"))
        width = int(width) 
        height = int(height)


    # Hacky way to detect the numbers on the board as sudoku.com uses SVGS instead of numbers. This checks
    # for height or the special s char at the svg. The dictionary only contains 1-5,7,9 as 6,8 are the same size
    # so they use the special s char.
        s = text.find_element_by_tag_name("path").get_attribute("d")[0:6]
        if s == "M10.53":
            sudokuTable[i].append(8)
        elif s == "M10.96":
            sudokuTable[i].append(6)
        else:
            dict = {
            (12,30) : 1,
            (20,31) : 2,
            (21,32) : 3,
            (24,30) : 4,
            (21,31) : 5,
            (20,30) : 7,
            (23,32) : 9,
        }
            #This spacing error was really hard to notice haha
            sudokuTable[i].append(dict.get((width,height)))
    
    #creating a backup
    backup = list(map(list, sudokuTable))
    solve_Sudoku(sudokuTable)

    ### TESTING
    # print(backup)
    # print(sudokuTable)

    #using numpad to input
    #numpad chain is numpad > numpad-title
    numpad = driver.find_elements_by_class_name("numpad-item")

    #game input 
    for yp, y in enumerate(backup):
        for xp, x in enumerate(y):
            if x == 0:
                gameCells[yp*9 + xp].click()
                numpad[sudokuTable[yp][xp] - 1].click()
        #sometimes a popup blocks it and causes a crash
        if yp == 6:
            driver.execute_script("arguments[0].scrollIntoView();", gameBoard)

    play_again = WebDriverWait(driver, 10).until(
        # not sure why but needed double braces to work
        EC.presence_of_element_located((By.CLASS_NAME, "button-play"))
    )

    ## Comment the bottom 2 lines and the while loop above to make it run only once 
    time.sleep(2)
    driver.execute_script("arguments[0].click();", play_again)

if printSolved:
    print("This program has solved " + str(numberToSolve) + " Sudoku boards.")

if closeBrowser:
    driver.close()

# if timeCount :
#     timeFinal = time.process_time() - timeStart
#     print("Time elapsed: ", timeFinal - timeStart, "seconds")