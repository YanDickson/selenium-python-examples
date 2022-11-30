from selenium.webdriver.common.by import By
import pytest

def test_find_elements(browser):
  pytest.skip()

  # https://webdriveruniversity.com/Contact-Us/contactus.html

  # Finding a list of elements
  
  list_items = browser.find_elements(By.CLASS_NAME, 'feedback-input')

  # Finding a single element

  first_name_field = browser.find_element(By.NAME, 'first_name')

  comments_field = browser.find_element(By.TAG_NAME, 'textarea')

  submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

  username_field = browser.find_element(By.ID, 'contact_form')

  nav_text = browser.find_element(By.LINK_TEXT, 'WebdriverUniversity.com (New Approach To Learning)')
  
  partail_nav_text = browser.find_element(By.PARTIAL_LINK_TEXT, 'WebdriverUniversity.com')

  reset_button = browser.find_element(By.XPATH, '//*[@id="form_buttons"]/input[1]')
