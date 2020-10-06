import pytest
    
def test_m4():
    assert False
    
def test_m5():
    assert 100 == 100

@pytest.mark.login   
def test_login():
    assert "admin" == "admin"