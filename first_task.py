# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
import nose


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_create_group(self):
        """Validation of correct create test group"""
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()
        self.assertTrue(success)
    
    def tearDown(self):
        success = True
        # We should delete all created test form
        self.wd.find_element_by_link_text("groups").click()
        self.wd.find_element_by_css_selector("span.group").click()
        if not self.wd.find_element_by_name("selected[]").is_selected():
            self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()
        self.wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
        self.wd.quit()

if __name__ == "__main__":
    nose.run(argv=["nosetests", "first_task.py", "--verbosity=2"])