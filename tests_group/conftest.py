import pytest

from group_lib import Group, GroupBase


@pytest.fixture(scope='session')
def app(request):
    fixture = GroupBase()
    request.addfinalizer(fixture.restore_group)
    return fixture


# i try to make docstring output but for now i don't know how dial with it
'''
@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    # execute all other hooks to obtain the report object
    rep = __multicall__.execute()
    if rep.when == "call":
        extra = item._obj.__doc__.strip()
        rep.nodeid =  extra
    return rep'''
