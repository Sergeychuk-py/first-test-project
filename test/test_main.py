import pytest


@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\n After test')


def test_main(before_after):
    assert 1 == 1


def test_main_1():
    assert 2 == 2
