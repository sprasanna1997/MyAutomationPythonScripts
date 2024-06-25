import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
name='Prasanna'
print('New Hello World Komalii')
driver.close()
path='D:/Automation/Openpyxl.xlsx'
workbook=openpyxl.load_workbook(path)
sheet=workbook.get_sheet_by_name('Sheet1')
rows=sheet.max_row
cols=sheet.max_column
print(rows)
print(cols)

for r in range(1,rows+1):
    for c in range(1,cols+1):
        res=sheet.cell(row=r,column=c).value
        print(res,end="                     ")

    print()
