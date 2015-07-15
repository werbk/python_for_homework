# -*- coding: utf-8 -*-
from random import randrange

import pytest

from fixture.variables import Profinity
from tests_group.group_helper import Group
from data.groups import test_data
from tests_group.validate import validate_group_list



#@pytest.mark.parametrize('group', test_data, ids=[repr(x) for x in test_data])

def test_create_group(app, db, json_groups):
    """Validation of correct create test group (All field fill up)"""
    group = json_groups
    old_groups = app.group.get_group_list()

    app.group.create(group)
    app.group.click_group_page()

    assert len(old_groups)+1 == app.group.count(), 'Group does not created'

    new_groups = app.group.get_group_list()
    old_groups.append(group)

    validate_group_list(db, new_groups, old_groups)
    app.group.delete_first_group()


def test_edit_group(app, db):
    """Validation of correct edit group (all field updated)"""

    app.group.validation_of_group_exist()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    group = Group(group_name=Profinity.long_word_20, group_header=Profinity.long_word_20,
                  group_footer=Profinity.long_word_20)
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)

    assert len(old_groups) == app.group.count(), 'Group list changed'

    new_groups = app.group.get_group_list()
    #app.group.delete_first_group()
    old_groups[index] = group

    validate_group_list(db, new_groups, old_groups)


def test_delete_group(app, db):
    """Validation of correct delete group"""

    app.group.validation_of_group_exist()
    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)

    assert len(old_groups)-1 == app.group.count(), 'Group does not created'
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups, 'Group list is different'

    validate_group_list(db, new_groups, old_groups)


