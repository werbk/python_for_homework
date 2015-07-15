# -*- coding: utf-8 -*-
from random import randrange
import pytest


from fixture.variables import Profinity
from tests_contract.contact_helper import Contact
from data.contacts import constant as test_data
from tests_contract.validate import validate_contact_list



#@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_of_add_new_valid_contact(app, db, json_contacts):
    """
    Validation of add correct new contact with full data
    """
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list()

    app.contact.create(contact)

    assert len(old_contact_list)+1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    new_contact_list_without = app.contact.get_contact_list_special_case()

    old_contact_list.append(contact)
    # this validation does not work again
    validate_contact_list(new_contact_list_without, db, old_contact_list, new_contact_list)
    app.contact.delete_contact()

def test_of_delete_contract(app, db):
    """
    Validation of  delete contract
    """

    app.contact.validation_of_contact_exist()
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))

    app.contact.delete_contact_by_index(index)
    assert len(old_contact_list)-1 == app.contact.count()

    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index:index+1] = []

    new_contact_list_without = app.contact.get_contact_list_special_case()
    validate_contact_list(new_contact_list_without, db, old_contact_list, new_contact_list, validate_ui=True)
    #assert old_contact_list == new_contact_list


def test_of_edit_contract(app, db):
    """
    Validation of edit contract
    """

    app.contact.validation_of_contact_exist()
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(first_name=Profinity.long_word_20, last_name=Profinity.long_word_20,
                      middle_name=Profinity.long_word_20, nickname=Profinity.long_word_20)
    contact.id = old_contact_list[index].id
    app.contact.edit_contract_by_index(contact, index)

    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()

    old_contact_list[index] = contact
    new_contact_list_without = app.contact.get_contact_list_special_case()
    validate_contact_list(new_contact_list_without, db, old_contact_list, new_contact_list)
    app.contact.delete_contact()


