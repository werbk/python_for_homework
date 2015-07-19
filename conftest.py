import pytest
import logging
import json
import jsonpickle
import os.path
import importlib

from fixture.orm import ORMFixture
from fixture.db import DbFixture
from fixture.TestBase import BaseClass
from fixture.variables import UserLogin


fixture = None
target = None



def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target

@pytest.fixture
def app(request):
    global fixture


    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']



    #url = request.config.getoption('--baseUrl')
    #login_user = request.config.getoption('--login_user')
    #login_password = request.config.getoption('--login_password')

    if fixture is None or not fixture.is_valid():
        fixture = BaseClass(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(user_name=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):

    def fin():
        fixture.session.ensure_logout()
        fixture.restore()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')

@pytest.fixture(scope="session")
def orm(request):
    orm_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'],
                          password=orm_config['password'])
    def fin():
        ormfixture.destroy()
    request.addfinalizer(fin)
    return ormfixture


def pytest_addoption(parser):
    default_login_user = [UserLogin.name, UserLogin.password]
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json') #'http://localhost/addressbook/')
    parser.addoption('--check_ui', action='store_true')

    # i believe that it possible do in 1 line but i don't know how two in 1 Login take to parameter at same time
    #parser.addoption('--loginu', action='store', default=default_login_user[0])
    #parser.addoption('--loginp', action='store', default=default_login_user[1])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture