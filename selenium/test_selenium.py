from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwards:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@title="北京西城区某单位出现33人集中发热，排除新冠肺炎，但与空调有关"]').click()
