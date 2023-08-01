import pyautogui as py
import time
import os

def p(x):
    py.press(x)
    time.sleep(1)

def e(x):
    py.write(x)
    time.sleep(1)

def ent():
    py.press("enter")
    time.sleep(1)

p("win")
e("google")
ent()
e("gmail.com")
ent()
time.sleep(2)
py.press("tab", presses=5)
ent()

os.system("pause")