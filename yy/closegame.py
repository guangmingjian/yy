import pyautogui as pag
import time
# from __future__ import print_function
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



imgroot = "image/"

def findpic(picloc,confidence):
    btnx = 0
    btny = 0
    if confidence < 1 :
        testbutton = pag.locateOnScreen(imgroot + picloc +'.png',confidence=confidence)
    else:
        testbutton = pag.locateOnScreen('image/zhunbei.png', confidence=confidence)

    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

def closegame():
    btnx, btny = findpic("closegame",0.9)
    time.sleep(2)
    if btnx > 0 :
        pag.click(btnx, btny)
        print("点击关闭按钮")

    time.sleep(2)
    btnx, btny = findpic("qdclose", 0.9)
    if btnx > 0 :
        pag.click(btnx, btny)
        print("关闭")


# closegame()
