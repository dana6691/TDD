import pytest

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"

def test_m2():
    name = "Tony"
    assert name.upper() == "TONY"

@pytest.mark.login  
def test_login_Uber():
    assert "admin" == "admin"