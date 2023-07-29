import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select


def met():
    driver=webdriver.Chrome()
    driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
    driver.maximize_window()
    time.sleep(3)
    ele = driver.find_element(By.XPATH,"//button[@id='product-menu-toggle']")
    act = ActionChains(driver)
    act.move_to_element(ele).perform()
    time.sleep(3)
    ele2=driver.find_element(By.XPATH,"//a[@class='menu-item-live']").click()
    time.sleep(3)















met()
