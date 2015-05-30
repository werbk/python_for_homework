# -*- coding: utf-8 -*-
from fixture.variables import UserLogin, Profinity
from contract_lib import Contract

def test_of_add_new_valid_contact(app):
    """
    Validation of add correct new contact with full data
    """

    app.session.login(UserLogin.name, UserLogin.password)

    app.add_contract()
    app.add_full_name(Contract(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data))

    app.add_title(Contract(title=Profinity.correct_data))
    app.add_company(Contract(company_name=Profinity.correct_data))
    app.add_address(Contract(address_name=Profinity.correct_data))

    app.add_phone_number(Contract(work=Profinity.correct_phone_number, fax=Profinity.correct_phone_number,
                         home=Profinity.correct_phone_number, mobile=Profinity.correct_phone_number))

    app.add_email(Contract(email1=Profinity.correct_email, email2=Profinity.correct_email,
                  email3=Profinity.correct_email))

    app.add_homepage(Contract(homepage=Profinity.correct_data))
    app.add_year()

    # secondary data
    app.add_secondary_adress(Contract(address=Profinity.correct_data))
    app.add_secondary_home(Contract(phone=Profinity.correct_data))
    app.add_secondary_notes(Contract(notes=Profinity.correct_data))

    app.submit_contact()
    app.session.logout()



def test_of_add_new_valid_contact_name_only(app):
    """
    Validation of add correct new contact with only full name
    """

    app.session.login(UserLogin.name, UserLogin.password)

    app.add_contract()
    app.add_full_name(Contract(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data))

    app.submit_contact()
    app.session.logout()
