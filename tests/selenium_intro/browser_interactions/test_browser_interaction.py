from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestBrowserInteractions:

  def test_navigate(self, browser):
    # Navigate to the URL
    browser.get('https://webdriveruniversity.com/')

  def test_current_url(self, browser):
    url = 'https://webdriveruniversity.com/Page-Object-Model/index.html'

    # Navigate to the URL
    browser.get(url)

    # Find the Contact Us element link and click it
    browser.find_element(By.LINK_TEXT, 'Contact Us').click()

    # Wait for the URL to change
    WebDriverWait(browser, 10).until(EC.url_changes(url))

    # Get the current URL of the browser
    new_url = browser.current_url

    # Verify current URL and title 
    assert new_url == 'https://webdriveruniversity.com/Contact-Us/contactus.html'

  def test_title(self, browser):
    browser.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

    # Get the title of the current page from the browser
    page_title = browser.title

    # Verify the title that is retrieved
    assert page_title == 'WebDriver | Contact Us'

  def test_refresh(self, browser):
    browser.get('https://webdriveruniversity.com/Contact-Us/contactus.html')
    time.sleep(3)

    # Refreshes the current page
    browser.refresh()

    time.sleep(1)

  def test_alert(self, browser):
    browser.get('https://webdriveruniversity.com/Popup-Alerts/index.html')
    button = browser.find_element(By.CSS_SELECTOR, '#button4 > p')

    # Click to trigger the alert
    button.click()

    # Wait until the alert is present
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())

    # WebDriverWait(browser, 10).until(EC.alert_is_present())
    # alert = browser.switch_to.alert

    # Get the alert text
    text = alert.text
    time.sleep(1)

    # Click the OK button on the Alert
    alert.accept()
    time.sleep(2)

    # Click to trigger the alert
    button.click()
    time.sleep(1)

    # Click the Cancel button on the alert
    alert.dismiss()
    time.sleep(2)

    assert text == 'Press a button!'
