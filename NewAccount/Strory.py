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
    对剧情进行处理
"""

import pyautogui as pag
import time
import os
import random

pag.PAUSE = 0.2


class story:

    def __init__(self):
        self.find_False_num = 0
        self.mh = "image/xinzhanghao/maohao.jpg" #冒号的位置
        self.tg = "image/xinzhanghao/tiaoguo.jpg"  # 跳过的位置
        self.jias = "image/xinzhanghao/jiasu.jpg"  # 跳过的位置
        self.jx = "image/xinzhanghao/jixu.jpg"  # 点击任意位置继续的位置
        self.xs = "image/xinzhanghao/xiaoshou.png"  # 点击任意位置继续的位置
        self.qd = "image/xinzhanghao/queding.jpg"  # 点击任意位置继续的位置
        self.zd = "image/xinzhanghao/zhandou.jpg"  # 点击任意位置继续的位置
        self.zb = "image/xinzhanghao/zhunbei.jpg"  # 点击任意位置继续的位置
        self.sb = "image/xinzhanghao/shibai.jpg"
        self.js = "image/xinzhanghao/jieshu.jpg"
        self.yj = "image/xinzhanghao/yanjing.jpg"
        self.wh = "image/xinzhanghao/wenhao.jpg"
        self.jshou = "image/xinzhanghao/jieshou.jpg"
        self.jxc = "image/xinzhanghao/jiaoxueclose.jpg"
        self.bos = "image/xinzhanghao/boss.jpg"
        self.baox = "image/xinzhanghao/baoxiang.png"
        self.lingj = "image/xinzhanghao/lingjiang.jpg"
        self.sous = "image/xinzhanghao/sousuo.jpg"
        self.zid = "image/xinzhanghao/zidong.jpg"
        self.fhss = "image/xinzhanghao/fanhuisousuo.jpg"
        # 查找图片位置,可信度，默认是1

    def findfigure(self, location, confi=1):
        btnx = 0
        btny = 0
        testbutton = pag.locateOnScreen(location, confidence=confi)
        if testbutton != None:
            btnx, btny = pag.center(testbutton)
        return btnx, btny


    def methodMap(self, method,cofidence):
        if method == "maohao":
            btnx, btny = self.findfigure(self.mh,confi=cofidence)
        elif method == "tiaoguo":
            btnx, btny = self.findfigure(self.tg, confi=cofidence)
        elif method == "jieshou":
            btnx, btny = self.findfigure(self.jshou, confi=cofidence)
        elif method == "jiasu":
            btnx, btny = self.findfigure(self.jias, confi=cofidence)
        elif method == "jixu":
            btnx, btny = self.findfigure(self.jx, confi=cofidence)
        elif method == "xiaoshou":
            btnx, btny = self.findfigure(self.xs, confi=cofidence)
            btny = btny -40
            btnx = btnx -40
        elif method == "queding":
            btnx, btny = self.findfigure(self.qd, confi=cofidence)
        elif method == "zhandou":
            btnx, btny = self.findfigure(self.bos, confi=0.9)
            if btnx <= 0 and btny <= 0:
                btnx, btny = self.findfigure(self.zd, confi=0.9)
        elif method == "zhunbei":
            btnx, btny = self.findfigure(self.zb, confi=cofidence)
        elif method == "shibai":
            btnx, btny = self.findfigure(self.sb, confi=0.8)
            if btnx <= 0 and btny <= 0:
                btnx, btny = self.findfigure(self.js, confi=0.8)
        elif method == "yanjing":
            btnx, btny = self.findfigure(self.yj, confi=cofidence)
        elif method == "wenhao":
            btnx, btny = self.findfigure(self.wh, confi=cofidence)
        elif method == "jiaoxueclose":
            btnx, btny = self.findfigure(self.jxc, confi=cofidence)
        elif method == "boss":
            btnx, btny = self.findfigure(self.bos, confi=0.9)
        elif method == "baoxiang":
            btnx, btny = self.findfigure(self.baox, confi=cofidence)
        elif method == "lingjiang":
            btnx, btny = self.findfigure(self.lingj, confi=cofidence)
        elif method == "sousuo":
            btnx, btny = self.findfigure(self.sous, confi=cofidence)
        elif method == "zidong":
            btnx, btny = self.findfigure(self.zid, confi=cofidence)
        elif method == "fanhuisousuo":
            btnx, btny = self.findfigure(self.fhss, confi=cofidence)
        else:
            return -1, -1
        return btnx, btny

    def findAndClick(self,method_names,confi = 0.8):
        for index,method_name in enumerate(method_names):
            time.sleep(0.2)
            btnx, btny = self.methodMap(method_name,confi)
            if btnx > 0 and btny > 0:
                pag.click(btnx, btny)
                time.sleep(1)
                print("查找%s成功"%method_name)
                if (method_name == "zhandou" or method_name == "boss" )and btnx > 0 and btny > 0:
                    btnx, btny = self.iterFind("zhunbei", confi=0.8, beginInterval=4, iternum=5)
                    if btnx > 0 and btny > 0:
                        pag.click(btnx, btny - 60)
                    btnx, btny = self.iterFind("shibai", confi=0.8, beginInterval=10, iternum=50)
                    if btnx > 0 and btny > 0:
                        pag.click(btnx, btny)
                if method_name == "baoxiang" and btnx > 0 and btny > 0:
                    time.sleep(2)
                    pag.click(btnx, btny+150)
                return 1
        self.find_False_num += 1
        if self.find_False_num >= 4:
            pag.click()
            self.find_False_num = 0
        return -1

    def fubenFindClick(self,method,confi=0.8):
        time.sleep(0.2)
        btnx, btny = self.methodMap(method, confi)
        if btnx > 0 and btny > 0:
            pag.click(btnx, btny)
            return 1
        else:
            return -1

    def iterFind(self, method,confi=0.8, beginInterval=5, iternum=200, iterInterval=0.5):
        btnx = 0
        btny = 0
        # 第一次搜索的时间间隔
        time.sleep(beginInterval)
        # 找到映射的方法，传入string值，得到相应的btnx，btny
        btnx, btny = self.methodMap(method,confi)
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
            btnx, btny = self.methodMap(method,confi)
            iter += 1
            print(btnx, btny)
        print(method + "查找次数", iter)
        # 时间太长了有问题
        if iter == iternum:
            print(method + "查找有问题")
            return -1, -1
        print(method + "查找成功")
        return btnx, btny

    def tansuo(self,item):
        confidence = 0.9
        succ = self.fubenFindClick("sousuo", confi=confidence)
        for i in range(item):
            if succ > 0 :
                # 找到了搜索，进入了副本里
                # 找小怪
                btnx, btny = self.iterFind("zhandou", 1, 3, 10)
                while btnx > 0 or btny > 0 :
                    counter = 0
                    while btnx <= 0 or btny <= 0:
                        btnx, btny = self.iterFind("zhandou", 1, 3, 3)
                        counter += 1
                        print("查找战斗%d次" % (counter))
                    print("查找战斗成功")
                    pag.click(btnx, btny)
                    # 查看是否有自动图标，如果没有证明已经进入到了战斗画面
                    btnx, btny = self.iterFind("zidong", confidence, 3, 10)
                    if btnx > 0 and btny > 0:
                        btnx, btny = self.iterFind("shibai", 0.8, 2, 300)
                        if btnx > 0 and btny > 0:
                            time.sleep(3.5)
                            pag.click(btnx, btny)
                        else:
                            print("未找到结束，程序出错")
                            return
                    btnx, btny = self.iterFind("zhandou", 1, 3, 3)
                baoxx, baoxy = self.iterFind("baoxiang", confidence, 3, 3)
                while baoxx > 0 or baoxy >0 :
                    pag.click(baoxx, baoxy)
                    time.sleep(3.5)
                    pag.click(baoxx + 150, baoxy + 150)
                    baoxx, baoxy = self.iterFind("baoxiang", confidence, 3, 3)

                #  # 反击返回
                # print("搜索返回")
                # fhbtnx,fhbtny = self.iterFind("baoxiang", confidence, 3, 10)
                # if fhbtnx > 0 or fhbtny >0:
                #     pag.click(fhbtnx,fhbtny)
                # else:

            succ = self.fubenFindClick("sousuo", confi=confidence)



    def story(self,item):
        for i in range(item):
            method_names = ["maohao","tiaoguo","jiasu"
                            ,"jixu","xiaoshou","queding"
                            ,"boss","yanjing","wenhao"
                            ,"jieshou","jiaoxueclose","zhandou"
                            ,"baoxiang","lingjiang","shibai"]
            self.findAndClick(method_names)
            print("第%d次迭代"%(i+1))


# story = story()
# story.story(20)

