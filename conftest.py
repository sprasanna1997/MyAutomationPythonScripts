import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    driver= webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    request.cls.driver=driver
    yield
    driver.close()