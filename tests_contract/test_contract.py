# -*- coding: utf-8 -*-
import random
import pytest
import time

from fixture.variables import Profinity
from tests_contract.contact_helper import Contact
from data.contacts import constant as test_data
from tests_contract.validate import validate_contact_list



#@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_of_add_new_valid_contact(app, db, check_ui, json_contacts ):
    """
    Validation of add correct new contact with full data
    """
    contact = json_contacts
    old_contact_list = db.get_contact_list()

    app.contact.create(contact)

    assert len(old_contact_list)+1 == app.contact.count()
    new_contact_list = db.get_contact_list()
    #new_contact_list_without = app.contact.get_contact_list_special_case()

    old_contact_list.append(contact)
    # this validation does not work again
    validate_contact_list(app, old_contact_list, new_contact_list, check_ui)
    app.contact.delete_contact()

def test_of_delete_contract(app, db, check_ui):
    """
    Validation of  delete contract
    """

    app.contact.validation_of_contact_exist()
    old_contact_list = db.get_contact_list()


    contact = random.choice(old_contact_list)

    app.contact.delete_contact_by_id(contact.id)

    # without sleep does not work. What i should do?
    time.sleep(15)

    new_contact_list = db.get_contact_list()

    old_contact_list.remove(contact)

    validate_contact_list(app, old_contact_list, new_contact_list, check_ui)


def test_of_edit_contract(app, db, check_ui):
    """
    Validation of edit contract
    """

    app.contact.validation_of_contact_exist()
    old_contact_list = db.get_contact_list()

    contact = random.choice(old_contact_list)
    old_contact_list.remove(contact)
    contact_id = contact.id

    contact = Contact(first_name=Profinity.long_word_20, last_name=Profinity.long_word_20,
                      middle_name=Profinity.long_word_20, nickname=Profinity.long_word_20)

    contact.id = contact_id
    app.contact.edit_contact_by_id(contact, contact_id)

    new_contact_list = db.get_contact_list()

    old_contact_list.append(contact)

    validate_contact_list(app, old_contact_list, new_contact_list, check_ui)
    app.contact.delete_contact()


