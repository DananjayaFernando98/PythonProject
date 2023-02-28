import time
import pyautogui

time.sleep(5)  # python file sleep for 5 second
text = open("message.txt")  # opening text file

for each_line in text:
    pyautogui.typewrite(each_line)  # type writing the file
