import selenium
from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapeData(driver, findByCSSNotLive, findByCSSLive, ifLive):
    try:
        # if ifLive throws a TimeoutException, the user is not live.
        ifLive = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ifLive)))
        followersLive = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, findByCSSLive)))
        print("Follower Count Found! User is live.")
        return followersLive.text
    except TimeoutException:
        followersNotLive = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, findByCSSNotLive)))
        print("Follower Count Found! User is not live.")
        return followersNotLive.text

def seperateData(literal):
    string = str.split(literal)
    value = string[0]
    # will not cast to an integer if you replace K or M with a space
    # value = int(value)

    if ('K' in value):
        print("Found you idiot.")

    return value









        

    