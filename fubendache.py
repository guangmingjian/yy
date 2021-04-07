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
pag.FAILSAFE = False
closenum = 4000
pag.PAUSE = 0.4
endIter = 300
# 挑战次数
ft = 2000
# 每次默认等待的时间
defaultInterval = 4
# 每次迭代查找的时间间隔
interval = 0
# 从战斗到准备的时间间隔
fight_prepare_interval = 4
# 开始战斗的时间间隔
beginfightInterval = 4
# 到胜利的时间
tosuccess = 5
# 战斗时间
fight_time = 5
# 到结束的时间
finish_time = 1
# 随机数最大值
maxrand = 5
confi = 0.8
imgroot2 = "image/"
imgroot1 = "image/fuben/"
imgtype = ".png"
gouliangcounter = 0
huanliang = 50
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
        btnx, btny = methodMap(methodname)
        time.sleep(1)
        pag.moveTo(x+random.randint(-10,10),y+random.randint(-5,5))
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        print("检查"+methodname)
        pag.click(duration=0.2)
        print("页面没跳转，继续点击")
    print("页面已经跳转")

# 刷御魂，iter是次数
def yuhun(iter):
    counter = 0
    while (counter < iter):
        # 开始查找挑战
        # btnx, btny = iterFind("kaishizhandou", beginInterval=beginfightInterval, iternum=500)
        # if btnx == -1 or btny == 0:
        #     print("未找到开始战斗，程序结束")
        #     return False
        # btnx = btnx + random.randint(-maxrand, maxrand)
        # pag.moveTo(btnx, btny)
        # # if counter > 0:
        # #    time.sleep((counter - 1) % 2)
        # pag.click(duration=0.5)
        #
        # jiancha("kaishizhandou",btnx, btny)
        time.sleep(4)
        dabaoflag = False
        btnx, btny = BM.iterfindpic(imgroot1 + "baoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=4)
        while btnx > 0:
            pag.click(btnx, btny)
            time.sleep(2)
            pag.click(50 + random.randint(0, 10), 600 - random.randint(0, 10))
            btnx, btny = BM.iterfindpic(imgroot1 + "baoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=10)
            dabaoflag = True
        if dabaoflag:
            print("搜索大宝箱")
            btnx, btny = BM.iterfindpic(imgroot1 + "dabaoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=3)
            if btnx > 0:
                pag.click(btnx + random.randint(-5, 5), btny + random.randint(-5, 5))
                time.sleep(5)
                pag.click(385 + random.randint(-5, 5), 398 + random.randint(-5, 5))
                time.sleep(2)

        global gouliangcounter
        gouliangcounter = gouliangcounter + 1
        print("**************************第" + str(gouliangcounter) + "个狗粮***********************")
        if gouliangcounter % huanliang == 0:
            BM.iterfindpic(imgroot2 + "zhunbei" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
            time.sleep(5)
            pag.click(544 + random.randint(-5, 5), 541)

            time.sleep(2)
            btnx, btny = BM.iterfindpic(imgroot1 + "quanbu" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
            pag.click(btnx, btny)
            btnx, btny = BM.iterfindpic(imgroot1 + "sucai" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
            pag.click(btnx, btny + random.randint(-5, 5), duration=0.01)

            btnx, btny = BM.iterfindpic(imgroot1 + "gouliang" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
            pag.moveTo(btnx, btny, duration=0.01)
            pag.dragTo(658, 455, duration=0.5)
            time.sleep(0.5)
            btnx, btny = BM.iterfindpic(imgroot1 + "gouliang" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)
            pag.moveTo(btnx, btny, duration=0.01)
            pag.dragTo(184, 418, duration=0.5)
            btnx, btny = BM.iterfindpic(imgroot1 + "gouliang" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)
            pag.moveTo(btnx, btny, duration=0.01)
            pag.dragTo(1146, 336, duration=1)

            btnx, btny = BM.iterfindpic(imgroot1 + "gouliangfanhui" + imgtype, confi=1, internaltime=0.1,
                                        mosttime=endIter)
            pag.click(btnx, btny + random.randint(-5, 5), duration=0.01)
            time.sleep(1)

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
        time.sleep(0.2)
        pag.click(btnx, btny,duration=0.6)

        jiancha("yuhunfinish",btnx, btny)
        print("点击结束")
        counter += 1
        print("第%d次"%counter)



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

