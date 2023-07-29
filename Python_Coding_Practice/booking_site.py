from datetime import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

class Sample:
  def login(self):
    driver = webdriver.Chrome()
    driver.get("https://www.booking.com/")
    city = driver.find_element(By.XPATH, "//input[@name='ss']").click()
    city.sendkeys("Ahemdabad")
    Checkin_date = driver.find_element(By.XPATH, "//button[@data-testid='date-display-field-start']")
    Checkin_date.click()
    selectdate = driver.find_element(By.XPATH, "//span[@data-date='2023-07-05']")
    selectdate.click()
    checkout_date =driver.find_element(By.XPATH,"//button[@class='d47738b911 e246f833f7 fe211c0731'][2]")
    checkout_date.click()
    selectdate2 = driver.find_element(By.XPATH, "//span[@data-date='2023-07-20']").click()
    searchbutton = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)


obj=Sample()
obj.login()


