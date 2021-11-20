import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")

    yield
    print("Once after every method")

def test_loginByEmail(setup):
    print("this is login by email")

def test_loginByfacebook(setup):
    print("this is login by facebook")