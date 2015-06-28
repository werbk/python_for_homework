import random
import re
import string

from selenium import webdriver

from fixture.session_helper import SessionHelper
from tests_group.group_lib import GroupBase
from tests_contract.contact_lib import ContactBase


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