from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
Webdriver = webdriver.Chrome(r"C:\Users\Fazil\Automation Drivers\chromedriver.exe")
Webdriver.maximize_window()
Webdriver.get("https://www.keybr.com/#")
pyautogui.click(1245,340)
pyautogui.click(470,520)
while True:
    Input = Webdriver.find_element_by_xpath('//*[@id="root"]/section/div[3]').text.replace('␣', ' ')
    pyautogui.typewrite(Input,0.1)