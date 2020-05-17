from test_stu.pageobject.loginqw_po.index import Index


class TestRegister:
    def setup(self):
        self.index=Index()

    def test_register(self):
        self.index.goto_register().register()