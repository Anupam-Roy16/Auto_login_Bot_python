
from selenium import webdriver
import os
from time import sleep

# Get the path of chromedriver which you have install

def startBot(username, password, url):
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(r"C:\Users\anupa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

    # opening the website in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name(
        "handleOrEmail").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name(
        "password").send_keys(password)

    # click on submit
    driver.find_element_by_css_selector(
        "input[type=\"submit\" i]").click()

    print("logged in successfully")
    sleep(1)
    driver.get("https://codeforces.com/")
    sleep(100)
# Driver Code
# Enter below your login credentials
username = "AnupamRoy"
password = "radhakrishna752"

# URL of the login page of site
# which you want to automate login.
url = "https://codeforces.com//enter?back=%2F"

# Call the function
startBot(username, password, url)
