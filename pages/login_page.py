from selenium.webdriver.common.by import By

class LoginPage:

  # CLASS VARIABLES
  url = 'https://webdriveruniversity.com/Login-Portal/index.html'

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # LOCATORS
  def username_field(self): 
    return self.browser.find_element(By.ID, 'text')

  def password_field(self):
    return self.browser.find_element(By.ID, 'password')

  def login_button(self):
    return self.browser.find_element(By.ID, 'login-button')

  # PAGE METHODS
  def login_user(self):
    self.username_field().send_keys('testUser')
    self.password_field().send_keys('userpassword')
    self.login_button().click()
    