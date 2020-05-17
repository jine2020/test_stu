from test_stu.pageobject.loginqw_po.register import Register
from selenium.webdriver.remote.webdriver import WebDriver


class Login:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def scanf(self):
        pass

    def goto_register(self):
        self.driver.find_element('.login_registerBar_link').click()
        return Register(self.driver)