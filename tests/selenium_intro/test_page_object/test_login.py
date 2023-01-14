from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login(browser):
  login_url = 'https://webdriveruniversity.com/Login-Portal/index.html'

  browser.get(login_url)

  username_field = browser.find_element(By.ID, 'text')
  password_field = browser.find_element(By.ID, 'password')
  login_button = browser.find_element(By.ID, 'login-button')

  username_field.send_keys('testUser')
  password_field.send_keys('userpassword')
  login_button.click()

  assert browser.switch_to.alert.text == 'validation failed'

def test_login_page_object(browser):
  login_page = LoginPage(browser)
  
  browser.get(login_page.url)
  login_page.login_user()
  assert browser.switch_to.alert.text == 'validation failed'
