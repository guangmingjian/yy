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
import time
import win32gui, win32ui, win32con, win32api


# 找到开始战斗
def kaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/test/2.png',confidence = 0.8)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        print(btnx, btny)
    # else:
    #     pag.click(duration=0.2)
    return btnx, btny

def allkaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateAllOnScreen('image/test/1.png',confidence=0.8)
    return testbutton

def window_capture(filename):
    hwnd = 726754  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

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

# 提交

def testfunction():
    flag = 1
    while flag > 0:
        btnx, btny = kaishizhandou()
        print(flag)
        flag += 1
        if btnx > 0:
            print("找到了")
            pag.moveTo(btnx, btny)
            break
        time.sleep(2)

window_capture("image/test/1.png")
