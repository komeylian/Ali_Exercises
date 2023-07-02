from persian_converter import fprint
import pyautogui
import webbrowser
import time


def first():
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
    time.sleep(3)

    # get password
    password = pyautogui.locateOnScreen(
        "C:/Ali_Exercises/pass.png", confidence=.8)
    Cpassword = pyautogui.center(password)
    pyautogui.moveTo(Cpassword)
    time.sleep(2)
    pyautogui.click()
    pyautogui.write("k7772")
    time.sleep(3)

    # get enter
    enter = pyautogui.locateOnScreen(
        "C:/Ali_Exercises/enter.png", confidence=.8)
    Center = pyautogui.center(enter)
    pyautogui.moveTo(Center)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

    # get size
    lowersize = pyautogui.locateOnScreen(
        "C:/Ali_Exercises/lowersize.png", confidence=.8)
    Clowersize = pyautogui.center(lowersize)
    pyautogui.moveTo(Clowersize)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)


def second():
    noghat = ['1.png', 'test.png', 'ali.png', 'test5.png',
              '', '', '', '', '', '', '', '', '', '', ]

    for nogteha in range(len(noghat)):
        # get enter
        path = f'C:/Ali_Exercises/{noghat[nogteha]}"'
        print(path)

        enter = pyautogui.locateOnScreen(path, confidence=.8)
        Center = pyautogui.center(enter)
        pyautogui.moveTo(Center)
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)


print(second())
