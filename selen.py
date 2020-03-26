from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#pick browser
driver = webdriver.Chrome('chromedriver\chromedriver.exe')
#pick site being used
driver.get("https://sudoku.com/expert/")
#confirm the title has sudoku in it
assert "sudoku" in driver.title

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
        width = int(width)
        height = int(height)

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

print(i)

print(gameTable)
print(gameCell)

#Closes the page
driver.close()
