
from fixture.TestBase import random_string
from tests_contract.contact_helper import Contact
import os.path
import json
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:

    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contact.json'

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = str(a)

test_data = [
    Contact(first_name='', middle_name='', last_name='', nickname='', title='',
            company_name='', address_name='', home='', mobile='', work='', fax='',
            email1='', email2='', email3='', homepage='', address='', phone='', notes='',
            id='', contact_name='')]+[Contact(first_name=random_string('first_name', 10),
                                              middle_name=random_string('middle_name', 20),
                                              last_name=random_string('last_name', 20),
                                              nickname=random_string('nickname', 10),
                                              title=random_string('title', 20),
                                              company_name=random_string('company_name', 20),
                                              address_name=random_string('address_name', 10),
                                              home=random_string('home', 20),
                                              mobile=random_string('mobile', 20),
                                              work=random_string('work', 10),
                                              fax=random_string('fax', 20),
                                              email1=random_string('email1', 20),
                                              email2=random_string('email2', 10),
                                              email3=random_string('email3', 20),
                                              homepage=random_string('homepage', 20),
                                              address=random_string('address', 10),
                                              phone=random_string('phone', 20),
                                              notes=random_string('notes', 20),
                                              contact_name=random_string('contact_name', 20)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))