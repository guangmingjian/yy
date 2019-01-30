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

pag.PAUSE = 0.2
endIter = 30
# 挑战次数
ft = 200
# 每次默认等待的时间
defaultInterval = 4
# 每次迭代查找的时间间隔
interval = 0.2
# 从战斗到准备的时间间隔
fight_prepare_interval = 4
# 开始战斗的时间间隔
beginfightInterval = 4
# 到胜利的时间
tosuccess = 25
# 战斗时间
fight_time = 20
# 到结束的时间
finish_time = 1
# 随机数最大值
maxrand = 10
confi = 0.8

# 找到挑战
def tiaozhan():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/tiaozhan.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

# 找到任务
def renwu():
    btnx = 0
    btny = 0
    try:
        testbutton = pag.locateOnScreen('image/renwu.jpg',confidence=confi)
        btnx, btny = pag.center(testbutton)
    except Exception as e:
        print("未找到任务")


    return btnx, btny


# 找到开始战斗
def kaishizhandou():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/kaishizhandou.jpg',confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    else:
        pag.click(duration=0.2)
    return btnx, btny


# 找到胜利
def shengli():
    btnx = 0
    btny = 0
    try:
        testbutton = pag.locateOnScreen('image/shengli.jpg', confidence=confi)
        btnx, btny = pag.center(testbutton)
    except Exception as e:
        print("未找到胜利")


    return btnx, btny

# 找到准备
def zhunbei():
    btnx = 0
    btny = 0
    try:
        testbutton = pag.locateOnScreen('image/zhunbei.jpg', confidence=confi)
        btnx, btny = pag.center(testbutton)
    except Exception as e:
        print
        "I/O error({0}): {1}".format(e.errno, e.strerror)
    return btnx, btny


def yuhunfinish():
    btnx = 0
    btny = 0

    try:
        testbutton = pag.locateOnScreen('image/yuhunfinish.jpg')
        btnx, btny = pag.center(testbutton)
    except Exception as e:
        print("未找到结束")
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
    print(method + "查找次数", iter)
    # 时间太长了有问题
    if iter == endIter:
        print(method + "查找有问题")
        return -1, -1
    print(method + "查找成功")
    return btnx, btny


# 刷御魂，iter是次数
def yuhun(iter):
    counter = 0
    while (counter < iter):
        # # 开始查找挑战
        # btnx, btny = iterFind("kaishizhandou", beginInterval=beginfightInterval, iternum=500)
        # if btnx == -1 or btny == 0:
        #     print("未找到开始战斗，程序结束")
        #     return False
        # btnx = btnx + random.randint(-maxrand, maxrand)
        # pag.moveTo(btnx, btny)
        # #if counter > 0:
        # #    time.sleep((counter - 1) % 2)
        # pag.click(duration=0.5)

        # 开始查找胜利
        btnx, btny = iterFind("shengli", beginInterval=tosuccess, iternum=450)
        if btnx == -1 or btny == 0:
            print("未找到开始战斗，程序结束")
            return False
        btnx = btnx + random.randint(-maxrand-10, maxrand+10)
        btny = btny + random.randint(-maxrand, maxrand)
        pag.moveTo(btnx, btny)
        #time.sleep((counter+1) % 2)
        pag.click(duration=0.2)

        # 查找结束标志
        btnx, btny = iterFind("yuhunfinish", beginInterval=finish_time, iternum=500)
        if btnx == -1 or btny == 0:
            print("未找到结束标志，程序出错")
            return False
        btnx = btnx + random.randint(-maxrand - 10, maxrand + 10)
        btny = btny + random.randint(120, 125)
        #time.sleep(counter%2)
        print("移动结束")
        time.sleep(1.2)
        pag.click(btnx, btny,duration=0.6)
        time.sleep(2)
        pag.click(btnx, btny,duration=0.2)
        print("点击结束")
        counter += 1
        print("第%d次"%counter)

#
yuhun(ft)
print("finish")