import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapeData(driver, findByCSS):
    try:
        followers = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, findByCSS)))
    except:
        print("ERROR: Cannot get follower count. Check how you entered your username.")
    finally:
        print("Follower Count Found!")
        # driver.close()
        return followers.text

def seperateData(literal):
    # filler
    return 1









        

    