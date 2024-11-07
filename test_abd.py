import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import  time

# Use Service for ChromeDriver
from selenium.webdriver.chrome.service import Service

def setup_function():
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get('https://www.saucedemo.com/v1/')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
    ('standard_user', 'secret_sauce'),
    ('locked_out_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce')
    ]
    
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.ID,'user-name').send_keys(username)
    time.sleep(10)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(10)
