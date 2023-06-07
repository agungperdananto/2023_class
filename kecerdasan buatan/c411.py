# pip install matplotlib
from matplotlib import pyplot as plt

class BaseFuzzy():

    def __init__(self):
        self.maximum = 0
        self.minimum = 0
    
    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)
    
    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)

class Speed(BaseFuzzy):

    def __init__(self):
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 200
    
    def slow(self, x):
        # 0 - s1 = 1
        # s1- s2 = down
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.down(x)
        else:
            return 0
    def steady(self, x):
        # s1- s2 = up
        # s2- s3 = 1
        # s3- s4 = down
        if self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.up(x)
        elif self.s2 <= x <= self.s3:
            return 1
        elif self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.down(x)
        else:
            return 0
    def fast(self, x):
        # s3- s4 = up
        # s4 - ..... =1
        if x > self.s4:
            return 1
        elif self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.up(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        # slow
        # 0 - s1 = 1 [1, 1]
        # s1- s2 = down [1, 0]
        # s2-sn = 0 [0, 0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')

        # steady
        # 0-s1 = 0 [0-0]
        # s1- s2 = up [0-1]
        # s2- s3 = 1 [1-1]
        # s3- s4 = down [1-0]
        # s4- sn = 0 [0-0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0-s3 = 0 [0-0]
        # s3- s4 = up [0-1]
        # s4 - sn =1 [1-1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')
        if value:
            x_param = [0, value, value]
            y_slow = self.slow(value)
            y_steady = self.steady(value)
            y_fast = self.fast(value)
            y_param_slow = [y_slow, y_slow, 0]
            y_param_steady = [y_steady, y_steady, 0]
            y_param_fast = [y_fast, y_fast, 0]
            plt.plot(x_param, y_param_slow, label='slow value')
            plt.plot(x_param, y_param_steady, label='steady value')
            plt.plot(x_param, y_param_fast, label='fast value')


        plt.legend(loc='upper right')
        plt.show()

class Temp(BaseFuzzy):

    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0
        self.t4 = 0
    
    def freeze():
        pass
    def cold():
        pass
    def warm():
        pass
    def hot():
        pass


speed = Speed()

x = 83
print('slow', speed.slow(x))
print('steady', speed.steady(x))
print('fast', speed.fast(x))

speed.graph(x)

