from ctypes.wintypes import HRSRC
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID") #format

output = cv2.VideoWriter("test.mp4", f, 20.0,dim)

now_start_time = time.time()

dur = 10
end_time = now_start_time + dur
while True:
    img = pyautogui.screenshot()
    frame1 = np.array(img)
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    current_time = time.time()
    if current_time> end_time:
        break
output.release()
print("---END---")