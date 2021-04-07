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
ft = 200
# 每次默认等待的时间
defaultInterval = 2
# 每次迭代查找的时间间隔
interval = 0
# 从战斗到准备的时间间隔
fight_prepare_interval = 2
# 开始战斗的时间间隔
beginfightInterval = 2
# 到胜利的时间
tosuccess = 20
# 战斗时间
fight_time = 20
# 到结束的时间
finish_time = 0.1
# 随机数最大值
maxrand = 5
confi = 0.8
pag.FAILSAFE = False
# 找到挑战
img_root = "image"
pic_type = ".png"

get_pic = lambda cont: BM.get_pic_loc(img_root,cont,pic_type)
# print(BM.get_pic_loc(img_root,"tiaozhan",pic_type))
# 刷御魂，iter是次数
def yuhun(iter):
    counter = 0
    while (counter < iter):
        x,y = BM.get_jieshu_axis(False)
        # time.sleep(1)
        # 查找挑战
        BM.jianchanoclick(get_pic("tiaozhan"),0.9,2)
        pag.click(x+random.randint(-5,5),y+random.randint(-5,5))
        time.sleep(2)
        # 找到了挑战
        BM.jianchaandclick(get_pic("shizhong"),0.8,x,y,1)
        # 找到了魂土猫，正在开始战斗
        # BM.jiancha(get_pic("tiaozhan"),0.8,0.1)

        BM.jianchatodis(get_pic("shizhong"),0.8,0.3)
        time.sleep(0.5)
        BM.new_shengli()
        #
        #
        #
        #
        # # 开始查找挑战
        # btnx, btny = iterFind("kaishizhandou", beginInterval=beginfightInterval, iternum=500)
        # if btnx == -1 or btny == 0:
        #     print("未找到开始战斗，程序结束")
        #     return False
        # btnx = btnx + random.randint(-maxrand, maxrand)
        # pag.moveTo(btnx, btny,duration=1)
        # # if counter > 0:
        # #    time.sleep((counter - 1) % 2)
        # pag.click(duration=0.2)
        #
        # jiancha("kaishizhandou",btnx, btny)
        #
        #
        #
        # # 开始查找胜利
        # btnx, btny = iterFind("shengli", beginInterval=tosuccess, iternum=endIter)
        # if btnx == -1 or btny == 0:
        #     print("未找到开始战斗，程序结束")
        #     return False
        # btnx = btnx + random.randint(-maxrand-10, maxrand+10)
        # btny = btny + random.randint(-maxrand, maxrand)
        # pag.moveTo(btnx, btny)
        # #time.sleep((counter+1) % 2)
        # pag.click(btnx, btny,duration=0.2)
        # pag.click(btnx, btny, duration=0.2)
        #
        # # 查找结束标志
        # btnx, btny = iterFind("yuhunfinish", beginInterval=finish_time, iternum=endIter)
        # if btnx == -1 or btny == 0:
        #     print("未找到结束标志，程序出错")
        #     return False
        #
        # btnx = 941 + random.randint(-maxrand - 30, maxrand + 30)
        # btny = 569 + random.randint(0, 20)
        # #time.sleep(counter%2)
        # print("移动结束")
        # time.sleep(0.8)
        # pag.click(btnx, btny,duration=0.2)
        #
        # jiancha("yuhunfinish",btnx, btny)
        print("点击结束")
        counter += 1
        print("*********************第%d次"%counter)




# if is_admin():
#     yuhun(ft)
#     print("finish")
# else:
#     if sys.version_info[0] == 3:
#     	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     else:#in python2.x
#         ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
yuhun(ft)

