 # -- coding: utf-8 --
import random

from tests_contract.contact_helper import Contact
from tests_group.group_helper import Group


def validate_contact_list(app, old_contact_list, new_contact_list, check_ui):
    #ua_list = new_contact_list_without
    #app.contact.get_contact_list_without_none()

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip(), home=contact.home.strip(),
                       mobile=contact.mobile.strip(), work=contact.work.strip(), phone=contact.phone.strip(), email1=contact.email1.strip(), email2=contact.email2.strip(),
                       email3=contact.email3.strip(), address=contact.address.strip())


    assert sorted(old_contact_list, key=Contact.if_or_max) == sorted(new_contact_list, key=Contact.if_or_max)

    if check_ui:
        db_list = map(clean, new_contact_list)
        assert sorted(app.contact.get_contact_list(), key=Contact.if_or_max) == sorted(db_list, key=Contact.if_or_max)


def get_group_list(app, orm):
     group_list = orm.get_group_list()
     if group_list == list():
         app.group.create(Group(group_name="TEST"))
         group_list = orm.get_group_list()
     return group_list


def select_contact_not_group(app, group, old_contacts_not_in_group, orm):
     if old_contacts_not_in_group == list():
         app.contact.create(Contact(first_name="TEST"))
         old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
         contact = old_contacts_not_in_group
     else:
         contact = random.choice(old_contacts_not_in_group)
     return contact, old_contacts_not_in_group


def select_contact_in_group(app, group, old_contacts_in_group, old_contacts_not_in_group, orm):
     if old_contacts_in_group == list():
         contact, old_contacts_not_in_group = select_contact_not_group(app, group, old_contacts_not_in_group, orm)
         app.contact.add_group_field(contact, group)
         old_contacts_in_group = orm.get_contacts_in_group(group)
         old_contacts_not_in_group = orm.get_contacts_not_in_group(group)
     else:
        contact = random.choice(old_contacts_in_group)
     return contact, old_contacts_in_group, old_contacts_not_in_group