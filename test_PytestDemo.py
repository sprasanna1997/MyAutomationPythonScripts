import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class TestPractice:

    #Variable Name
    name="Prasanna Senthilkumar"
    email="ji@gmail.com"
    address="80, Ashok Nagar \n Chennai \n Tamilnadu"
    password="Dummypassowrd"
    @pytest.fixture(autouse=True)
    def setup(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach',True)
        self.driver= webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_element_textbox(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()=' Elements']"))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()=' Text Box']"))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[contains(@id,'fullname')]"))).send_keys(self.name)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[contains(@id,'email')]"))).send_keys(self.email)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[contains(@id,'address')]"))).send_keys(self.address)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[contains(@id,'password')]"))).send_keys(self.password)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "// input[ @ value = 'Submit']"))).click()

    def test_element_checkbox(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()=' Elements']"))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,"//a[text()=' Check Box']"))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,"(//span[@class='plus'])[1]"))).click()
        time.sleep(2)
        self.wait.until(ec.element_to_be_clickable((By.XPATH,"(//span[@class='plus'])[1]"))).click()
        time.sleep(2)
        self.wait.until(ec.element_to_be_clickable((By.XPATH,"(//input[@type='checkbox'])[6]"))).click()
        time.sleep(2)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "(//span[@class='plus'])[1]"))).click()
        time.sleep(2)
