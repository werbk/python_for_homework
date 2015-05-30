from fixture.TestBase import BaseClass
from selenium.webdriver.firefox.webdriver import WebDriver


class Contract:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company_name=None,
                 address_name=None, home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, address=None, phone=None, notes=None):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.address_name = address_name
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address = address
        self.phone = phone
        self.notes = notes


class ContractBase():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = BaseClass(self)

    def add_contract(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys()

    def add_full_name(self, Contract):
        wd = self.wd
        if Contract.first_name:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys("%s" % Contract.first_name)
        if Contract.middle_name:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys("%s" % Contract.middle_name)
        if Contract.last_name:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys("%s" % Contract.last_name)
        if Contract.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys("%s" % Contract.nickname)

    def add_title(self, Contract):
        wd = self.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % Contract.title)

    def add_company(self, Contract):
        wd = self.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % Contract.company_name)

    def add_address(self, Contract):
        wd = self.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % Contract.address_name)

    def add_phone_number(self, Contract):
        wd = self.wd
        if Contract.home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys("%s" % Contract.home)
        if Contract.mobile:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys("%s" % Contract.mobile)
        if Contract.work:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys("%s" % Contract.work)
        if Contract.fax:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys("%s" % Contract.fax)

    def add_email(self, Contract):
        wd = self.wd
        if Contract.email1:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys("%s" % Contract.email1)
        if Contract.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys("%s" % Contract.email2)
        if Contract.email3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys("%s" % Contract.email3)

    def add_homepage(self, homepage=None):
        wd = self.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % homepage)

    def add_year(self):
        wd = self.wd
        # in futures we can made function where we will sent date and it choose it with similar way as previous
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1999")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1999")

    def add_secondary_adress(self, Contract):
        wd = self.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % Contract.address)

    def add_secondary_home(self, Contract):
        wd = self.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % Contract.phone)

    def add_secondary_notes(self, Contract):
        wd = self.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % Contract.notes)

    def submit_contact(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()