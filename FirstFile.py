from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
name='Prasanna'
print('New Hello World Komalii')