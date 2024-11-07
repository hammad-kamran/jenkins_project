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
    driver.get('https://stage.alnafi.com/auth/sign-in')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
    ('abdeali@gmail.com', 'abdeali@123'),
    ('ali@gmail.com', 'ali@123'),
    ('abd@gmail.com', 'abd@123')
    ]
    
@pytest.mark.parametrize("email,password",my_cred())
def test_login(email,password):
    print("My pytest login")
    driver.find_element(By.ID,'Email').send_keys(email)
    time.sleep(10)
    driver.find_element(By.ID, 'Password').send_keys(password)
    time.sleep(10)
