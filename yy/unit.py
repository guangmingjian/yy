#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
@File    : 
@Time    : 
@Author  : mingjian
@Software: PyCharm
@Desc    :
    描述
"""
import pyautogui as  pag
import random
import time
# 找到开始战斗
def kaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/test/jingyanjc.jpg',confidence = 1)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    # else:
    #     pag.click(duration=0.2)
    return btnx, btny

def allkaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateAllOnScreen('image/test/jingyanjc.jpg',confidence=0.65)
    return testbutton

# maxrand = 5
# testbutton = allkaishizhandou()
# counter = 1
# for i in  testbutton:
#    btnx,btny = pag.center(i)
#    pag.moveTo(btnx,btny)
#    print(counter)
#    time.sleep(3)
#    counter += 1
# btnx = btnx + random.randint(-maxrand-50, maxrand+50)
# btny = btny + random.randint(-maxrand, maxrand)
flag = 1
while flag > 0:
    btnx,btny = kaishizhandou()
    print(flag)
    flag += 1
    if btnx > 0:
        pag.moveTo(btnx,btny)
    time.sleep(2)
# 提交