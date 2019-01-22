#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui as pag
import time
import os
pag.PAUSE = 0.2
endIter = 60
interval = 2
fight_prepare_interval = 6
# 找到挑战
def tiaozhan() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/tiaozhan.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny
# 找到准备
def zhunbei() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/zhunbei.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny

def yuhunfinish() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/yuhunfinish.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny
def methodMap(method):
    if method == "yuhunfinish":
        btnx, btny = yuhunfinish()
    elif method == "tiaozhan":
        btnx, btny = tiaozhan()
    elif method == "zhunbei":
        btnx, btny = zhunbei()
    else:
        return -1,-1
    return btnx,btny

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
    boolean：
    true or false
    ----------
'''
def iterFind(method,beginInterval=6,iternum=30,iterInterval=2):
    btnx = 0
    btny = 0
    # 第一次搜索的时间间隔
    time.sleep(beginInterval)
    # 找到映射的方法，传入string值，得到相应的btnx，btny
    btnx,btny = methodMap(method)
    # 如果传入的string名称错误，证明没有此函数，退出程序
    if btnx == -1:
        print("方法名有误")
        os._exit(0)
        return False
    print("开始查找"+ method)
    print(btnx, btny)
    iter = 0
    # 第一次未找到，循环进行查找，迭代iternum次，每次间隔iterInterval
    while (btnx == 0 and btny == 0) and iter < iternum:
        time.sleep(iterInterval)
        btnx, btny = methodMap(method)
        iter += 1
        print(btnx, btny)
    print(method+ "查找次数"+iter)
    # 时间太长了有问题
    if iter == endIter:
        print(method+"查找有问题")
        return False
    print(method+"查找成功")
    return True


# 刷御魂，iter是次数
def yuhun(iter,waitfinish = 10):
    beginInterval = 4
    counter = 0
    while(counter<iter):
        time.sleep(beginInterval)
        print("查找开始挑战")
        tzbtnx,tzbtny = tiaozhan()
        # 可以进行挑战了
        if tzbtnx > 0 and tzbtny>0:
            # 移动到挑战并点击挑战
            pag.moveTo(tzbtnx,tzbtny)
            pag.click(duration=0.5)
            time.sleep(fight_prepare_interval)
            zbbtnx,zbbtny = zhunbei()
            print("查找准备")
            # 不断获取直到找到准备,可能已经固定阵容
            # 如果是固定阵容也跳出循环
            zbiter = 1
            while (zbbtnx == 0 and zbbtny == 0)and zbiter<4  :
                time.sleep(interval)
                zbbtnx, zbbtny = zhunbei()
                zbiter += 1
            # 点击准备
            if zbbtny > 0 and zbbtny > 0:
                pag.moveTo(zbbtnx,zbbtny-60)
                pag.click()
            yhfinbtnx, yhfinbtny = yuhunfinish()
            time.sleep(waitfinish)
            print("开始查找结束")
            print(yhfinbtnx,yhfinbtny)
            zbiter = 1
            while (yhfinbtnx == 0 and yhfinbtny == 0) and zbiter < endIter:
                time.sleep(interval)
                yhfinbtnx, yhfinbtny = yuhunfinish()
                zbiter += 1
                print(yhfinbtnx, yhfinbtny)
            print(zbiter)
            # 时间太长了有问题
            if zbiter == endIter:
                return counter
            pag.moveTo(yhfinbtnx,yhfinbtny)
            pag.click(duration=0.2)
            counter += 1

yuhun(1,70)
print("finish")
