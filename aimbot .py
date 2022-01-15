import pyautogui
import time

while True:
    x,y = pyautogui.position()
    print('X=',x, 'Y=',y, end='')
    print('\b' * 15, end='')
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(1)