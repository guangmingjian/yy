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
    testbutton = pag.locateOnScreen('image/jiejietupo/shuaxin2.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

maxrand = 10
# 开始查找胜利
btnx, btny = shengli()
btnx = btnx + random.randint(-maxrand - 10, maxrand + 10)
btny = btny + random.randint(-maxrand, maxrand)
pag.moveTo(btnx, btny)
# time.sleep((counter+1) % 2)
# pag.click(duration=0.5)

# 测试一下