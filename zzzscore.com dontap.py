import pyautogui
import keyboard
import time

# LINK: https://zzzscore.com/dontap/en/

COORDS = [
	(1006, 665),
	(1133, 665),
	(888, 665),
	(778, 665)
	]

# COORDS MAY DIFFER FOR YOUR PC, pyautogui.displayMousePosition() to get coords with RGB

while not keyboard.is_pressed('q'):
	for i in COORDS:
		if pyautogui.pixel(i[0], i[1]) == (0, 0, 0):
			pyautogui.click(i[0], i[1])
			#time.sleep(.1)
