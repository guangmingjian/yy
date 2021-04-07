import pyautogui as pag
import time
import random
import closegame as cg
import os
maxiter = 1500
defaultconfi = 0.8
cgflag = False
ir = "image/"
pt = ".png"

get_pic_loc = lambda img_root,cs,pic_type: os.path.join(img_root, cs + pic_type)

def get_jieshu_axis(rand=True):
    btnx,btny = 1297,742
    if rand:
        btnx, btny = btnx + random.randint(- 10, 10), btny + random.randint(-5, 5)
    return btnx, btny


def close_game(num):
    if num >= maxiter and cgflag:
        print("关闭游戏")
        cg.closegame()


# 找到任务
def renwu():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/renwu.png', confidence=defaultconfi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        pag.click(btnx, btny, duration=0.2)
        print("寻找任务成功")
    else:
        print("无任务")
    return btnx, btny


# 找到任务
def baoxiang():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/fuben/baoxiang.png', confidence=defaultconfi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        pag.click(btnx, btny, duration=0.2)
        print("寻找宝箱成功")
        time.sleep(2)
        pag.click()
    else:
        print("无任务")
    return btnx, btny


def shengliandjieshu(mostiter):
    # 开始查找胜利
    itertime = 0
    imgroot = "image/"
    imgtype = ".png"
    maxrand = 5
    shengliflag = True
    # pag.moveTo(1802, 951 + random.randint(-5, 5), duration=0.01)
    while itertime < mostiter:
        if shengliflag:
            btnx, btny = findpic(imgroot + "shengli" + imgtype, confi=0.8)
            if btnx > 0:
                btnx = 1200 + random.randint(-maxrand - 10, maxrand + 10)
                btny = 700 + random.randint(-maxrand, maxrand)
                pag.moveTo(btnx, btny)
                # time.sleep((counter+1) % 2)
                pag.doubleClick(btnx, btny, duration=0.1)
                time.sleep(0.3)
                pag.doubleClick(btnx, btny, duration=0.1)
                print("移动结束")
                time.sleep(0.3)
                pag.doubleClick(btnx, btny, duration=0.1)
                time.sleep(0.5)
                pag.doubleClick(btnx, btny, duration=0.1)
                jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                time.sleep(0.5)
                jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                time.sleep(0.5)
                jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                return True
                # shengliflag = False

        # 查找结束标志
        btnx, btny = findpic(imgroot + "dianjijixu" + imgtype, confi=0.8)
        if btnx > 0:
            btnx = 1200 + random.randint(-maxrand - 30, maxrand + 30)
            btny = 700 + random.randint(0, 20)
            # time.sleep(counter%2)
            print("移动结束")
            time.sleep(0.2)
            pag.click(btnx, btny, duration=0.2)
            jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            time.sleep(0.5)
            jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            time.sleep(0.5)
            jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            return True
        pag.doubleClick(1263 + random.randint(-5, 5), 736, duration=0.01)
        # if itertime % 5 ==0:
        #     pag.moveTo(1802,951+random.randint(-5,5),duration=0.01)
        close_game(itertime)
    return False


# 找到teamviewer确定
def tmqueding():
    btnx = 0
    btny = 0
    testbutton = pag.locateOnScreen('image/tmqueding.png', confidence=defaultconfi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        pag.click(btnx, btny, duration=0.2)
        print("寻找teamviewer确定成功")
    else:
        print("无teamviewer确定")
    return btnx, btny


def findpic(loc, confi):
    renwu()
    # tmqueding()
    btnx = 0
    btny = 0
    if confi == 1:
        testbutton = pag.locateOnScreen(loc)
    else:
        testbutton = pag.locateOnScreen(loc, confidence=confi)
    if testbutton != None:
        btnx, btny = pag.center(testbutton)
        print(loc + "   已经找到    ")
    else:
        print(loc + "   没有找到    ")
    return btnx, btny


def jiancha(loc, confi, x, y, internal=1):
    btnx, btny = findpic(loc, confi)
    counter = 0
    while (btnx > 0):
        time.sleep(internal)
        pag.moveTo(x + random.randint(-10, 10), y + random.randint(-5, 5))
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        print("检查" + loc)
        pag.click(duration=0.2)
        print("页面没跳转，继续点击")
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1
    print("页面已经跳转")


#
def jianchanoclick(loc, confi, internal=0.2):
    """
    直到查到结束，否则一直循环。消失后返回
    :param loc:
    :param confi:
    :param internal:
    :return:
    """
    btnx, btny = findpic(loc, confi)
    counter = 0
    while btnx == 0 and btny == 0:
        time.sleep(internal)
        print("页面停留，在等待.....")
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1
    print("页面已经跳转")


def jianchaandclick(loc, confi, x, y, internal=1):
    """
    直到查到某一标志，否则继续点击
    :param loc:
    :param confi:
    :param internal:
    :return:
    """
    btnx, btny = findpic(loc, confi)
    counter = 0
    pag.doubleClick(x + random.randint(-5, 5), y + random.randint(-5, 5), duration=0.2)
    while btnx == 0 and btny == 0:
        time.sleep(internal)
        print("未检查到：" + loc)
        print("双击: {} {}...".format(x,y))
        pag.doubleClick(x + random.randint(-5, 5), y + random.randint(-5, 5),duration=0.2)
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1
    print("页面已经跳转")


def jianchatoapper(loc, confi, internal=0.5):
    btnx, btny = findpic(loc, confi)
    counter = 0
    while btnx == 0 and btny == 0:
        time.sleep(internal)
        print("页面停留，在等待.....")
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1
    print("页面已经跳转")

def jianchatodis(loc, confi, internal=0.5):
    btnx, btny = findpic(loc, confi)
    counter = 0
    while btnx > 0 and btny > 0:
        time.sleep(internal)
        print("页面停留，在等待.....")
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1
    print("页面已经跳转")


def jianchari(loc, confi, x, y, internal=1):
    btnx, btny = findpic(loc, confi)
    counter = 0
    while (btnx == 0):
        time.sleep(internal)
        pag.moveTo(x + random.randint(), y + random.randint(-10, 10))
        # if counter > 0:
        #    time.sleep((counter - 1) % 2)
        print("检查" + loc)
        pag.click(duration=0.2)
        print("页面没跳转，继续点击")
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1

    print("页面已经跳转")


def iterfindpic(loc, confi, internaltime, mosttime):
    btnx, btny = findpic(loc, confi)
    counter = 0
    while btnx == 0:
        print("iterfindpic: 无 " + loc)
        time.sleep(internaltime)
        counter += 1
        if counter > mosttime:
            print("迭代寻找  " + loc + "  失败 ")
            return 0, 0
        btnx, btny = findpic(loc, confi)
        close_game(counter)
        counter += 1

    print("迭代寻找  " + loc + "  成功 ")
    return btnx, btny


def iterfindpiclist(loc_list, confi, internaltime, mosttime):
    for i in range(mosttime):
        time.sleep(internaltime)
        for loc in loc_list:
            btnx, btny = findpic(loc, confi)
            if btnx == 0:
                print("iterfindpic: 无 " + loc)
                print("共寻找" + str(i) + "次")
                print("迭代寻找  " + loc + "  失败 ")
            else:
                print("迭代寻找  " + loc + "  成功 ")
                return btnx, btny
    return 0, 0


# def jianchalist(loc_list, confi,x,y,internal=1):
#     while True:
#         for loc in loc_list:
#             btnx,btny = findpic(loc,confi)
#             if btnx == 0:
#                 print("iterfindpic: 无 "+loc)
#
#                 print("迭代寻找  " + loc + "  失败 ")
#             else:
#                 print("迭代寻找  " +loc + "  成功 ")
#                 return  btnx, btny
#     return 0,0
#
#     counter = 0
#     while (btnx > 0):
#
#         time.sleep(internal)
#         pag.moveTo(x+random.randint(-10,10),y+random.randint(-5,5))
#         # if counter > 0:
#         #    time.sleep((counter - 1) % 2)
#         print("检查"+loc)
#         pag.click(duration=0.2)
#         print("页面没跳转，继续点击")
#         btnx, btny = findpic(loc, confi)
#         close_game(counter)
#         counter += 1
#
#
#     print("页面已经跳转")


def guiwangshengliandjieshu(mostiter):
    # 开始查找胜利
    itertime = 0
    imgroot = "image/"
    imgtype = ".png"
    maxrand = 5
    shengliflag = True
    # pag.moveTo(1802, 951 + random.randint(-5, 5), duration=0.01)
    while itertime < mostiter:
        if shengliflag:
            btnx, btny = findpic(imgroot + "shengli" + imgtype, confi=0.8)
            if btnx > 0:
                btnx = 1200 + random.randint(-maxrand - 10, maxrand + 10)
                btny = 700 + random.randint(-maxrand, maxrand)
                pag.moveTo(btnx, btny)
                # time.sleep((counter+1) % 2)
                pag.doubleClick(btnx, btny, duration=0.1)
                # time.sleep(0.3)
                # pag.doubleClick(btnx, btny, duration=0.1)
                # print("移动结束")
                # time.sleep(0.3)
                # pag.doubleClick(btnx, btny, duration=0.1)
                # time.sleep(0.5)
                # pag.doubleClick(btnx, btny, duration=0.1)
                # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                # time.sleep(0.5)
                # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                # time.sleep(0.5)
                # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
                # return True
                # shengliflag = False

        # 查找结束标志
        btnx, btny = findpic(imgroot + "dianjijixu" + imgtype, confi=0.8)
        if btnx > 0:
            btnx = 1200 + random.randint(-maxrand - 30, maxrand + 30)
            btny = 700 + random.randint(0, 20)
            # time.sleep(counter%2)
            print("移动结束")
            time.sleep(0.8)
            pag.doubleClick(btnx, btny, duration=0.2)
            pag.doubleClick(btnx, btny, duration=0.2)
            btnx1, btny1 = findpic("image/jiejietupo/queding.png", confi=0.8)
            if btnx1 > 0:
                pag.click(btnx1, btny1, duration=0.001)
                return True

            pag.doubleClick(btnx, btny, duration=0.2)
            pag.doubleClick(btnx, btny, duration=0.2)

            btnx1, btny1 = findpic("image/jiejietupo/queding.png", confi=0.8)
            if btnx1 > 0:
                pag.click(btnx1, btny1, duration=0.001)
                return True
            print("点击结束")
            time.sleep(0.8)
            pag.doubleClick(btnx, btny, duration=0.2)

            btnx1, btny1 = findpic("image/jiejietupo/queding.png", confi=0.8)
            if btnx1 > 0:
                pag.click(btnx1, btny1, duration=0.001)
                return True
            print("点击结束")
            # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            # time.sleep(0.5)
            # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            # time.sleep(0.5)
            # jiancha(imgroot + "dianjijixu" + imgtype, 0.8, btnx, btny, 0.2)
            return True
        pag.doubleClick(1263 + random.randint(-5, 5), 736, duration=0.01)
        # if itertime % 5 ==0:
        #     pag.moveTo(1802,951+random.randint(-5,5),duration=0.01)
        close_game(itertime)
    return False


def new_shengli():
    x,y = get_jieshu_axis(False)
    jianchaandclick(get_pic_loc(ir,"jieshu",pt), 1, x - random.randint(0,50), y, 1)
    # 返回了说明找到了结束
    time.sleep(1)
    jiancha(get_pic_loc(ir,"jieshu",pt),1,x,y,0.5)