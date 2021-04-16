from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

Duration = 0
Driver_Path = r"C:\Users\{}\Automation Drivers\chromedriver.exe"
Playlist_URL = r'https://www.youtube.com/playlist?list=PL-osiE80TeTvviVL0pJGX5mZCo7CAvIuf'

options = webdriver.ChromeOptions()
options.add_argument('headless')
WebDriver = webdriver.Chrome(Driver_Path, options = options)
WebDriver.maximize_window()
WebDriver.get(Playlist_URL)
time.sleep(1)
WebDriver.find_element_by_tag_name('html').send_keys(Keys.END)
time.sleep(3)
Container = WebDriver.find_element_by_xpath(r'//*[@id="contents"]')

def hms_to_s(s):
    t = 0 
    for u in s.split(':'): 
        t = 60 * t + int(u)
    return t

for word in Container.text.split():
    if len(word)>4 and ':' in word:
        print(word)
        Duration = Duration + hms_to_s(word)/60
print(int(Duration),'minutes')
