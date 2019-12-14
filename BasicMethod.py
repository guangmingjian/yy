import pyautogui as pag
import pyautogui as pag
import numpy as np
import time
import os
import random
defaultconfi = 0.8

# 找到任务
def renwu():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/renwu.png',confidence=defaultconfi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        print("寻找任务成功")
    else:
        print("无任务")
    return btnx, btny

def findpic(loc, confi):
    rbtnx, rbtny = renwu()
    if rbtnx > 0 and rbtny > 0:
        pag.moveTo(rbtnx, rbtny)
        # time.sleep((counter+1) % 2)
        pag.click(duration=0.2)
    btnx = 0
    btny = 0
    if confi == 1:
        testbutton = pag.locateOnScreen(loc)
    else:
        testbutton = pag.locateOnScreen(loc, confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        print(loc +  "   已经找到    ")
    else:
        print(loc + "   没有找到    ")
    return btnx, btny


def jiancha(loc, confi,x,y,internal=1):
    btnx, btny = findpic(loc,confi)
    while (btnx > 0):

        time.sleep(internal)
        pag.moveTo(x+random.randint(-10,10),y+random.randint(-5,5))
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        print("检查"+loc)
        pag.click(duration=0.2)
        print("页面没跳转，继续点击")
        btnx, btny = findpic(loc, confi)
    print("页面已经跳转")

def iterfindpic(loc,confi,internaltime,mosttime):
    btnx,btny = findpic(loc,confi)
    counter = 0
    while btnx == 0:
        time.sleep(internaltime)
        counter += 1
        if counter > mosttime:
            return 0,0
        btnx, btny = findpic(loc, confi)
    print("迭代寻找  " +loc + "  成功 ")
    return  btnx, btny
