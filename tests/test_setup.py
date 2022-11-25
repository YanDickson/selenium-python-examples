def test_pytest_setup():
  assert True

def test_browser_setup(browser):
  browser.get('https://google.com')
  