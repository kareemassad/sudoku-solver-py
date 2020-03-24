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

time.sleep(2)
#returns an exception if element "game-table" is not located
board = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "game-table"))
    )
cells = board.find_element_by_class_name("game-cell")

print(board)
print(cells)
# driver.close()
