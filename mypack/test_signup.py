import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")

    yield
    print("Once after every method")

def test_signUpByEmail(setup):
    print("this is signUp by email")

def test_signUpByfacebook(setup):
    print("this is signUp by facebook")