from __future__ import print_function
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

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 找到胜利
def shengli():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/xinzhanghao/maohao.jpg',confidence=0.8)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny


maxrand = 10
# 开始查找胜利
btnx, btny = shengli()
# btnx = btnx + random.randint(-maxrand - 10, maxrand + 10)
# btny = btny + random.randint(-maxrand, maxrand)
if is_admin():
    # 将要运行的代码加到这里
    pag.click(btnx, btny)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)



# time.sleep((counter+1) % 2)
# pag.click(duration=0.5)

# 测试一下