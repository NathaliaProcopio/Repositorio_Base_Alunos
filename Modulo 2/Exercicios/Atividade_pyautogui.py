import pyautogui

pyautogui.PAUSE = 0.4

pyautogui.hotkey("win", "r")
pyautogui.write("calc")
pyautogui.press("enter")

pyautogui.write("8 + 2")
pyautogui.press("enter")