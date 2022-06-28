import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


os.environ['PATH'] += r"C:\SeleniumDriver"
driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)

boton1 = driver.find_element_by_id("downloadButton")
boton1.click()

confirmacion = driver.find_element_by_class_name("progress-label")
time.sleep(10)
if confirmacion.text == "Complete!":
    print(f"Complete!")
else:
    print(f"Cargando!")

driver.close()
