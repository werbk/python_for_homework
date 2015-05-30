# -*- coding: utf-8 -*-
from group_lib import Group
from tests_contract.contract_lib import connection


@connection
def test_create_group(app):
    """Validation of correct create test group (All field fill up)"""
    app.create_group(Group(group_name='test', group_header='test', group_footer='test'))
    app.click_group_page()
    app.delete_first_group()


@connection
def test_create_group_name(app):
    """Validation of correct create test group (Only group name fill up)"""

    app.create_group(Group(group_name='test'))
    app.click_group_page()

    # This code i use at all test, where i should put it do use it?
    app.delete_first_group()



