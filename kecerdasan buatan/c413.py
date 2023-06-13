# pip install matplotlib
from matplotlib import pyplot as plt

class VariableFuzzy():

    def __init__(self):
        self.max = 0
        self.min = 0

    def naik(self, x):
        return (x - self.min )/(self.max - self.min)

    def turun(self, x):
        return (self.max - x)/(self.max - self.min)

class Speed(VariableFuzzy):

    def __init__(self):
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 200
    
    def slow(self, x):
        # 0-s1 = 1
        if x < self.s1:
            return 1
        # s1-s2 = turun
        
        elif self.s1<=x<=self.s2:
            self.min = self.s1
            self.max = self.s2
            return self.turun(x)
        else:
            return 0

    def steady(self, x):
        # s1-s2 = naik
        if self.s1<=x<=self.s2:
            self.min = self.s1
            self.max = self.s2
            return self.naik(x)
        # s2-s3 = 1
        elif self.s2<=x<=self.s3:
            return 1
        # s3-s4 = turun
        elif self.s3<=x<=self.s4:
            self.min = self.s3
            self.max = self.s4
            return self.turun(x)
        else:
            return 0
    
    def fast(self, x):
        # s3-s4 = naik
        # s4-... = 1
        if x > self.s4:
            return 1
        elif self.s3<=x<=self.s4:
            self.min = self.s3
            self.max = self.s4
            return self.naik(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 5))
        # slow
        # 0-s1 = 1 [1=>1]
        # s1-s2 = down[1=>0]
        # s2- ... [0=>0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')
        # steady
        # 0-s1  => 0[0-0]
        # s1-s2 =>up[0-1]
        # s2-s3 => 1 [1-1]
        # s3-s4 => down [1-0]
        # s4-sn = > 0 [0-0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0-s3 =>0[0-0]
        # s3-s4 => up[0-1]
        # s4-sn => 1[1-1]
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
            plt.plot(x_param, y_param_slow, label='slow_value')
            plt.plot(x_param, y_param_steady, label='steady_value')
            plt.plot(x_param, y_param_fast, label='fast_value')


        plt.legend(loc = 'upper left')
        plt.show()


class Preassure(VariableFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 28
        self.p7 = 35
        self.p8 = 40
        self.p9 = 70
        
    def graph(self):
        # very low
        # 0-p1 = 1
        # p1-p2 = down
        # low
        # p1-p2=up
        # p2-p4=down
        # medium
        # p3-p5 = up
        # p5-p6 =1
        # p6-p7 = down
        # high
        # p6-p8 = up
        # p8-p9 = down
        # very high
        # p8-p9 = up
        # p9-...=1
        pass


speed = Speed()
x = 85
print('slow', speed.slow(x))
print('steady', speed.steady(x))
print('fast', speed.fast(x))
speed.graph(x)
        
