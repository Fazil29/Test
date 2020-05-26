from selenium import webdriver
import time
import datetime

Duration = 0
Driver_Path = r"C:\Users\Fazil\Automation Drivers\chromedriver.exe"
Playlist_URL = r'https://www.youtube.com/playlist?list=PLF_7kfnwLFCF_VxKKAhHSLryCsJr3GW71'

options = webdriver.ChromeOptions()
options.add_argument('headless')
WebDriver = webdriver.Chrome(Driver_Path, options = options)

WebDriver.get(Playlist_URL)
time.sleep(2)
Container = WebDriver.find_element_by_xpath(r'//*[@id="contents"]')

def hms_to_s(s):
    t = 0 
    for u in s.split(':'): 
        t = 60 * t + int(u)
    return t

for word in Container.text.split():
    if len(word)>1 and ':' in word:
        Duration = Duration + hms_to_s(word)/60
print(int(Duration),'minutes')