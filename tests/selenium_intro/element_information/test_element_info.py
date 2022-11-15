from selenium.webdriver.common.by import By

class TestClass:

  def test_is_selected(self, browser):
    browser.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

    checked_item = browser.find_element(By.CSS_SELECTOR, '[value="option-3"]')
    seleted = checked_item.is_selected()
    assert seleted == True

  def test_element_text(self, browser):
    browser.get('https://webdriveruniversity.com/Click-Buttons/index.html')

    page_heading = browser.find_element(By.TAG_NAME, 'h1')
    text = page_heading.text
    assert text == 'Lets Get Clicking!'

  def test_is_displayed(self, browser):
    browser.get('https://webdriveruniversity.com/Click-Buttons/index.html')

    page_heading = browser.find_element(By.TAG_NAME, 'h1')
    is_it = page_heading.is_displayed()
    assert is_it == True
