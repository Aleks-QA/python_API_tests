import pytest


@pytest.fixture
def setup():
    print('\n__Start test__')
    yield
    print('__Finish test__')

