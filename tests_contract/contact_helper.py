from sys import maxsize


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