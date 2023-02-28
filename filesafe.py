import pyautogui
import time


#   FAIL-SAFE Do not disable this
pyautogui.FAILSAFE = True

# Example
time.sleep(3)
text = open("derails.txt")
for each_line in text:
    pyautogui.write(each_line)
