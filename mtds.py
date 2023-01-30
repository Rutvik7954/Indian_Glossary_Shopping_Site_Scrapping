import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\BAPS\Downloads\chromedriver.exe")

def get_page(str1):
    driver.get(str1)

def get_elements_using_class(str2):
    elements = driver.find_elements(by=By.CLASS_NAME, value=str2)
    return elements
