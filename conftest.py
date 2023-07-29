import time

import pytest
from selenium import webdriver


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    time.sleep(3)
    yield
    driver.quit()