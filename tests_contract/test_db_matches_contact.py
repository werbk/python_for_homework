 # -- coding: utf-8 --
from tests_contract.contact_helper import Contact


def test_contact_list(app, db):
    ua_list = app.contact.get_contact_list_without_none()

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip(), home=contact.home.strip(),
                       mobile=contact.mobile.strip(), work=contact.work.strip(), phone=contact.phone.strip(), email1=contact.email1.strip(), email2=contact.email2.strip(),
                       email3=contact.email3.strip(), address=contact.address.strip())

    db_list = map(clean, db.get_contact_list_db())
    assert sorted(ua_list, key=Contact.if_or_max) == sorted(db_list, key=Contact.if_or_max)