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
import closegame as cg
import BasicMethod as BM
closenum = 1500
pag.PAUSE = 0.6
endIter = 2000
# 挑战次数
ft = 30
# 每次默认等待的时间
defaultInterval = 2
# 每次迭代查找的时间间隔
interval = 0
# 从战斗到准备的时间间隔
fight_prepare_interval = 2
# 开始战斗的时间间隔
beginfightInterval = 2
# 到胜利的时间
tosuccess = 3
# 战斗时间
fight_time = 3
# 到结束的时间
finish_time = 0.1
# 随机数最大值
maxrand = 5
confi = 0.8
pag.FAILSAFE = False
imgroot2 = "image/"
imgroot1 = "image/fuben/"
imgtype = ".png"
# 找到挑战
def tiaozhan():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/tiaozhan.png')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

# 找到任务
def renwu():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/renwu.png',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny


# 找到开始战斗
def kaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/tiaozhan.png',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny


# 找到胜利
def shengli():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/shengli.png',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

# 找到准备
def zhunbei():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/zhunbei.jpg',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny


def yuhunfinish():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/dianjijixu.png',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny


def methodMap(method):
    rbtnx, rbtny = renwu()
    if rbtnx > 0 and rbtny > 0:
        pag.moveTo(rbtnx, rbtny)
        # time.sleep((counter+1) % 2)
        pag.click(duration=0.2)
    if method == "yuhunfinish":
        btnx, btny = yuhunfinish()
    elif method == "tiaozhan":
        btnx, btny = tiaozhan()
    elif method == "zhunbei":
        btnx, btny = zhunbei()
    elif method == "kaishizhandou":
        btnx, btny = kaishizhandou()
    elif method == "shengli":
        btnx, btny = shengli()
    else:
        return -1, -1
    return btnx, btny


'''
    迭代查找某一图片，查找到相应的图片则返回true，否则false

    :argument
    ----------
    arg1：将要查找的方法名
    arg2：初次查找的时间间隔
    arg3：最大的迭代次数
    arg4：每次迭代的时间间隔 
    ----------
    :returns
    ----------
    :return1 btnx
    :return2 btny
    如果没找到则返回-1，-1
    ----------
'''


def iterFind(method, beginInterval=defaultInterval, iternum=endIter, iterInterval=interval):
    btnx = 0
    btny = 0
    # 第一次搜索的时间间隔
    time.sleep(beginInterval)
    # 找到映射的方法，传入string值，得到相应的btnx，btny
    btnx, btny = methodMap(method)
    # 如果传入的string名称错误，证明没有此函数，退出程序
    if btnx == -1:
        print("方法名有误")
        os._exit(0)
        return -1, -1
    print("开始查找" + method)
    print(btnx, btny)
    iter = 0
    # 如果第一次未找到，循环进行查找，迭代iternum次，每次间隔iterInterval
    while (btnx == 0 and btny == 0) and iter < iternum:
        time.sleep(iterInterval)
        btnx, btny = methodMap(method)
        iter += 1
        print(btnx, btny)
        print(method + "查找次数：", iter)
        if iter > closenum:
            cg.closegame()
            exit(0)

    print(method + "查找次数", iter)
    # 时间太长了有问题
    if iter == endIter:
        print(method + "查找有问题")
        return -1, -1
    print(method + "查找成功")
    return btnx, btny

def jiancha(methodname,x,y):
    btnx, btny = methodMap(methodname)
    while (btnx > 0):

        time.sleep(0.4)
        pag.moveTo(x+random.randint(-10,10),y+random.randint(-5,5))
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        print("检查"+methodname)
        pag.click(duration=0.2)
        print("页面没跳转，继续点击")
        btnx, btny = methodMap(methodname)
    print("*********页面已经跳转********************")

# 刷御魂，iter是次数
def yuhun(iter):
    counter = 0
    while (counter < iter):
        # 开始查找挑战
        btnx, btny = iterFind("kaishizhandou", beginInterval=beginfightInterval, iternum=500)
        if btnx == -1 or btny == 0:
            print("未找到开始战斗，程序结束")
            return False
        btnx = btnx + random.randint(-maxrand, maxrand)
        pag.moveTo(btnx, btny,duration=0.6)
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        pag.click(duration=0.2)

        jiancha("kaishizhandou",btnx, btny)

        btnx, btny = BM.iterfindpic(imgroot2 + "zhunbei" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
        pag.click(btnx, btny, duration=0.01)

        BM.jiancha(imgroot2 + "zhunbei" + imgtype, 1, btnx, btny, 1)


        # 开始查找胜利
        btnx, btny = iterFind("shengli", beginInterval=tosuccess, iternum=450)
        if btnx == -1 or btny == 0:
            print("未找到开始战斗，程序结束")
            return False
        btnx = btnx + random.randint(-maxrand-10, maxrand+10)
        btny = btny + random.randint(-maxrand, maxrand)
        pag.moveTo(btnx, btny)
        #time.sleep((counter+1) % 2)
        pag.click(btnx, btny,duration=0.2)
        pag.click(btnx, btny, duration=0.2)

        # 查找结束标志
        btnx, btny = iterFind("yuhunfinish", beginInterval=finish_time, iternum=500)
        if btnx == -1 or btny == 0:
            print("未找到结束标志，程序出错")
            return False

        btnx = 941 + random.randint(-maxrand - 30, maxrand + 30)
        btny = 569 + random.randint(0, 20)
        #time.sleep(counter%2)
        print("移动结束")
        time.sleep(0.8)
        pag.doubleClick(btnx, btny,duration=0.2)
        pag.doubleClick(btnx, btny, duration=0.2)
        # jiancha("yuhunfinish",btnx, btny)
        # btnx,btny = BM.findpic("image/jiejietupo/queding.png",confi=0.8)
        # if btnx > 0 :
        #     pag.click(btnx,btny,duration=0.001)
        print("点击结束")
        counter += 1
        print("*********************第%d次"%counter)



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
# if is_admin():
#     yuhun(ft)
#     print("finish")
# else:
#     if sys.version_info[0] == 3:
#     	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     else:#in python2.x
#         ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
yuhun(ft)

