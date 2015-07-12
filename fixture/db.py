import mysql.connector
from tests_group.group_helper import Group
from tests_contract.contact_helper import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), group_name=name, group_header=header, group_footer=footer))

        finally:
            cursor.close()
        return list


    def get_contact_list_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname, address, home, mobile, work, email, email2, email3, '
                           'phone2 from addressbook where deprecated = "0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work,
                 email, email2, email3, phone2) = row

                list.append(Contact(id = int(id), first_name=firstname, last_name=lastname,
                            home=home,
                            mobile=mobile, work=work, email1=email,
                            email2=email2, email3=email3,  phone=phone2, address=address))
        finally:
            cursor.close()
        return list

'''
def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, middlename, lastname, nickname, title, company, address, home, '
                           'mobile, work, fax, email, email2, email3, homepage, address2, phone2, notes '
                           'from addressbook where deprecated = "0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes) = row

                list.append(Contact(id = id, first_name=firstname, last_name=lastname,
                            middle_name=middlename, nickname=nickname,
                            title=title, company_name=company,
                            address_name=address, work=work,
                            fax=fax, home=home,
                            mobile=mobile, email1=email,
                            email2=email2, email3=email3, homepage=homepage, address=address2, phone=phone2,
                            notes=notes))
        finally:
            cursor.close()
        return list'''