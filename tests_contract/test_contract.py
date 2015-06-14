# -*- coding: utf-8 -*-
from fixture.variables import Profinity
from contract_lib import Contact
import logging
from random import randrange


def test_of_add_new_valid_contact(app):
    """
    Validation of add correct new contact with full data
    """
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                      title=Profinity.correct_data, company_name=Profinity.correct_data,
                      address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                      fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                      mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                      email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                      add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                      notes=Profinity.correct_data)
    app.contact.create(contact)

    assert len(old_contact_list)+1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    app.contact.delete_contact()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.if_or_max) == sorted(new_contact_list, key=Contact.if_or_max)


def test_of_add_new_valid_contact_name_only(app):
    """
    Validation of add correct new contact with only full name
    """
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                      middle_name=Profinity.correct_data, nickname=Profinity.correct_data)
    app.contact.create(contact)

    assert len(old_contact_list)+1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()

    app.contact.delete_contact()

    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.if_or_max) == sorted(new_contact_list, key=Contact.if_or_max)


def test_of_delete_contract(app):
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
    assert old_contact_list == new_contact_list


def test_of_edit_contract(app):
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
    app.contact.delete_contact()

    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.if_or_max) == sorted(new_contact_list, key=Contact.if_or_max)