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
import numpy as np
import time
import os
import random
pag.PAUSE = 0.4
# 找到挑战
class ToPo:
    endIter = 30
    # 挑战次数
    ft = 10
    # 每次默认等待的时间
    defaultInterval = 4
    # 每次迭代查找的时间间隔
    interval = 0.5
    maxrand = 10

    def __init__(self):
        self.succ_num = 0
        self.fl = np.zeros([9,2],dtype=int) #保存鼠标点击九宫格的位置
        self.jjtp = 'image/jiejietupo/jiejietupo.jpg' #结界突破位置
        self.gpjl = 'image/jiejietupo/gongpojilu.jpg'  # 攻破记录的位置
        self.sx = 'image/jiejietupo/shuaxin.jpg'  # 刷新的位置
        self.sx2 = 'image/jiejietupo/shuaxin2.jpg'  # 刷新的位置
        self.gr = 'image/jiejietupo/geren.jpg'  # 攻破记录的位置
        self.yyl= 'image/jiejietupo/yinyangliao.jpg'  # 刷新的位置
        self.jg = 'image/jiejietupo/jingong.jpg'  # 进攻的位置
        self.sl = 'image/jiejietupo/shengli.jpg'  # 胜利的位置
        self.js = 'image/jiejietupo/jieshu.jpg'  # 结束的位置
        self.sb = 'image/jiejietupo/shibai.jpg'  # 失败的位置
        self.qd = 'image/jiejietupo/queding.jpg'  # 确定的位置
        self.first = 1
        self.shuaxinbtnx = 0
        self.shuaxinbtny = 0

    class Mytimer:
        #
        def __str__(self):
            return self.prompt

        __repr__ = __str__

        # 初始化操作
        def __init__(self):
            self.unit = ['年', '月', '天', '小时', '分钟', '秒 ']
            self.prompt = '未开始计时'
            self.lasted = []
            self.begin = 0  # 此处不可用start 因为属性名与方法名一样，属性名会覆盖方法，end同理
            self.end = 0

        # 时间相加
        def __add__(self, other):
            prompt = '一共运行了'
            result = []
            for index in range(6):
                result.append(self.lasted[index] + other.lasted[index])
                if result[index]:
                    prompt += str(result[index]) + self.unit[index]
            return prompt

        # 开始计时
        def start(self):
            self.begin = time.localtime()
            self.prompt = "请先stop"
            print("计时开始")

        # 停止计时
        def stop(self):
            if not self.begin:
                print("请先进行")
            else:
                self.end = time.localtime()
                self._calc()
                print("计时结束")

        # 内部方法

        def _calc(self):
            self.lasted = []
            self.prompt = '总共运行了'
            for index in range(6):
                self.lasted.append(self.end[index] - self.begin[index])
                if self.lasted[index]:
                    self.prompt += str(self.lasted[index]) + self.unit[index]
            # 为下轮循环初始化
            self.begin = 0
            self.end = 0

    # 查找图片位置
    def findfigure(self,location):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(location)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny
    # 返回界面上方结界突破的位置，确定第二列的x的位置
    def jiejietupo(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.jjtp)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny

    # 攻破记录的位置，确定第一列中x的位置
    def gongpojilu(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.gpjl)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny

    # 刷新的位置，确定第三列x轴位置
    def shuaxin(self):
        btnx = 0
        btny = 0
        testbutton = None
        if self.first > 0:
            testbutton = pag.locateOnScreen(self.sx)
            self.first = 0
        else:
            testbutton = pag.locateOnScreen(self.sx2)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
            self.shuaxinbtnx = btnx
            self.shuaxinbtny = btny
        return btnx, btny

    # 个人
    def geren(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.gr)
        if testbutton != None:
            btnx = testbutton[0]
            btny = testbutton[1]
        return btnx, btny

    #阴阳寮
    def yinyangliao(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.yyl)
        if testbutton != None:
            btnx = testbutton[1]
            btny = testbutton[1] + testbutton[3]
        return btnx, btny


    # 进攻
    def jingong(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.jg,confidence=0.8)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny

    # shengli
    def shengli(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.sl)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
            self.succ_num += 1
        return btnx, btny

    # 失败
    def shibai(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.sb)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny

    # 结束
    def jieshu(self):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(self.js)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
            self.succ_num += 1
        return btnx, btny




    def fight_location(self):
        btnx1, btny1 = self.gongpojilu()
        btnx2, btny2 = self.jiejietupo()
        btnx3, btny3 = self.shuaxin()
        btnx4, btny4 = self.geren()
        btnx5, btny5 = self.yinyangliao()
        self.fl[0] = [btnx1,btny4]
        self.fl[1] = [btnx1, btnx5]
        self.fl[2] = [btnx1, btny5]
        self.fl[3] = [btnx2, btny4]
        self.fl[4] = [btnx2, btnx5]
        self.fl[5] = [btnx2, btny5]
        self.fl[6] = [btnx3, btny4]
        self.fl[7] = [btnx3, btnx5]
        self.fl[8] = [btnx3, btny5]
        return self.fl

    def methodMap(self,method):
        if method == "jingong":
            btnx, btny = self.jingong()
        elif method == "jieshu":
            btnx, btny = self.jieshu()
            if btnx < 1 and btny < 1:
                btnx, btny = self.shibai()
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

    def iterFind(self,method, beginInterval=defaultInterval, iternum=endIter, iterInterval=interval):
        btnx = 0
        btny = 0
        # 第一次搜索的时间间隔
        time.sleep(beginInterval)
        # 找到映射的方法，传入string值，得到相应的btnx，btny
        btnx, btny = self.methodMap(method)
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
            btnx, btny = self.methodMap(method)
            iter += 1
            print(btnx, btny)
        print(method + "查找次数", iter)
        # 时间太长了有问题
        if iter == iternum:
            print(method + "查找有问题")
            return -1, -1
        print(method + "查找成功")
        return btnx, btny

    # 一次消耗三劵
    def fightOneFresh(self):
        self.succ_num = 0
        self.fight_location()
        # 每成功一次增加记数，
        # 如果全部挑战完成，没有成功到达3次，返回-1
        for i in range(9):
            time.sleep(10)
            pag.click(self.fl[i][0],self.fl[i][1])
            # 开始查找进攻
            btnx, btny = self.iterFind("jingong", beginInterval=2, iternum=30)
            if btnx == -1 or btny == 0:
                print("未找到进攻，程序结束")
                return False
            btnx = btnx + random.randint(-self.maxrand -5 , self.maxrand +5 )
            pag.moveTo(btnx, btny)
            # time.sleep((counter+1) % 2)
            pag.click(duration=0.4)


            # 开始查找结束
            btnx, btny = self.iterFind("jieshu", beginInterval=12, iternum=2000)
            if btnx == -1 or btny == 0:
                print("未找到结束，程序结束")
                return False
            btnx = btnx + random.randint(-self.maxrand - 10, self.maxrand + 10)
            btny = btny + random.randint(-self.maxrand- 10, self.maxrand + 10)
            pag.moveTo(btnx, btny)
            # time.sleep((counter+1) % 2)
            pag.click(duration=0.4)
            time.sleep(1.5)
            pag.click(duration=0.4)
            if self.succ_num >=3:
                return 1
        if self.succ_num>=3:
            return 1
        else :
            return -1




    def fightnN(self,k):
        for i in range(k):
            mt = self.Mytimer()
            mt.start()
            self.fightOneFresh()
            time.sleep(10)
            pag.click(self.fl[7][0], self.fl[7][1])
            time.sleep(3)
            mt.stop()
            runtime = mt.lasted
            print(runtime)
            if runtime[0] > 0 or runtime[1] > 0 or runtime[2] > 0 or runtime[3] > 0:
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx,btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)
            elif runtime[4] >= 5:
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx, btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)
            elif runtime[4] < 5 and runtime[4] >=4 :
                time.sleep(1*60)
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx, btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)
            elif runtime[4] < 4 and runtime[4] >= 3:
                time.sleep(2 * 60)
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx, btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)
            elif runtime[4] < 3 and runtime[4] >= 2:
                time.sleep(3 * 60)
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx, btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)
            else:
                time.sleep(4.5 * 60)
                pag.click(self.shuaxinbtnx, self.shuaxinbtny)
                time.sleep(5)
                btnx, btny = self.findfigure(self.qd)
                if btnx == -1 or btny == 0:
                    print("未找到确定，程序结束")
                    return False
                btnx = btnx + random.randint(-self.maxrand - 5, self.maxrand + 5)
                pag.click(btnx, btny)



# btnx, btny , testbutton = tiaozhan()
# pag.moveTo(testbutton[0]+testbutton[2],testbutton[1]+testbutton[3])
#

# tp = ToPo()
#
# f1 = tp.fight_location()
# print(f1)
# row = 8
# pag.moveTo(f1[row][0],f1[row][1])

tp = ToPo()
tp.fightnN(5)