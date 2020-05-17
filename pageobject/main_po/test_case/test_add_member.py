from time import sleep

from test_stu.pageobject.main_po.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        sleep(2)
        assert "abcdefffff" in add_member.get_member()
