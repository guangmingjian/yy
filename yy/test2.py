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

import pyautogui as pag
import time
import os
import random

# 找到胜利
def shengli():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/diannao.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny
def queding():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/queding.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

maxrand = 10
# 开始查找胜利
while(True):
    btnx, btny = shengli()
    pag.click(btnx, btny, clicks=2)
    print(btnx, btny)
    # time.sleep((counter+1) % 2)
    # pag.click(duration=0.5)
    time.sleep(2)
    btnx, btny = queding()
    pag.click(btnx, btny, clicks=2)

