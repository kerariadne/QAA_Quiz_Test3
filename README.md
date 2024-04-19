# README: User Login Test Case with Incorrect Credentials

## Overview
This README document describes the automated test case designed to verify the behavior of the login functionality on [Automation Exercise](http://automationexercise.com) when incorrect credentials are used. It includes detailed steps to execute the test and verify that the appropriate error message is displayed.

## Tools and Technologies
- **Selenium WebDriver**: Automates browser actions to simulate user interactions.
- **Python**: The programming language used to script the test.
- **Pytest** or **unittest**: Python testing frameworks could be used to run this test script.

### Test Steps
1. **Launch the Browser**: Open a web browser session.
2. **Navigate to URL**: Type `http://automationexercise.com` into the browser's address bar.
3. **Verify Home Page Visibility**: Ensure that the website's home page loads successfully.
4. **Navigate to Login Page**: Click the 'Signup / Login' button to access the login page.
5. **Check Login Section Visibility**: Confirm that the 'Login to your account' section is visible.
6. **Enter Credentials**: Type the incorrect email and password into the login fields.
7. **Attempt to Login**: Click the 'login' button to submit the login form.
8. **Verify Error Message**: Check for and confirm the visibility of the error message "Your email or password is incorrect!".
