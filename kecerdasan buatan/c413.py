from matplotlib import pyplot as plt
class VariableFuzzy():

    def __init__(self):
        self.max = 0
        self.min = 0

    def naik(self, x):
        return (x - self.min )/(self.max - self.min)

    def turun(self):
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
            return self.turun(x)
        else:
            return 0

    def steady(self, x):
        # s1-s2 = naik
        if self.s1<=x<=self.s2:
            return self.naik(x)
        # s2-s3 = 1
        elif self.s2<=x<=self.s3:
            return 1
        # s3-s4 = turun
        elif self.s2<=x<=self.s3:
            return self.turun(x)
        else:
            return 0
    
    def fast(self, x):
        # s3-s4 = naik
        # s4-... = 1
        if x > self.s4:
            return 1
        elif self.s3<=x<=self.s4:
            return self.naik(x)
        else:
            return 0

    def graph(self, x=None):
        # slow
        plt.figure(figsize=(20, 10), dpi=80)
        # 0=>s1 [1]
        # s1=>s2 [down]
        # s2=>...[0]
        x_low = [0, self.s1, self.s2, self.sn]
        y_low = [1, 1, 0, 0]
        plt.plot(x_low, y_low, label='low')
        # steady
        # 0=>s1 [0]
        # s1=>s2 [up]
        # s2=>s3 [1]
        # s3=>s4 [down]
        # s4=>...[0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0 ]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0=>s3 [0]
        # s3=>s4 [up]
        # s4=>...[1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1 ]
        plt.plot(x_fast, y_fast, label='fast')

        plt.legend(loc="upper left")
        plt.show()
