# -*- coding: utf-8 -*-
from random import randrange

import pytest

from fixture.TestBase import random_string
from fixture.variables import Profinity
from tests_group.group_helper import Group


test_data = [
    Group(group_name=name, group_header=header, group_footer=footer)
    for name in ['', random_string('name', 10)]
    for header in ['', random_string('header', 20)]
    for footer in ['', random_string('footer', 20)]
            ]



@pytest.mark.parametrize('group', test_data, ids=[repr(x) for x in test_data])
def test_create_group(app, group):
    """Validation of correct create test group (All field fill up)"""

    old_groups = app.group.get_group_list()

    app.group.create(group)
    app.group.click_group_page()

    assert len(old_groups)+1 == app.group.count(), 'Group does not created'

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    app.group.delete_first_group()
    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max), 'Group list is different'


def test_edit_group(app):
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
    app.group.delete_first_group()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max), 'Group list is different'


def test_delete_group(app):
    """Validation of correct delete group"""

    app.group.validation_of_group_exist()
    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)

    assert len(old_groups)-1 == app.group.count(), 'Group does not created'
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups, 'Group list is different'
