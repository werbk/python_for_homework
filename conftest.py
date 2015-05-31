import pytest

from fixture.TestBase import BaseClass


@pytest.fixture(scope='session')
def app(request):
    fixture = BaseClass()
    request.addfinalizer(fixture.restore)
    return fixture


