# -*- coding: utf-8 -*-
import nose

from selenium.webdriver.firefox.webdriver import WebDriver
from TestBase import Profinity, UserLogin
from contract_lib import ContractBase


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestContact(ContractBase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_of_add_new_valid_contact(self):
        """
        Validation of add correct new contact with full data
        """

        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, UserLogin.name, UserLogin.password)

        self.add_contract(wd)
        self.add_full_name(wd, first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                           middle_name=Profinity.correct_data, nickname=Profinity.correct_data)

        self.add_title(wd, title=Profinity.correct_data)
        self.add_company(wd, company_name=Profinity.correct_data)
        self.add_address(wd, address_name=Profinity.correct_data)

        self.add_phone_number(wd, work=Profinity.correct_phone_number, fax=Profinity.correct_phone_number,
                              home=Profinity.correct_phone_number, mobile=Profinity.correct_phone_number)

        self.add_email(wd, email1=Profinity.correct_email, email2=Profinity.correct_email,
                       email3=Profinity.correct_email)

        self.add_homepage(wd, homepage=Profinity.correct_data)
        self.add_year(wd)

        # secondary data
        self.add_secondary_adress(wd, address=Profinity.correct_data)
        self.add_secondary_home(wd, phone=Profinity.correct_data)
        self.add_secondary_notes(wd, notes=Profinity.correct_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def tearDown(self):
        # Here should use some method to delete test data, i will try do it ASAP
        # TODO:
        '''self.wd.find_element_by_link_text("home").click()
        if not self.wd.find_element_by_id("MassCB").is_selected():
            self.wd.find_element_by_id("MassCB").click()
        self.wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()'''

        self.wd.find_element_by_link_text("Logout").click()

if __name__ == "__main__":
    nose.run(argv=["nosetests", "tests_contract.py", "--verbosity=2"])