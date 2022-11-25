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

  def test_iframe(self, browser):
    browser.get('https://webdriveruniversity.com/IFrame/index.html')

    # Find the iframe element
    iframe_element = browser.find_element(By.ID, 'frame')

    # 1. Switch to the iframe
    browser.switch_to.frame(iframe_element)
    
    # 2. Interact with element in frame
    contact_us_link = browser.find_element(By.LINK_TEXT, 'Contact Us')
    contact_us_link.click()
    time.sleep(2)

    # 3. Switch back to default content
    browser.switch_to.default_content()

    # 4. Interact with element outside of frame
    navbar_link = browser.find_element(By.ID, 'nav-title')
    navbar_link.click()
    time.sleep(2)
