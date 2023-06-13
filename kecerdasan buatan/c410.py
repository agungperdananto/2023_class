# pip install matplotlib
from matplotlib import pyplot as plt

class BaseFuzzy():

    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum )/ (self.maximum - self.minimum)
    def down(self, x):
        return (self.maximum - x)/ (self.maximum - self.minimum)

class Speed(BaseFuzzy):

    def __init__(self):
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 200

    def slow(self, x):
        #  0 -s1 = 1
        # s1 - s2 = down
        if x < self.s1:
            return 1 
        elif self.s1<=x<=self.s2:
            self.maximum = self.s2
            self.minimum=self.s1
            return self.down(x)
        else:
            return 0

    def steady(self, x):
        # s1-s2 = up
        # s2-s3 = 1
        # s3-s4 = down
        if self.s1 <= x <= self.s2:
            self.maximum = self.s2
            self.minimum=self.s1
            return self.up(x)
        elif self.s2 <= x <= self.s3:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum=self.s3
            return self.down(x)
        else:
            return 0

    def fast(self, x):
        # s3 - s4 = up
        # s4 - .... = 1
        if x > self.s4:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum=self.s3
            return self.up(x)
        else: 
            return 0
 
    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        # slow
        # 0 - s1 = 1 [1, 1]
        # s1 - s2 = down [1, 0]
        # s2 - sn = 0 [0, 0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')
        # steady
        # 0-s1 = 0 [0, 0]
        # s1-s2 = up [0, 1]
        # s2-s3 = 1 [1, 1]
        # s3-s4 = down [1, 0]
        # s4-sn = 0 [0, 0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0 - s3 = [0, 0]
        # s3 - s4 = up [0, 1]
        # s4 - sn = 1 [1, 1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')

        if value:
            slow_value = self.slow(value)
            steady_value = self.steady(value)
            fast_value = self.fast(value)
            x_param = [0, value, value]
            # slow
            y_slowvalue = [slow_value, slow_value, 0]
            plt.plot(x_param, y_slowvalue, label='slow value')
            # steady
            y_steadyvalue = [steady_value, steady_value, 0]
            plt.plot(x_param, y_steadyvalue, label='steady value')
            # fast
            y_fastvalue = [fast_value, fast_value, 0]
            plt.plot(x_param, y_fastvalue, label='fast value')

        plt.legend(loc='upper right')
        plt.show()


class Pressure(BaseFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 22
        self.p4 = 27
        self.p5 = 30
        self.p6 = 40
        self.p7 = 50
        self.p8 = 55
        self.p9 = 60

    def graph(self):
        # very low
        # 0-p1 = 1
        # p1-p3 = down
        # low
        # p2-p3 = up
        # p3-p4 = down
        # medium
        # p3-p5 = up
        # p5-p6 = 1
        # p6 - p7= down
        # high
        # p6 - p7= up
        # p7-p9 = down
        # very high
        # p8-p9 = up
        # p9-...=1
        pass

speed = Speed()
x = 92
print('slow', speed.slow(x))
print('steady', speed.steady(x))
print('fast', speed.fast(x))

speed.graph(x)