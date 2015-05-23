# -*- coding: utf-8 -*-
import pytest

from TestBase import Profinity
from TestBase import UserLogin
from contract_lib import ContractBase


@pytest.fixture
def app(request):
    fixture = ContractBase()
    request.addfinalizer(fixture.restore_contract)
    return fixture


def test_of_add_new_valid_contact(app):
    """
    Validation of add correct new contact with full data
    """

    app.open_home_page()
    app.login(UserLogin.name, UserLogin.password)

    app.add_contract()
    app.add_full_name(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data)

    app.add_title(title=Profinity.correct_data)
    app.add_company(company_name=Profinity.correct_data)
    app.add_address(address_name=Profinity.correct_data)

    app.add_phone_number(work=Profinity.correct_phone_number, fax=Profinity.correct_phone_number,
                         home=Profinity.correct_phone_number, mobile=Profinity.correct_phone_number)

    app.add_email(email1=Profinity.correct_email, email2=Profinity.correct_email,
                  email3=Profinity.correct_email)

    app.add_homepage(homepage=Profinity.correct_data)
    app.add_year()

    # secondary data
    app.add_secondary_adress(address=Profinity.correct_data)
    app.add_secondary_home(phone=Profinity.correct_data)
    app.add_secondary_notes(notes=Profinity.correct_data)

    app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()