from selenium import webdriver
import pytest

def test_secondtest() -> object:
    path = 'C:/Users/madhuk4/PycharmProjects/FirstProject/Driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://thetestingworld.com/testing')
    print('hello')
    driver.quit()
