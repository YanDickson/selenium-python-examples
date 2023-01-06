from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def test_select(browser):
  browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

  # Select an element in the first dropdown list based on its value
  menu_1 = browser.find_element(By.ID, 'dropdowm-menu-1')

  # Use select element to initialize Select class
  select_1 = Select(menu_1)

  # Select an element by its value
  select_1.select_by_value('python')
  time.sleep(2)
  

  # Select an element in the first dropdown list based on its index in the list
  menu_2 = browser.find_element(By.ID, 'dropdowm-menu-2')

  # Use select element to initialize Select class
  select_2 = Select(menu_2)

  # Select an element by its index
  select_2.select_by_index(1)
  time.sleep(2)
