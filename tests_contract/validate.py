 # -- coding: utf-8 --
from tests_contract.contact_helper import Contact


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
