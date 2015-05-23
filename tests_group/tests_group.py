# -*- coding: utf-8 -*-
import unittest
import nose

from selenium.webdriver.firefox.webdriver import WebDriver
from TestBase import UserLogin
from group_lib import Group, GroupTestBase


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Precondition4Group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def tearDown(self):
        # We should delete all created test form
        self.delete_group()

        self.wd.find_element_by_link_text("Logout").click()
        self.wd.quit()


class TestGroup(GroupTestBase, Precondition4Group):

    def test_create_group(self):
        """Validation of correct create test group"""

        wd = self.wd
        self.open_home_page(wd)

        self.login(wd, UserLogin.name, UserLogin.password)
        self.create_group(wd, Group(group_name='test', group_header='test', group_footer='test'))

        self.click_group_page(wd)


if __name__ == "__main__":
    nose.run(argv=["nosetests", "tests_group.py", "--verbosity=2"])