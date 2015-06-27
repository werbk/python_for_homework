import pytest
import logging
import json
import os.path

from fixture.TestBase import BaseClass
from fixture.variables import UserLogin


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption('--browser')

    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file) as file:
            target = json.load(file)


    #url = request.config.getoption('--baseUrl')
    #login_user = request.config.getoption('--login_user')
    #login_password = request.config.getoption('--login_password')

    if fixture is None or not fixture.is_valid():
        fixture = BaseClass(browser=browser, base_url=target['baseUrl'])

    fixture.session.ensure_login(user_name=target['username'], password=target['password'])
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
    parser.addoption('--target', action='store', default='target.json') #'http://localhost/addressbook/')

    # i believe that it possible do in 1 line but i don't know how two in 1 Login take to parameter at same time
    #parser.addoption('--loginu', action='store', default=default_login_user[0])
    #parser.addoption('--loginp', action='store', default=default_login_user[1])