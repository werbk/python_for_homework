from fixture.variables import UserLogin
from functools import wraps
from fixture.variables import Profinity
from sys import maxsize
import re


def connection(fn):
    @wraps(fn)
    def wrapper(app):
        app.session.login(UserLogin.name, UserLogin.password)
        try:
            fn(app)
        finally:
            app.session.logout()

    return wrapper


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company_name=None,
                 address_name=None, home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, address=None, phone=None, notes=None, add_year=None, id=None, contact_name=None):

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
        self.add_year = add_year
        self.contract_name = contact_name
        self.id = id

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s' % (self.id, self.first_name,
                                                                                self.last_name, self.nickname,
                                                                                self.title, self.company_name,
                                                                                self.address_name, self.home,
                                                                                self.mobile, self.work , self.fax,
                                                                                self.email1, self.email2, self.email3,
                                                                                self.homepage, self.address, self.phone,
                                                                                self.notes, self.contract_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and \
                self.last_name == other.last_name

    def if_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class ContactBase():
    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_contract_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contract_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/')): #and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("home").click()

    def validation_of_contact_exist(self):
        if self.count() == 0:
            self.create((Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                        middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                        phone=Profinity.correct_phone_number, work=Profinity.correct_phone_number,
                        home=Profinity.correct_phone_number,mobile=Profinity.correct_phone_number)))

    def edit_contract(self, Contract):
        wd = self.app.wd
        self.open_contract_page()

        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.contract_field(Contract)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contract_page()
        contract_cache = None

    def contract_field(self, Contact):
        wd = self.app.wd
        a = dir(Contact)
        '''for k in dir(Contact)[5:-1]:
            if k != 'add_year':
                wd.find_element_by_name("%s" % k).click()
                wd.find_element_by_name("%s" % k).clear()
                wd.find_element_by_name("%s" % k).send_keys("%s" % Contact.key(k))'''


        if Contact.first_name:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys("%s" % Contact.first_name)
        if Contact.middle_name:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys("%s" % Contact.middle_name)
        if Contact.last_name:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys("%s" % Contact.last_name)
        if Contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys("%s" % Contact.nickname)

        if Contact.title:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys("%s" % Contact.title)

        if Contact.company_name:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys("%s" % Contact.company_name)

        if Contact.address_name:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys("%s" % Contact.address_name)

        if Contact.home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys("%s" % Contact.home)
        if Contact.mobile:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys("%s" % Contact.mobile)
        if Contact.work:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys("%s" % Contact.work)
        if Contact.fax:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys("%s" % Contact.fax)

        if Contact.email1:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys("%s" % Contact.email1)
        if Contact.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys("%s" % Contact.email2)
        if Contact.email3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys("%s" % Contact.email3)

        if Contact.homepage:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys("%s" % Contact.homepage)

        if Contact.add_year:
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

        if Contact.address:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys("%s" % Contact.address)

        if Contact.phone:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys("%s" % Contact.phone)

        if Contact.notes:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys("%s" % Contact.notes)

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        self.contract_field(Contact)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        contract_cache = None

    def delete_contact(self):
        self.delete_contact_by_index(0)

    contract_cache = None

    def get_contact_list(self):
        if self.contract_cache is None:
            wd = self.app.wd
            self.open_contract_page()
            contract_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                my_id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text.splitlines()
                all_email = cells[4].text.splitlines()
                adress = cells[3].text.splitlines()

                a = None
                b = None
                c = None
                d = None
                e = None
                f = None
                g = None
                h = None
                if all_phones:
                    if len(all_phones)>0 and all_phones[0]:
                        a=all_phones[0]
                    if len(all_phones)>1 and all_phones[1]:
                        b=all_phones[1]
                    if len(all_phones)>2 and all_phones[2]:
                       c = all_phones[2]
                    if len(all_phones)>3 and all_phones[3]:
                     d = all_phones[3]

                if all_email:
                    if len(all_email)>0 and all_email[0]:
                        e = all_email[0]
                    if len(all_email)>1 and all_email[1]:
                        f = all_email[1]
                    if len(all_email)>2 and all_email[2]:
                        g = all_email[2]
                if adress:
                    h = adress[0]

                contract_cache.append(Contact(first_name=cells[1].text, last_name=cells[2].text, id=my_id, home=a,
                                              mobile = b, work = c, phone = d, email1 = e, email2= f,
                                              email3 = g , address = h))

            return contract_cache

    def get_contact_list_without_none(self):
        if self.contract_cache is None:
            wd = self.app.wd
            self.open_contract_page()
            contract_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                my_id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text.splitlines()
                all_email = cells[4].text.splitlines()
                adress = cells[3].text.splitlines()

                a = ''
                b = ''
                c = ''
                d = ''
                e = ''
                f = ''
                g = ''
                h = ''
                if all_phones:
                    if len(all_phones)>0 and all_phones[0]:
                        a=all_phones[0]
                    if len(all_phones)>1 and all_phones[1]:
                        b=all_phones[1]
                    if len(all_phones)>2 and all_phones[2]:
                       c = all_phones[2]
                    if len(all_phones)>3 and all_phones[3]:
                     d = all_phones[3]

                if all_email:
                    if len(all_email)>0 and all_email[0]:
                        e = all_email[0]
                    if len(all_email)>1 and all_email[1]:
                        f = all_email[1]
                    if len(all_email)>2 and all_email[2]:
                        g = all_email[2]
                if adress:
                    h = adress[0]

                contract_cache.append(Contact(first_name=cells[1].text, last_name=cells[2].text, id=my_id, home=a,
                                              mobile = b, work = c, phone = d, email1 = e, email2= f,
                                              email3 = g , address = h))

            return contract_cache

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contract_page()

        wd.find_elements_by_name("selected[]")[index].click()

        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        contract_cache = None

    def edit_contract_by_index(self, Contract, index):
        wd = self.app.wd
        self.open_contract_page()

        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        self.contract_field(Contract)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contract_page()
        contract_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contract_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contract_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        my_id = wd.find_element_by_name('id').get_attribute('value')

        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        second_phone = wd.find_element_by_name('phone2').get_attribute('value')

        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')

        fax = wd.find_element_by_name('fax').get_attribute('value')

        return(Contact(first_name=first_name, last_name=last_name, id=my_id, home=home_phone,
                       work=work_phone,mobile=mobile_phone, phone=second_phone, email1 = email1, email2 = email2,
                       email3 = email3,  address=address, fax = fax))

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = ''
        mobile_phone = ''
        work_phone = ''
        second_phone = ''
        fax = ''
        if re.search('H: (.*)', text):
            home_phone = re.search('H: (.*)', text).group(1)
        if re.search('M: (.*)', text):
            mobile_phone = re.search('M: (.*)', text).group(1)
        if re.search('W: (.*)', text):
            work_phone = re.search('W: (.*)', text).group(1)
        if re.search('P: (.*)', text):
            second_phone = re.search('P: (.*)', text).group(1)
        if re.search('F: (.*)', text):
            fax = re.search('F: (.*)', text).group(1)


        return Contact(home=home_phone,work=work_phone,mobile=mobile_phone, phone=second_phone, fax = fax)


# all data old
'''
Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                      title=Profinity.correct_data, company_name=Profinity.correct_data,
                      address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                      fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                      mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                      email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                      add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                      notes=Profinity.correct_data)
'''