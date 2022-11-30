from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_clear(browser):
  browser.get('https://webdriveruniversity.com/To-Do-List/index.html')

  # Finding input field
  input_field = browser.find_element(By.CSS_SELECTOR, '[type="text"]')

  input_field.send_keys('Clear this')
  time.sleep(1)
  input_field.clear()
  time.sleep(2)

def test_send_keys(browser):
  browser.get('https://webdriveruniversity.com/To-Do-List/index.html')

  # Finding input field
  input_field = browser.find_element(By.CSS_SELECTOR, '[type="text"]')

  # Send some text and the enter key to the input field
  input_field.send_keys('Write code', Keys.ENTER)
  time.sleep(3)

def test_click(browser):

  browser.get('https://webdriveruniversity.com/To-Do-List/index.html')

  # Finding to-do list items
  list_of_items = browser.find_elements(By.TAG_NAME, 'li')

  for item in list_of_items:
    item.click()
    time.sleep(1)
