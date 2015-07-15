
from fixture.TestBase import clear

def test_phones_on_home_page(app):
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