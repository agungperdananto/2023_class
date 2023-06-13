# pip install matplotlib

from matplotlib import pyplot as plt

class BaseFuzzy():

    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)
    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

class Speed(BaseFuzzy):

    def __init__(self):
        self.s1 = 20
        self.s2 = 40
        self.s3 = 60
        self.s4 = 80
        self.sn = 100

    def slow(self, x):
        # 0 - s1 = 1
        # s1 - s2 = down
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.down(x)
        else:
            return 0
    def steady(self, x):
        # s1 - s2 = up
        # s2 - s3 = 1
        # s3 - s4 = down
        if self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.up(x)
        if self.s2 <= x <= self.s3:
            return 1
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.down(x)
        else:
            return 0
    def fast(self, x):
        # s3 - s4 =up
        # s4 - ... = 1
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.up(x)
        elif x > self.s4:
            return 1
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
        # s1 - s2 = up [0, 1]
        # s2 - s3 = 1 [1, 1]
        # s3 - s4 = down [1, 0]
        # s4-sn = 0[0, 0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0 - s3 = 0 [0, 0]
        # s3 - s4 =up [0, 1]
        # s4 - sn = 1 [1, 1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')
        
        if value:
            value_slow = self.slow(value)
            value_steady = self.steady(value)
            value_fast = self.fast(value)
            x_param = [0, value, value]
            # slow
            y_slowvalue = [value_slow, value_slow, 0]
            plt.plot(x_param, y_slowvalue, label='slow value')
            # steady
            y_steadyvalue = [value_steady, value_steady, 0]
            plt.plot(x_param, y_steadyvalue, label='steady value')
            # fast
            y_fastvalue = [value_fast, value_fast, 0]
            plt.plot(x_param, y_fastvalue, label='fast value')
            

        plt.legend(loc='upper right')
        plt.show()

class Pressure(BaseFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 27
        self.p7 = 32
        self.p8 = 37
        self.p9 = 40

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
x = 72
print('slow', speed.slow(x))
print('steady', speed.steady(x))
print('fast', speed.fast(x))

speed.graph(x)