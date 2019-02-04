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


# 找到开始战斗
def kaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/jiejietupo/zhenrong.jpg',confidence=0.8)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    # else:
    #     pag.click(duration=0.2)
    return btnx, btny


btnx,btny = kaishizhandou()
pag.moveTo(btnx,btny-60)