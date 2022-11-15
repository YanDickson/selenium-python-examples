# Examples for Concepts Reviewed in the  Selenium Python Workshop
> This project shows coding examples for the concepts reviewed in the Selenium-Python workshop.

## Directories to look for
- python_intro - code examples of introduction to python; basic python concepts to kick-start a project.
- tests/pytest_intro - code example for introduction to pytest; creating tests and desiging assertions.
- tests/selenium_intro - code examples with Selenium-Python examples and working with page objects.

## Technologies Used
- Python - version 3.10
- Pytest
- Selenium

## Exercises
The solutions to the exercises can be found in the following directories:
- python_exercises
- tests/pytest_exercise
- tests/qw_test_store

## Setup
To setup this project follow the steps below.
1. Download and install Python locally. You can download Python from [Python.org](https://www.python.org/downloads/).
2. Install pipenv locally. To install pipenv, run `pip install pipenv` from the command line.
3. Clone this repository.
4. To install the project dependencies by running `python3 -m pipenv install` from the root of the project.

## Webdriver Setup
For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/).

You will also need to install the latest version of the WebDriver executable for Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

To verify the setup was successful, run the command `python3 -m pipenv run pytest tests/test_selenium.py`.

## Test Execution
To execute tests run the following commands:
- `python3 -m pipenv run pytest` for all tests.
- `python3 -m pipenv run pytest [path/to/test/file]` to run a single test.

Alternatively, you can start the pipenv shell to run the tests using a shorter version of the above commands. To start the shell run the command `python3 -m pipenv shell`.
- run `pytest` to execute all tests.
- run `pytest [path/to/test/file]` to execute a single test.