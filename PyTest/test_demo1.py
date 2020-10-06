"""
py.test --> test all files
py.test [foldername]/[filename.py] --> one file only
py.test [foldername]/ --> all files within a folder
py.test -k [testname] -v --> all the test start with the name
py.test [foldername]/[filename.py] -m [markname] --> execute only marked one at specific file
py.test -m [markname] --> executed all with same markname
"""


import pytest

@pytest.mark.login
def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"

def test_m2():
    name = "Tony"
    assert name.upper() == "TONY"

@pytest.mark.login    
def test_m3():
    assert True
    
def test_m4():
    assert False
    
@pytest.mark.login    
def test_m5():
    assert 100 == 100

def test_m6():
    assert "ninja" == "NINJA"

@pytest.mark.login
def test_login_FB():
    assert "admin" == "admin"
    
