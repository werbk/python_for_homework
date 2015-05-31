from selenium.webdriver.firefox.webdriver import WebDriver
from tests_group.group_lib import GroupBase
from tests_contract.contract_lib import ContactBase


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % user_name)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()


class BaseClass():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

        self.session = SessionHelper(self)
        self.group = GroupBase(self)
        self.contact = ContactBase(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def restore(self):
        wd = self.wd
        wd.quit()

