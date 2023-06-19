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
        self.pn = 80

        self.color = {
            'very_low': 'C0',
            'low': 'C1',
            'medium': 'C2',
            'high': 'C3',
            'very_high': 'C4',
        }
        self.default = 'C5'
    
    def very_low(self, x):
        # 0-p1 = 1
        # p1-p2 = down
        if x < self.p1:
            return 1
        elif self.p1<=x<=self.p2:
            self.min = self.p1
            self.max = self.p2
            return self.turun(x)
        else:
            return 0

    def low(self, x):
        # p1-p2=up
        # p2-p4=down
        if self.p1<=x<=self.p2:
            self.min = self.p1
            self.max = self.p2
            return self.naik(x)
        elif self.p2<=x<=self.p4:
            self.min = self.p2
            self.max = self.p4
            return self.turun(x)
        else:
            return 0

    def medium(self, x):
        # p3-p5 = up
        # p5-p6 =1
        # p6-p7 = down
        if self.p3<=x<=self.p5:
            self.min = self.p3
            self.max = self.p5
            return self.naik(x)
        elif self.p5<=x<=self.p6:
            return 1
        elif self.p6<=x<=self.p7:
            self.min = self.p6
            self.max = self.p7
            return self.turun(x)
        else:
            return 0

    def high(self, x):
        # p6-p8 = up
        # p8-p9 = down
        if self.p6<=x<=self.p8:
            self.min = self.p6
            self.max = self.p8
            return self.naik(x)
        elif self.p8<=x<=self.p9:
            self.min = self.p8
            self.max = self.p9
            return self.turun(x)
        else:
            return 0


    def very_high(self, x):
        # p8-p9 = up
        # p9-...=1
        if x > self.p9:
            return 1
        elif self.p8<=x<=self.p9:
            self.min = self.p8
            self.max = self.p9
            return self.naik(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 5))
        # very low
        # 0-p1 = 1
        # p1-p2 = down
        # p2-pn = 0
        x_v_low = [0, self.p1, self.p2, self.pn]
        y_v_low = [1, 1, 0, 0]
        plt.plot(x_v_low, y_v_low, label='very low', color=self.color.get('very_low', self.default))
        # low
        # 0-p1 = 0
        # p1-p2 = up
        # p2-p4 = down
        # p4-pn = 0
        x_low = [0, self.p1, self.p2, self.p4, self.pn]
        y_low = [0, 0, 1, 0, 0]
        plt.plot(x_low, y_low, label='low', color=self.color.get('low', self.default))
        # medium
        # 0-p3 = 0
        # p3-p5 = up
        # p5-p6 =1
        # p6-p7 = down
        # p7-pn = 0
        x_medium = [0, self.p3, self.p5, self.p6, self.p7, self.pn]
        y_medium = [0, 0, 1, 1, 0, 0]
        plt.plot(x_medium, y_medium, label='medium', color=self.color.get('medium', self.default))
        # high
        # 0-p6 = 0
        # p6-p8 = up
        # p8-p9 = down
        # p9-pn = 0
        x_low = [0, self.p6, self.p8, self.p9, self.pn]
        y_low = [0, 0, 1, 0, 0]
        plt.plot(x_low, y_low, label='high', color=self.color.get('high', self.default))
        # very high
        # 0-p8 = 0
        # p8-p9 = up
        # p9-pn = 1
        x_fast = [0, self.p8, self.p9, self.pn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='very high', color=self.color.get('very_high', self.default))
        if value:
            x_param = [0, value, value]
            y_v_low = self.very_low(value)
            y_low = self.low(value)
            y_medium = self.medium(value)
            y_high = self.high(value)
            y_v_high = self.very_high(value)

            y_param_v_low = [y_v_low, y_v_low, 0]
            y_param_low = [y_low, y_low, 0]
            y_param_medium = [y_medium, y_medium, 0]
            y_param_high = [y_high, y_high, 0]
            y_param_v_high = [y_v_high, y_v_high, 0]


            plt.plot(x_param, y_param_v_low, label='very low value', color=self.color.get('very_low', self.default))
            plt.plot(x_param, y_param_low, label='low value', color=self.color.get('low', self.default))
            plt.plot(x_param, y_param_medium, label='medium value', color=self.color.get('medium', self.default))
            plt.plot(x_param, y_param_high, label='high value', color=self.color.get('high', self.default))
            plt.plot(x_param, y_param_v_high, label='very high value', color=self.color.get('very_high', self.default))
        
        plt.legend(loc = 'upper right')
        plt.show()



# speed = Speed()
# x = 85
# print('slow', speed.slow(x))
# print('steady', speed.steady(x))
# print('fast', speed.fast(x))
# speed.graph(x)

preassure = Preassure()
x = 16
print('very low', preassure.very_low(x))
print('low', preassure.low(x))
print('medium', preassure.medium(x))
print('high', preassure.high(x))
print('very high', preassure.very_high(x))

preassure.graph(x)
