from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://training.openspan.com/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("sharan")
driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("155113412")



