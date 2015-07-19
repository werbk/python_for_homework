from tests_contract.contact_helper import Contact
import random
from tests_contract.validate import get_group_list, select_contact_not_group, select_contact_in_group

def test_add_contact_in_group(app, orm):
    """Validation of add contact in group"""

    group_list = get_group_list(app, orm)
    group = random.choice(group_list)

    old_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)

    contact, old_contacts_not_in_group = select_contact_not_group(app, group, old_contacts_not_in_group, orm)

    app.contact.add_group_field(contact, group)

    old_contacts_in_group.append(contact)
    old_contacts_not_in_group.remove(contact)

    new_contacts_in_group = orm.get_contacts_in_group(group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)

    assert sorted(new_contacts_in_group, key=Contact.if_or_max) == \
           sorted(old_contacts_in_group, key=Contact.if_or_max)
    assert sorted(new_contacts_not_in_group, key=Contact.if_or_max) == \
           sorted(old_contacts_not_in_group, key=Contact.if_or_max)


def test_delete_contact_from_group(app, orm):
    """validation of delete contact from group"""

    group_list = get_group_list(app, orm)
    group = random.choice(group_list)

    old_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_not_in_group = orm.get_contacts_not_in_group(group)

    contact, old_contacts_in_group, old_contacts_not_in_group = \
        select_contact_in_group(app, group, old_contacts_in_group, old_contacts_not_in_group, orm)

    app.contact.delete_from_group_field(contact, group)

    old_contacts_in_group.remove(contact)
    old_contacts_not_in_group.append(contact)

    new_contacts_in_group = orm.get_contacts_in_group(group)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(group)

    assert sorted(new_contacts_in_group, key=Contact.if_or_max) == \
           sorted(old_contacts_in_group, key=Contact.if_or_max)
    assert sorted(new_contacts_not_in_group, key=Contact.if_or_max) == \
           sorted(old_contacts_not_in_group, key=Contact.if_or_max)