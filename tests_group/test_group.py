# -*- coding: utf-8 -*-
import random

from fixture.variables import Profinity
from tests_group.group_helper import Group
from tests_group.validate import validate_group_list




#@pytest.mark.parametrize('group', test_data, ids=[repr(x) for x in test_data])

def test_create_group(app, db, check_ui, json_groups):
    """Validation of correct create test group (All field fill up)"""
    group = json_groups
    old_groups = db.get_group_list()

    app.group.create(group)
    app.group.click_group_page()

    #assert len(old_groups)+1 == app.group.count(), 'Group does not created'

    new_groups = db.get_group_list()
    old_groups.append(group)

    validate_group_list(app, new_groups, old_groups, check_ui)
    app.group.delete_first_group()


def test_edit_group(app, db, check_ui):
    """Validation of correct edit group (all field updated)"""

    app.group.validation_of_group_exist()
    old_groups = db.get_group_list()


    group = random.choice(old_groups)
    group_id = group.id

    group = Group(group_name=Profinity.long_word_20, group_header=Profinity.long_word_20,
                  group_footer=Profinity.long_word_20)
    group.id=group_id

    app.group.edit_group_by_id(group, group_id)

    new_groups = db.get_group_list()
    #app.group.delete_first_group()
    old_groups.remove(group)
    old_groups.append(group)
    validate_group_list(app, new_groups, old_groups, check_ui)


def test_delete_group(app, db, check_ui):
    """Validation of correct delete group"""

    app.group.validation_of_group_exist()
    old_groups = db.get_group_list()

    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)

    new_groups = db.get_group_list()

    old_groups.remove(group)
    assert old_groups == new_groups, 'Group list is different'

    validate_group_list(app, new_groups, old_groups, check_ui)





