from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_visibility_of(browser):
  # Initialises wait class
  wait = WebDriverWait(browser, 10)

  browser.get('https://webdriveruniversity.com/Ajax-Loader/index.html')

  button = browser.find_element(By.CSS_SELECTOR, '#button1 > p')

  # Waits until the given element is visible on the page
  wait.until(EC.visibility_of(button))
  
  assert button.is_displayed() == True

def test_sleep(browser):
  browser.get('https://webdriveruniversity.com/Login-Portal/index.html')

  username = browser.find_element(By.ID, 'text')
  password = browser.find_element(By.ID, 'password')
  login_button = browser.find_element(By.ID, 'login-button')

  username.send_keys('testUser')
  time.sleep(3)

  password.send_keys('testpassword')
  time.sleep(3)

  login_button.click()
  time.sleep(3)

def test_element_to_be_present(browser):
  wait = WebDriverWait(browser, 10)

  browser.get('https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html')
  
  browser.find_element(By.ID, 'myInput').send_keys('Z')

  # Waits until the given locator is present in the DOM
  wait.until(EC.presence_of_element_located((By.ID, 'myInputautocomplete-list')))

  list_item = browser.find_element(By.CSS_SELECTOR, '#myInputautocomplete-list > div:nth-child(1)')
  list_item.click()
  time.sleep(1)

def test_title_contains(browser):
  wait = WebDriverWait(browser, 10)

  browser.get('https://webdriveruniversity.com/To-Do-List/index.html')

  # Waits until the title of the page contains the given text
  wait.until(EC.title_contains('To Do List'))

  browser.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('Do python workshop')
  time.sleep(1)

def test_title_contains(browser):
  wait = WebDriverWait(browser, 10)

  browser.get('https://webdriveruniversity.com/To-Do-List/index.html')
  
  # Waits until the title of the page matches the given string
  wait.until(EC.title_is('WebDriver | To Do List'))

  browser.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('Do python workshop')
  time.sleep(1)

def test_url_changes(browser):
  url = 'https://webdriveruniversity.com/Page-Object-Model/index.html'
  wait = WebDriverWait(browser, 10)

  browser.get(url)
  
  browser.find_element(By.LINK_TEXT, 'Contact Us').click()

  # Waits until the given URL changes
  wait.until(EC.url_changes(url))

  assert browser.find_element(By.NAME, 'contactme').text == 'CONTACT US'

def test_text_to_be_present(browser):
  url = 'https://webdriveruniversity.com/Accordion/index.html'
  locator = (By.ID, 'hidden-text')
  expected_text = 'LOADING COMPLETE.'
  wait = WebDriverWait(browser, 10)

  # Navigate to the URL
  browser.get(url)

  # Wait for the element to have the text
  # EC.text_to_be_present_in_element(locator, text)
  wait.until(EC.text_to_be_present_in_element(locator, expected_text))
  
  # Verify the expected text is now on the element
  text_appear_box = browser.find_element(By.ID, 'hidden-text')
  assert text_appear_box.text == expected_text
