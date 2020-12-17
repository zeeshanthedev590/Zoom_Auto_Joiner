import pyautogui
import os
import time
pyautogui.FAILSAFE = False
id = input('What Is Your Meeting Id:')
passcode = input('What Is Your Passcode:')
os.startfile('C://Users//Zeeshan Khalid//AppData//Roaming//Zoom//bin//zoom.exe')
time.sleep(1)

join = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//join.png')
print(join)
pyautogui.moveTo(join)
pyautogui.click(join)

time.sleep(1)
id_in = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//id.png')

print(id_in)
pyautogui.moveTo(id_in)
pyautogui.click(id_in)
pyautogui.write(id)

time.sleep(1)
video = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//video.png')

print(video)
pyautogui.moveTo(video)
pyautogui.click(video)

time.sleep(1)
btn1 = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//btn1.png')

print(btn1)
pyautogui.moveTo(btn1)
pyautogui.click(btn1)

time.sleep(2)
passw = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//pass.png')

print(passw)
pyautogui.moveTo(passw)
pyautogui.click(passw)
pyautogui.write(passcode)

time.sleep(2)
btn2 = pyautogui.locateOnScreen(
    'G://My Projects//Python Projects//Zoom_Auto_Joiner//btn2.png')

print(btn2)
pyautogui.moveTo(btn2)
pyautogui.click(btn2)
