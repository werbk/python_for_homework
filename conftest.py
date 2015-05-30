import pytest

from tests_group.group_lib import Group, GroupBase
from fixture.TestBase import BaseClass


@pytest.fixture(scope='session')
def app(request):
    fixture = GroupBase()
    request.addfinalizer(fixture.restore_group)
    return fixture

