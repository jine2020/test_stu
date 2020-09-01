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
        self.driver.find_element(By.XPATH,'//*[@title="//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]"]').click()
