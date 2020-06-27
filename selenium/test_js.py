from time import sleep

from test_stu.selenium.base import Base


class TestJS(Base):
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element=self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        sleep(4)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        #js操作时间控件
        self.driver.get('https://www.12306.cn/index/')
        sleep(5)
        time_element=self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        sleep(4)
