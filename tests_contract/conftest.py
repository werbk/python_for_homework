import pytest

from contract_lib import ContractBase


@pytest.fixture(scope='session')
def app(request):
    fixture = ContractBase()
    request.addfinalizer(fixture.restore_contract)
    return fixture