import pytest
import logging

from fixture.TestBase import BaseClass
from fixture.variables import UserLogin


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--baseUrl')
    loginu = request.config.getoption('--loginu')
    loginp = request.config.getoption('--loginp')
    if fixture is None:
        fixture = BaseClass(browser=browser, base_url = url)

    else:
        if not fixture.is_valid():
            fixture = BaseClass(browser=browser, base_url = url)

    fixture.session.ensure_login(user_name=loginu, password=loginp)
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):

    def fin():
        fixture.session.ensure_logout()
        fixture.restore()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    default_login_user = [UserLogin.name, UserLogin.password]
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')

    # i believe that it possible do in 1 line but i don't know how to in 1 Login take to parameter at same time
    parser.addoption('--loginu', action='store', default=default_login_user[0])
    parser.addoption('--loginp', action='store', default=default_login_user[1])