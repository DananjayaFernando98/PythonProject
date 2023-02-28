import pyautogui
import time

# Give the python file some time before connecting
time.sleep(3)

#Mouse Function

# Print the resulution of your screen
#print(pyautogui.size())


# Prints the Current Position
#print(pyautogui.position())

# Moves the mouse overtime (3 second)
# pyautogui.moveTo(100, 100, 3)

# move the mouse relative to its current position
# pyautogui.moveRel(100, 100, 3)

#Click

# pyautogui.click(500, 500, 3, 3, button="left" )

# pyautogui.tripleClick()
# pyautogui.doubleClick()
# pyautogui.leftClick()
# pyautogui.rightClick()

# Scroll Up 500
# pyautogui.scroll(500)

# Scroll down 500
# pyautogui.scroll(-500)

# Mouse UP & Mouse Down
# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")

# Example of mouse up & down
# pyautogui.mouseDown(100, 400, button="left")
# pyautogui.moveTo(800, 400, 3)
#
# pyautogui.mouseUp()
# pyautogui.moveTo(1000, 400, 3)

# pyautogui.mouseDown(150, 400, button="left")
# pyautogui.moveTo(150, 500, 3)


# Spiral
# time.sleep(1)
#
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, distance, 1, button="left")
#     pyautogui.dragRel(-distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, -distance, 1, button="left")
# time.sleep(2)

# TikTok Liker Example
# time.sleep(3)
# range will be the you want like
# for i in range(10):
#     pyautogui.moveTo(450, 500)
#     time.sleep(1)
#     pyautogui.doubleClick()
#     time.sleep(1)
#     pyautogui.moveTo(840, 500)
#     time.sleep(1)
#     pyautogui.leftClick()

# Keyboard Function
# pyautogui.write("Hello Github")
# pyautogui.press("enter")
# pyautogui.press("space")


# Dino Game - Chrome
# time.sleep(3)
# for i in range(20):
#     pyautogui.press("space")
#     time.sleep(0.5)

# Screenshot in pyautogui
pyautogui.screenshot("Screenshot.png")











