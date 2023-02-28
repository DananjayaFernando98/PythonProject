import pyautogui
import time

# Give the python file some time before connecting
time.sleep(5)

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
time.sleep(1)

distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
time.sleep(2)





