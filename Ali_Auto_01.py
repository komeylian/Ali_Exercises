from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
import webbrowser
import time


webbrowser.open_new(
    'https://pharmacysamandaru.fda.gov.ir/login.aspx?ReturnUrl=%2fdrugstores%2fdrugs-list.aspx')
time.sleep(5)
# get user name
username = pyautogui.locateOnScreen(
    "C:/Ali_Exercises/user.png", confidence=.8)
Cusername = pyautogui.center(username)
pyautogui.moveTo(Cusername)
time.sleep(2)
pyautogui.click()
pyautogui.write("k7772")
time.sleep(2)


# get password
password = pyautogui.locateOnScreen(
    "C:/Ali_Exercises/pass.png", confidence=.8)
Cpassword = pyautogui.center(password)
pyautogui.moveTo(Cpassword)
time.sleep(2)
pyautogui.click()
pyautogui.write("k7772")
time.sleep(2)


# get enter
enter = pyautogui.locateOnScreen("C:/Ali_Exercises/enter.png", confidence=.8)
Center = pyautogui.center(enter)
pyautogui.moveTo(Center)
time.sleep(1)
pyautogui.click()
time.sleep(2)


# # Scroll down by 100 units
# pyautogui.scroll(100)
# pyautogui.hotkey('page_down')
# pyautogui.scroll(200, x=100, y=200)


# # Scroll down using PAGE_DOWN key
# pyautogui.hotkey('page_down')


# Scroll down using keyboard inputs
#pyautogui.press('pagedown')
pyautogui.scroll(-100)



# # get size
# lowersize = pyautogui.locateOnScreen(
#     "C:/Ali_Exercises/lowersize.png", confidence=.8)
# Clowersize = pyautogui.center(lowersize)
# pyautogui.moveTo(Clowersize)
# time.sleep(1)
# pyautogui.click()
# time.sleep(3)
# pyautogui.click()
# time.sleep(3)
# pyautogui.click()
# time.sleep(3)
# pyautogui.click()
# time.sleep(3)
# '''''
# get lowerbutton
# lowerbutton = pyautogui.locateOnScreen(
#     "C:/Ali_Exercises/lowerbutton.png", confidence=.8)
# Clowerbutton = pyautogui.center(lowerbutton)
# pyautogui.moveTo(Clowerbutton)
# time.sleep(1)
# pyautogui.click()
# time.sleep(3)
# pyautogui.click()
# time.sleep(3)
# pyautogui.click()
# time.sleep(3)
# '''


# # Scroll down by 100 units
# pyautogui.scroll(100)


# # Launch the web browser (e.g., Chrome)
# driver = webdriver.Chrome()

# # Open a web page
# driver.get('https://example.com')

# # Scroll down using the body element
# body = driver.find_element_by_tag_name('body')
# body.send_keys(Keys.PAGE_DOWN)
