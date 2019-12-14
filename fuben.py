#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui as pag
import time
import os
pag.PAUSE = 0.4

endIter = 30
# 每次默认等待的时间
defaultInterval = 6
# 每次迭代查找的时间间隔
interval = 2
# 从战斗到准备的时间间隔
fight_prepare_interval = 4
# 开始战斗的时间间隔
beginfightInterval = 4
# 战斗时间
fight_time = 30
zhandouimgLoc = "image/fuben/zhandou.jpg"
# 找到搜索
def sousuo() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/sousuo.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny
# 找到战斗
def zhandou() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen(zhandouimgLoc,confidence=.8)
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
def unitfinish() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/yuhunfinish.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny

def xiaodeng():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/xiaodeng.jpg',confidence=.8)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx, btny

def baoxiang() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/baoxiang.jpg',confidence=.8)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny

def jiangli() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/jiangli.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx-100,btny

def methodMap(method):
    if method == "unitfinish":
        btnx, btny = unitfinish()
    elif method == "sousuo":
        btnx, btny = sousuo()
    elif method == "zhunbei":
        btnx, btny = zhunbei()
    elif method == "zhandou":
        btnx,btny = zhandou()
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

def withoutFight() :
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/zhiren.jpg')
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
    return btnx,btny-100

# 战斗并点击准备,如果找不到战斗标志，则点击纸人上方进行移动
def fight():
    # 开始查找战斗目标
    iter = 0
    maxiter = 5
    btnx, btny = iterFind("zhandou", iternum=maxiter)
    if btnx == -1 or btny == 0:
        # 可能需要多次移动，迭代移动

        while((btnx == 0 or btny==0) and iter < maxiter):
            iter += 1
            print("未找到战斗目标，需要进行移动")
            ydx, ydy = withoutFight()
            if ydx == 0 and ydy == 0:
                print("找不到纸人,程序有问题")
                return False
            # 点击进行移动
            pag.click(ydx, ydy)
            # 继续查找战斗，如果找不到证明还是没有怪，继续进行移动
            btnx, btny = iterFind("zhandou", iternum=maxiter,iterInterval=3)
    # 如果跑了maxiter次还是找不到，则有问题退出
    if iter == maxiter :
        print("始终找不到")
        return False
    # 点击战斗的图标
    pag.moveTo(btnx, btny,duration=0.1)
    pag.click(duration=0.1)
    # 有可能没有点击到这个怪物,怪物进行了移动
    time.sleep(10)
    fightbutton = pag.locateOnScreen(zhandouimgLoc)
    # # 进入到了战斗画面
    # if fightbutton == None:
    #     print("已经开始作战了")
    #     # 查找准备并点击准备
    #     # 点击准备
    #     btnx, btny = iterFind("zhunbei", iternum=4)
    #     if btnx > 0 or btny > 0:
    #         pag.moveTo(btnx, btny)
    #         pag.click(duration=0.5)
    #     return True
    # 没有进入战斗画面迭代查找
    fightiter = 0
    while((fightbutton!=None) and fightiter<maxiter):
        fightiter += 1
        btnx,btny = pag.center(fightbutton)
        pag.moveTo(btnx, btny)
        pag.click()
        time.sleep(interval)
        fightbutton = pag.locateOnScreen(zhandouimgLoc)
    # 进入到了战斗画面
    if fightiter < maxiter :
        print("已经开始作战了")
        # 查找准备并点击准备
        # 点击准备
        btnx, btny = iterFind("zhunbei", iternum=4)
        if btnx > 0 or btny > 0:
            pag.moveTo(btnx, btny)
            pag.click(duration=0.5)
        return True
    print("始终找不到怪物")
    return  False
# 部分中无攻击标志，找到右下角小纸人，向右走

def onefight():
    fightFlag = fight()
    if fightFlag != True:
        print("搜索结束")
        return False
    # 开始查找单个怪物的结束
    # 查找结束标志
    btnx, btny = iterFind("unitfinish", beginInterval=fight_time, iternum=60)
    if btnx == -1 or btny == 0:
        print("未找到结束标志，程序出错")
        return False
    pag.moveTo(btnx, btny)
    pag.click(duration=0.5)

def beginSousuo():
    # 开始查找搜索
    btnx, btny = iterFind("sousuo", beginInterval=beginfightInterval, iternum=5)
    if btnx == -1 or btny == 0:
        print("未找到搜索，程序结束")
        return False
    pag.moveTo(btnx, btny)
    pag.click()

def fuben(iter):
    counter = 0
    while (counter < iter):
        counter += 1
        beginSousuo()
        # 进行一次战斗

        onefight()
        # # 检查是否结束
        # yhfinbtnx, yhfinbtny = unitfinish()
        # time.sleep(8)
        # zbiter = 1
        # while (yhfinbtnx == 0 and yhfinbtny == 0) and zbiter < 30:
        #     time.sleep(2)
        #     yhfinbtnx, yhfinbtny = unitfinish()
        #     zbiter += 1
        # # 时间太长了有问题
        # if zbiter == 30:
        #     return False
        # pag.moveTo(yhfinbtnx, yhfinbtny)
        # pag.click(duration=0.2)
        # counter += 1
        # print(counter)

# fuben(3)

# fuben(2)
yhfinbtnx,yhfinbtny = xiaodeng()
pag.moveTo(yhfinbtnx,yhfinbtny)
# pag.click()
# time.sleep(2)
# yhfinbtnx,yhfinbtny = jiangli()
# pag.moveTo(yhfinbtnx,yhfinbtny)
# pag.click()


# fightFlag = fight()
# yhfinbtnx, yhfinbtny = unitfinish()
# time.sleep(8)
# zbiter = 1
# while (yhfinbtnx == 0 and yhfinbtny == 0) and zbiter < 30:
#     time.sleep(2)
#     yhfinbtnx, yhfinbtny = unitfinish()
#     zbiter += 1
# # 时间太长了有问题
# if zbiter == 30:
#     print("bug")
# pag.moveTo(yhfinbtnx, yhfinbtny)
# pag.click(duration=0.2)
#
# yhfinbtnx, yhfinbtny = unitfinish()
# time.sleep(8)
# zbiter = 1
# while (yhfinbtnx == 0 and yhfinbtny == 0) and zbiter < 30:
#     time.sleep(2)
#     yhfinbtnx, yhfinbtny = unitfinish()
#     zbiter += 1
#     pag.moveTo(yhfinbtnx, yhfinbtny)
#     pag.click(duration=0.2)
