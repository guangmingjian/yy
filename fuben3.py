import pyautogui as pag
import time
import os
import random
import ctypes, sys
import closegame as cg
import BasicMethod as BM
BM.cgflag = True
pag.PAUSE = 0.01
fight_n = 100
pag.FAILSAFE = False
endIter = 300
# 每次默认等待的时间
defaultInterval = 0.1
# 每次迭代查找的时间间隔
interval = 0.001
# 从战斗到准备的时间间隔
fight_prepare_interval = 0.2
# 开始战斗的时间间隔
beginfightInterval = 0.2
# 战斗时间
fight_time =0.1
maxrand = 5
zhandouimgLoc = "image/fuben/zhandou.png"
imgroot2 = "image/"
imgroot1 = "image/fuben/"
imgtype = ".png"
gouliangcounter = 0
huanliang = 50

def one_guai_fight(btnx, btny):
    # 查找战斗
    # zhandoulist = [imgroot1 + "zhandou" + imgtype,imgroot1 + "boss" + imgtype]
    # btnx, btny = BM.iterfindpiclist(zhandoulist, confi=0.8, internaltime=0.1, mosttime=endIter)
    # btnx, btny = BM.iterfindpic(imgroot1 + "zhandou" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)

    # btnx = 941 + random.randint(-maxrand - 30, maxrand + 30)
    # btny = 569 + random.randint(0, 20)
    # time.sleep(counter%2)
    # print("移动结束")
    # time.sleep(0.8)
    pag.click(btnx, btny, duration=0.01)
    # BM.jiancha(imgroot1 + "zhandou" + imgtype, 0.8, btnx, btny, 0.3)
    # 换狗粮
    global  gouliangcounter
    gouliangcounter = gouliangcounter + 1
    print("**************************第" +str(gouliangcounter) +"个狗粮***********************")
    if gouliangcounter % huanliang == 0:
        time.sleep(20)
        # pag.click(574+ random.randint(-5,5),569)
        #
        # time.sleep(2)
        # pag.click(62 + random.randint(-5,5),754 + random.randint(-5,5))
        # btnx, btny = BM.iterfindpic(imgroot1 + "sucai" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
        # pag.click(btnx, btny+ random.randint(-5,5), duration=0.01)
        #
        #
        #
        # btnx, btny = BM.iterfindpic(imgroot1 + "gouliang" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
        # pag.moveTo(btnx, btny, duration=0.01)
        # pag.dragTo(658, 455, duration=0.5)
        # time.sleep(0.5)
        # btnx, btny = BM.iterfindpic(imgroot1 + "gouliang" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)
        # pag.moveTo(btnx, btny, duration=0.01)
        # pag.dragTo(184, 418, duration=0.5)
        # btnx, btny = BM.iterfindpic(imgroot1 + "gouliangfanhui" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
        # pag.click(btnx, btny + random.randint(-5, 5), duration=0.01)
        # time.sleep(1)



    btnx, btny = BM.iterfindpic(imgroot2 + "zhunbei" + imgtype, confi=1, internaltime=0.1, mosttime=endIter)
    pag.click(btnx, btny, duration=0.01)

    BM.jiancha(imgroot2 + "zhunbei" + imgtype, 1, btnx, btny, 1)

    # 开始查找胜利
    btnx, btny = BM.iterfindpic(imgroot2 + "shengli" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)
    if btnx == -1 or btny == 0:
        print("未找到胜利，程序结束")
        return False
    btnx = btnx + random.randint(-maxrand - 10, maxrand + 10)
    btny = btny + random.randint(-maxrand, maxrand)
    pag.moveTo(btnx, btny)
    # time.sleep((counter+1) % 2)
    pag.click(btnx, btny, duration=0.2)
    pag.click(btnx, btny, duration=0.2)

    # 查找结束标志
    btnx, btny = BM.iterfindpic(imgroot2 + "dianjijixu" + imgtype, confi=0.8, internaltime=0.1, mosttime=endIter)

    btnx = 941 + random.randint(-maxrand - 30, maxrand + 30)
    btny = 569 + random.randint(0, 20)
    # time.sleep(counter%2)
    print("移动结束")
    time.sleep(0.8)
    pag.click(btnx, btny, duration=0.2)

    BM.jiancha(imgroot2 + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.4)
    print("点击结束")


def one_sousuo():
    # 查找战斗
    zhandoulist = [ imgroot1 + "boss" + imgtype,imgroot1 + "zhandou" + imgtype]
    btnx, btny = BM.iterfindpiclist(zhandoulist, confi=0.8, internaltime=0.1, mosttime=10)
    while btnx > 0:
        one_guai_fight(btnx, btny)


        print("打完一个小怪")
        btnx, btny = BM.iterfindpiclist(zhandoulist, confi=0.8, internaltime=0.01, mosttime=2)
        if btnx < 1:
            print("**********************需要移动")
            pag.moveTo(1266-random.randint(0,10),600,duration=0.1)
            pag.dragTo(50+random.randint(0,10),600-random.randint(0,10), 0.4,button='left')
            # pag.mouseDown(button="left")
            # pag.moveTo(1000-random.randint(0,10),10)
            # pag.mouseUp()
            btnx, btny = BM.iterfindpiclist(zhandoulist, confi=0.8, internaltime=0.1, mosttime=2)

    print("已经无怪，一次探索结束")
    time.sleep(2)
    btnx,btny = BM.iterfindpic(imgroot1 + "baoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=10)
    while btnx > 0:
        pag.click(btnx,btny)
        time.sleep(2)
        pag.click(50+random.randint(0,10),600-random.randint(0,10))
        btnx, btny = BM.iterfindpic(imgroot1 + "baoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=10)


    # btnx, btny = BM.iterfindpiclist(zhandoulist, confi=0.8, internaltime=0.1, mosttime=40)

# def fanhuisousuo():

def fight():

    for i in range(fight_n):
        #大宝箱
        print("搜索大宝箱")
        btnx, btny = BM.iterfindpic(imgroot1 + "dabaoxiang" + imgtype, confi=0.8, internaltime=0.1, mosttime=3)
        if btnx > 0:
            pag.click(btnx + random.randint(-5, 5), btny + random.randint(-5, 5))
            time.sleep(5)
            pag.click(385+random.randint(-5,5),398+random.randint(-5,5))
            time.sleep(2)
        print("搜索地域鬼王")
        # 如果在找到地域鬼王，说明未在搜索界面
        btnx, btny = BM.iterfindpic(imgroot1 + "digui" + imgtype, confi=0.8, internaltime=0.1, mosttime=3)
        if btnx > 0 :
            print("点击第二十八章")
            pag.click(1180 + random.randint(-10,10),670 + random.randint(-5,5))
            time.sleep(1)

        btnx, btny = BM.iterfindpic(imgroot1 + "sousuo" + imgtype, confi=0.8, internaltime=0.1, mosttime=5)
        if btnx > 0:
            print("点击搜索")
            pag.click(btnx + random.randint(-10, 10), btny + random.randint(-5, 5))

        btnx, btny = BM.iterfindpic(imgroot1 + "queding" + imgtype, confi=0.8, internaltime=0.1, mosttime=5)
        if btnx > 0:
            print("点击搜索")
            pag.click(btnx + random.randint(-10, 10), btny + random.randint(-5, 5))

        one_sousuo()
        print("第" + str(i+1) + "次探索结束")
        print("还有" + str(fight_n - i -1)+ "次")
    time.sleep(2)
    print("全部结束，关闭游戏")
    cg.closegame()


fight()









