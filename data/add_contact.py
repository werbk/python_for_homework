
import pytest

from fixture.TestBase import random_string
from tests_contract.contact_helper import Contact
from fixture.variables import Profinity

constant = [Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                      title=Profinity.correct_data, company_name=Profinity.correct_data,
                      address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                      fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                      mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                      email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                      add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                      notes=Profinity.correct_data),
            Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                      title=Profinity.correct_data, company_name=Profinity.correct_data,
                      address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                      fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                      mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                      email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                      add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                      notes=Profinity.correct_data)


    ]

test_data = [
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, nickname=nickname, title=title,
            company_name=company_name, address_name=address_name, home=home, mobile=mobile, work=work, fax=fax,
            email1=email1, email2=email2, email3=email3, homepage=homepage, address=address, phone=phone, notes=notes,
            id=id, contact_name=contact_name)

    for first_name in ['', random_string('first_name', 10)]
    for middle_name in ['', random_string('middle_name', 20)]
    for last_name in ['', random_string('last_name', 20)]
    for nickname in [random_string('nickname', 10)]
    for title in [random_string('title', 20)]
    for company_name in [random_string('company_name', 20)]
    for address_name in [random_string('address_name', 10)]
    for home in [random_string('home', 20)]
    for mobile in [random_string('mobile', 20)]
    for work in [random_string('work', 10)]
    for fax in [random_string('fax', 20)]
    for email1 in [random_string('email1', 20)]
    for email2 in [random_string('email2', 10)]
    for email3 in [random_string('email3', 20)]
    for homepage in [random_string('homepage', 20)]
    for address in [random_string('address', 10)]
    for phone in [random_string('phone', 20)]
    for notes in [random_string('notes', 20)]
    for contact_name in [random_string('contact_name', 20)]
            ]
