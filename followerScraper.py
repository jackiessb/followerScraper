# A Twitch follower scraper
# Created by JackieSSB, Twitter is @JerryTheWhale

'''
NOTES: 
   Add loop for consecutive pings.
   Advanced error checking: 
       checking the validity of links through requests.
   Potential GUI?
   Publish to Github and advertise. PogU!
'''
import selenium
import scraper
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Asking the user what profile to scrape
username = input("Enter the Twitch channel you would like to scrape: ")

# Appends the username to the end of the URL
URLtext = 'https://www.twitch.tv/' + username

# Turns off annoying error messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:/Users/memjk/Documents/chromedriver.exe',options=options)

# Start WebDriver
driver.get(URLtext)
print("Current sesion is: {}".format(driver.session_id))

# Current CSS selector. Subject to change. Future Jackson may need to change this.
findByCSS = '#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area > div.simplebar-scroll-content > div > div > div > div.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline.channel-root__info--home > div > div.home-header-sticky.tw-mg-auto.tw-pd-t-2 > div.tw-align-items-center.tw-flex.tw-justify-content-between.tw-mg-b-2 > div.tw-align-items-start.tw-flex.tw-full-width > div.tw-align-self-center > p'

# Literal scraping action
literal = scraper.scrapeData(driver, findByCSS)

# Seperation of characters from string literal
scraper.seperateData(literal)
