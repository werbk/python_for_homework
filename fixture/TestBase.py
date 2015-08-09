import random
import re
import string
from selenium import webdriver
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
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self,):
        wd = self.app.wd

        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, user_name, password):
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)


class BaseClass():
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognize browser %s' % browser)

        #self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupBase(self)
        self.contact = ContactBase(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def restore(self):
        wd = self.wd
        wd.quit()


def clear(info):
    return re.sub('[() -]', '', info)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' #+ string.punctuation
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])