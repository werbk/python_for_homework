
from fixture.TestBase import clear
from tests_contract.contact_helper import Contact
from tests_contract.contact_lib import cleann


def test_phones_on_home_page(app, db):
    """
    Validation data on edit page == home page
    """
    app.contact.validation_of_contact_exist()

    contact_from_hp = app.contact.get_contact_list_without_none()
    contact_from_ep = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_hp[0].home == clear(contact_from_ep.home)
    assert contact_from_hp[0].mobile == clear(contact_from_ep.mobile)
    assert contact_from_hp[0].work == clear(contact_from_ep.work)
    assert contact_from_hp[0].phone == clear(contact_from_ep.phone)

    assert contact_from_hp[0].email1 == clear(contact_from_ep.email1)
    assert contact_from_hp[0].email2 == clear(contact_from_ep.email2)
    assert contact_from_hp[0].email3 == clear(contact_from_ep.email3)
    assert contact_from_hp[0].address == clear(contact_from_ep.address)


def test_phones_on_contact_view_page(app):
    """
    Validation data on edit page == view page
    """
    app.contact.validation_of_contact_exist()

    contact_from_vp = app.contact.get_contact_info_from_view_page(0)
    contact_from_ep = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_vp.home == contact_from_ep.home
    assert contact_from_vp.mobile == contact_from_ep.mobile
    assert contact_from_vp.work == contact_from_ep.work
    assert contact_from_vp.phone == contact_from_ep.phone
    assert contact_from_vp.fax == contact_from_ep.fax


def test_check_data_on_home_page(app, db):
    """Validation of all data on home page"""

    home_page_contacts = app.contact.get_contact_list_without_none()
    assert sorted(list(map(cleann, home_page_contacts)), key=Contact.if_or_max) == sorted(list(map(cleann, db.get_contact_list())), key=Contact.if_or_max)


# or i should do something like that?
def _test_check_data_on_view_page(app, db):
    """Validation of all data on view page"""

    a = sorted(list(map(cleann, db.get_contact_list())), key=Contact.if_or_max)

    for i in xrange(app.contact.count()):
        contact_from_hp = map(cleann, app.contact.get_contact_info_from_view_page(i))

        assert contact_from_hp[i].home == clear(a.home)
        assert contact_from_hp[i].mobile == clear(a.mobile)
        assert contact_from_hp[i].work == clear(a.work)
        assert contact_from_hp[i].phone == clear(a.phone)

        assert contact_from_hp[i].email1 == clear(a.email1)
        assert contact_from_hp[i].email2 == clear(a.email2)
        assert contact_from_hp[i].email3 == clear(a.email3)
        assert contact_from_hp[i].address == clear(a.address)

