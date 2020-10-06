"""
[[pip install pytest-dist]]
py.test [foldername]/[filename.py] -n 5 --> runs the tests by using multiple workers 5
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    # PATH = "/Users/daheekim/Desktop/VisualStudio/TDD/PyTest/chromedriver"
    # driver = webdriver.Chrome(PATH)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    assert driver.title == "Google"
    driver.quit()
    
def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()
def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook - Log In or Sign Up"
    driver.quit()
def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()