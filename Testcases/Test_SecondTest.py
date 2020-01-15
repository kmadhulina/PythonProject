from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def test_secondtest() -> object:
    path = '/Driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://thetestingworld.com/testing')
    print('hello')
    driver.quit()
