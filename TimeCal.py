import time as t


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
        self.begin = t.localtime()
        self.prompt = "请先stop"
        print("计时开始")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("请先进行")
        else:
            self.end = t.localtime()
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

