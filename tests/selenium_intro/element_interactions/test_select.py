from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def test_select_value(browser):
  browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

  # Select an element in the first dropdown list based on its value
  menu_1 = browser.find_element(By.ID, 'dropdowm-menu-1')

  # Use select element to initialize Select class
  select_1 = Select(menu_1)

  # Select an element by its value
  select_1.select_by_value('python')
  time.sleep(2)
  
def test_select_index(browser):
  browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

  # Select an element in the second dropdown list based on its index in the list
  menu_2 = browser.find_element(By.ID, 'dropdowm-menu-2')

  # Use select element to initialize Select class
  select_2 = Select(menu_2)

  # Select an element by its index
  select_2.select_by_index(1)
  time.sleep(2)

def test_select_text(browser):
  browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

  # Select an element in the third dropdown list based on its visible text
  menu_3 = browser.find_element(By.ID, 'dropdowm-menu-3')

  # Use select element to initialize Select class
  select_3 = Select(menu_3)

  # Select an element by its visible text
  select_3.select_by_visible_text('JQuery')
