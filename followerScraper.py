# A Twitch follower scraper
# Created by JackieSSB, Twitter is @JerryTheWhale

'''
NOTES: 
   Add loop for consecutive pings.
   Add functionality if user is live. (Can we detect this?)
   Advanced error checking: 
       checking the validity of links through requests.
   Potential GUI?
   Publish to Github and advertise. PogU!
'''
import selenium
import scraper
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
findByCSSNotLive = '#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area > div.simplebar-scroll-content > div > div > div > div.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline.channel-root__info--home > div > div.home-header-sticky.tw-mg-auto.tw-pd-t-2 > div.tw-align-items-center.tw-flex.tw-justify-content-between.tw-mg-b-2 > div.tw-align-items-start.tw-flex.tw-full-width > div.tw-align-self-center > p'
findByCSSLive = '#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch-chat.channel-root--live.channel-root--watch.channel-root--unanimated > div.channel-root__main--with-chat.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--with-chat > div > div:nth-child(2) > div > div.tw-mg-t-2.tw-mg-x-2 > div:nth-child(1) > div > div.tw-flex.tw-justify-content-center > div > div > div.tw-pd-1 > div.tw-align-center'
ifLive = '#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch-chat.channel-root--live.channel-root--watch.channel-root--unanimated > div.channel-root__main--with-chat.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--with-chat > div > div.tw-flex-grow-0.tw-flex-shrink-1 > div > div > div > div.tw-mg-t-1.tw-pd-l-1 > div > div > a > div.ScHaloIndicator-sc-1l14b0i-1.jYqVGu.tw-halo__indicator > div > div > div > div > p'

# Literal scraping action
literal = scraper.scrapeData(driver, findByCSSNotLive, findByCSSLive, ifLive)

# Seperation of characters from string literal
actualCount = scraper.seperateData(literal)

# print(actualCount)
