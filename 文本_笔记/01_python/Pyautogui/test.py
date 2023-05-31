import pyautogui
from PIL import Image
import time
import sys

pyautogui.hotkey("alt", "tab")
time.sleep(1)
pyautogui.click(900, 450)
# pyautogui.screenshot("gj.jpg", region=(860, 290, 210, 65))
# pyautogui.screenshot("gj1.jpg", region=(780, 270, 350, 100))
#
# while True:
#     loc = pyautogui.locateCenterOnScreen("gj.jpg")
#     print(loc)

# pyautogui.keyDown("z")
if len(sys.argv) >= 2:
    sleep_time = float(sys.argv[1])
    print(sleep_time)
else:
    sleep_time = 0
while True:
    pyautogui.keyDown("z")
    pyautogui.keyUp("z")
    if sleep_time == 0:
        continue
    else:
        time.sleep(sleep_time)
