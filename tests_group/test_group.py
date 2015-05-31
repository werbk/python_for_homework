# -*- coding: utf-8 -*-
from group_lib import Group
from fixture.variables import Profinity


def test_create_group(app):
    """Validation of correct create test group (All field fill up)"""

    app.group.create(Group(group_name=Profinity.correct_data, group_header=Profinity.correct_data,
                           group_footer=Profinity.correct_data))
    app.group.click_group_page()
    app.group.delete_first_group()


def test_create_group_name(app):
    """Validation of correct create test group (Only group name fill up)"""

    app.group.create(Group(group_name='test'))
    app.group.click_group_page()
    app.group.delete_first_group()


def test_edit_group(app):
    """Validation of correct edit group (all field updated)"""

    app.group.validation_of_group_exist()
    app.group.edit_group(Group(group_name=Profinity.long_word_20, group_header=Profinity.long_word_20,
                               group_footer=Profinity.long_word_20))
    app.group.delete_first_group()


def test_delete_group(app):
    """Validation of correct delete group"""
    app.group.validation_of_group_exist()
    app.group.delete_first_group()

