from selenium.webdriver.common.by import By


class Locators:
    home = (By.CLASS_NAME, 'fa-home')
    signUp = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    loginText = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2')
    emailInput = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    password = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    loginButton = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button')
    errorText = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')
