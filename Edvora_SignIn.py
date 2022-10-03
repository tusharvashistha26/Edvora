from lib2to3.pgen2 import driver
from tkinter import Button
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s=Service("chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app")

driver.find_element_by_xpath("//button[text()='SignIn']").click()
time.sleep(3)

driver.find_element_by_tag_name("input").send_keys("tusva")  

time.sleep(2)


driver.find_element_by_tag_name("input").send_keys("honey")
time.sleep(3)

driver.find_element_by_xpath("//button[text()='Create Account']").click()
time.sleep(3)

driver.close()
print("Your edvora account has been created successfully")
