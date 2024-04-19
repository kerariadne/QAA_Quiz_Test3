from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def driver_init():
    driver.get('https://www.automationexercise.com/')
    driver.maximize_window()


def check_home():
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Locators.home))
    driver.find_element(*Locators.signUp).click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Locators.loginText))


def enter_info(email, password):
    driver.find_element(*Locators.emailInput).send_keys(email)
    driver.find_element(*Locators.password).send_keys(password)
    driver.find_element(*Locators.loginButton).click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Locators.errorText))
    driver.quit()