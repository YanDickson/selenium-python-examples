from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class TestSelect:
  '''Using the webdriver Select class'''

  def test_select(self, browser):
    browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

    # Select an element in the first dropdown list based on its value
    menu_1 = browser.find_element(By.ID, 'dropdowm-menu-1')
    select_1 = Select(menu_1)
    select_1.select_by_value('python')
    time.sleep(2)

    # Select an element in the first dropdown list based on its index in the list
    menu_2 = browser.find_element(By.ID, 'dropdowm-menu-2')
    select_2 = Select(menu_2)
    select_2.select_by_index(1)
    time.sleep(2)
