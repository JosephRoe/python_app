from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)

print(driver.title)


time.sleep(2)
driver.close()
