from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.ID, 'corp_name').send_keys('aaaaaa')
        self.driver.find_element(By.ID, 'manager_name').send_keys("aaaaaa")
        sleep(5)
        self.driver.quit()
        return True
