from time import sleep

from selenium.webdriver.common.by import By

from test_stu.selenium.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get('https://wwww.baidu.com')
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'登录').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'立即注册').click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(3)
