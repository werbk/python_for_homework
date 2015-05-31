# -*- coding: utf-8 -*-
from fixture.variables import Profinity
from contract_lib import Contract, connection


@connection
def test_of_add_new_valid_contact(app):
    """
    Validation of add correct new contact with full data
    """

    app.contact.create(Contract(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                        middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                        title=Profinity.correct_data, company_name=Profinity.correct_data,
                        address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                        fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                        mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                        email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                        add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                        notes=Profinity.correct_data))


@connection
def test_of_add_new_valid_contact_name_only(app):
    """
    Validation of add correct new contact with only full name
    """

    app.contact.create((Contract(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                        middle_name=Profinity.correct_data, nickname=Profinity.correct_data)))

