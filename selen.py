from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# importing sudoku.py
from sudoku import find_empty_node, solve_Sudoku, check_validity

#pick browser
driver = webdriver.Chrome('chromedriver\chromedriver.exe')
#pick site being used
driver.get("https://sudoku.com/expert/")
#confirm the title has sudoku in it
assert "sudoku" in driver.title

# not sure if this is necessary tbh
while True:

    time.sleep(2)
    #returns an exception if element "game-table" is not located
    gameTable = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "game-table"))
        )
    gameCell = gameTable.find_elements_by_class_name("game-cell")

    #get the initial values of the board given at sudoku.com
    i = 0
    givenBoard = [[]]


    for x, cell in enumerate(gameCell):
        if x % 9 == 0 and x != 0:
            givenBoard.append([])
            i = i + 1
        value = cell.find_element_by_class_name("cell-value")
        try:
            text = value.find_element_by_tag_name("svg")
        except:
            givenBoard[i].append(0)
            continue

        width, height = (text.get_attribute("width"), text.get_attribute("height"))
        # width = int(width)
        # height = int(height)


    # Hacky way to detect the numbers on the board as sudoku.com uses SVGS instead of numbers. This checks
    # for height or the special s char at the svg. The dictionary contains 1>5,7,9 and 6,8 are the same size
    # so they use the s char.
        if (width, height) == (22,32):
            s = text.find_element_by_tag_name("path").get_attribute("d")[0:6]
            if s == "M10.53":
                givenBoard[i].append(8)
            else:
                givenBoard[i].append(6)


        dict = {
            (12,30) : 1,
            (20,31) : 2,
            (21,32) : 3,
            (24,30) : 4,
            (21,31) : 5,
            (20,30) : 7,
            (23,32) : 9,
        }
        givenBoard[i].append(dict.get((width,height)))
    
    #creating a backup
    backup = list(map(list, givenBoard))
    solve_Sudoku(givenBoard)

    print(backup)
    print(givenBoard)

    #using numpad to input
    #numpad chain is numpad > numpad-title
    numpad = driver.find_elements_by_class_name("numpad-title")

    #game input 
    for yp, y in enumerate(backup):
        for xp, x in enumerate(y):
            if x == 0:
                gameCell[yp*9 + xp].click()
                numpad[givenBoard[yp][xp] - 1].click()
        #sometimes a popup blocks it and causes a crash
        if yp == 6:
            driver.execute_script("arguments[0].scrollIntoView();", gameTable)

    play_again = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.CLASS_NAME, "button-play")
    )

    ## Comment the bottom 2 lines and the while loop above to make it run only once 
    time.sleep(2)
    driver.execute_script("arguments[0].click();", play_again)

    #Closes the page
    driver.close()
