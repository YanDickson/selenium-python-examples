from selenium.webdriver.common.by import By
import pytest

def test_find_elements(browser):
  pytest.skip()

  # Finding a list of elements

  # https://webdriveruniversity.com/To-Do-List/index.html
  list_items = browser.find_elements(By.TAG_NAME, 'li')


  # Finding a single element

  # https://webdriveruniversity.com/Contact-Us/contactus.html
  first_name_field = browser.find_element(By.NAME, 'first_name')

  comments_field = browser.find_element(By.TAG_NAME, 'textarea')

  submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

  # https://webdriveruniversity.com/Login-Portal/index.html
  username_field = browser.find_elemet(By.ID, 'text')
