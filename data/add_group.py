


from fixture.TestBase import random_string

from tests_group.group_helper import Group


constant = [
    Group(group_name='name1', group_header='header1', group_footer='footer1'),
    Group(group_name='name1', group_header='header1', group_footer='footer1')
]

test_data = [
    Group(group_name=name, group_header=header, group_footer=footer)
    for name in ['', random_string('name', 10)]
    for header in ['', random_string('header', 20)]
    for footer in ['', random_string('footer', 20)]]