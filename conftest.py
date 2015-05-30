import pytest

from tests_group.group_lib import GroupBase


@pytest.fixture(scope='session')
def app(request):
    fixture = GroupBase()
    request.addfinalizer(fixture.restore_group)
    return fixture


