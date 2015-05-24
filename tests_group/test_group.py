# -*- coding: utf-8 -*-

from fixture.variables import UserLogin
from group_lib import Group


def test_create_group(app):
    """Validation of correct create test group (All field fill up)"""
    app.session.login(UserLogin.name, UserLogin.password)
    app.create_group(Group(group_name='test', group_header='test', group_footer='test'))
    app.click_group_page()
    app.delete_first_group()
    app.wd.find_element_by_link_text("Logout").click()


def test_create_group_name(app):
    """Validation of correct create test group (Only group name fill up)"""

    app.session.login(UserLogin.name, UserLogin.password)
    app.create_group(Group(group_name='test', group_header='', group_footer=''))
    app.click_group_page()

    # This code i use at all test, where i should put it do use it?
    app.delete_first_group()
    app.wd.find_element_by_link_text("Logout").click()


