from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestWaitConditions:
  '''Examples of implementing wait strategies'''

  def test_explicit_wait(self, browser):
    browser.get('https://webdriveruniversity.com/Ajax-Loader/index.html')

    button = browser.find_element(By.CSS_SELECTOR, '#button1 > p')

    wait = WebDriverWait(browser, 10)
    # Waits until the given element is visible on the page
    wait.until(EC.visibility_of(button))
    is_it = button.is_displayed()
    assert is_it == True

  def test_sleep(self, browser):
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

  def test_element_to_be_present(self, browser):
    browser.get('https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html')
    input_field = browser.find_element(By.ID, 'myInput')

    input_field.send_keys('Z')

    wait = WebDriverWait(browser, 10)
    # Waits until the given locator is present in the DOM
    wait.until(EC.presence_of_element_located((By.ID, 'myInputautocomplete-list')))

    list_item = browser.find_element(By.CSS_SELECTOR, '#myInputautocomplete-list > div:nth-child(1)')
    list_item.click()
    time.sleep(1)

  def test_title_contains(self, browser):
    browser.get('https://webdriveruniversity.com/To-Do-List/index.html')
    wait = WebDriverWait(browser, 10)
    # Waits until the title of the page contains the given text
    wait.until(EC.title_contains('To Do List'))

    browser.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('Do python workshop')
    time.sleep(1)

  def test_title_contains(self, browser):
    browser.get('https://webdriveruniversity.com/To-Do-List/index.html')
    wait = WebDriverWait(browser, 10)
    # Waits until the title of the page matches the given string
    wait.until(EC.title_is('WebDriver | To Do List'))

    browser.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('Do python workshop')
    time.sleep(1)

  def test_url_changes(self, browser):
    url = 'https://webdriveruniversity.com/Page-Object-Model/index.html'
    browser.get(url)
    browser.find_element(By.LINK_TEXT, 'Contact Us').click()

    wait = WebDriverWait(browser, 10)
    # Waits until the given URL changes
    wait.until(EC.url_changes(url))

    assert browser.find_element(By.NAME, 'contactme').text == 'CONTACT US'
 