import pyautogui

x= input("What are you looking for? ")
input("Press Enter")

pyautogui.FAILSAFE = True
pyautogui.moveTo(0,1000)
pyautogui.click()
pyautogui.PAUSE = 2.0
pyautogui.typewrite("Amazon")
pyautogui.hotkey("enter")
pyautogui.moveTo(353,115)
pyautogui.click()
pyautogui.typewrite(x)
pyautogui.hotkey("enter")
