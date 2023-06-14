# pip install matplotlib

from matplotlib import pyplot as plt

class BaseFuzzy():

    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)
    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)

class Temp(BaseFuzzy):

    def __init__(self):
        self.t1 = 5
        self.t2 = 10
        self.t3 = 20
        self.t4 = 50
        self.tn = 60

        self.red = [1, 0, 0]
        self.blue = [0, 0, 1]
        self.green = [0, 1, 0]
        self.yellow = [255/255, 214/255, 155/255]

    def freeze(self, x):
        # 0 - t1 = 1
        # t1 - t2 = down
        if x < self.t1:
            return 1
        elif self.t1 <= x <= self.t2:
            self.minimum = self.t1
            self.maximum = self.t2
            return self.down(x)
        else:
            return 0
    def cold(self, x):
        # t1 - t2 = up
        # t2 - t3 = down
        if self.t1 <= x <= self.t2:
            self.minimum = self.t1
            self.maximum = self.t2
            return self.up(x)
        elif self.t2 <= x <= self.t3:
            self.minimum = self.t2
            self.maximum = self.t3
            return self.down(x)
        else:
            return 0
    def warm(self, x):
        # t2 - t3 = up
        # t3 - t4 = down
        if self.t2 <= x <= self.t3:
            self.minimum = self.t2
            self.maximum = self.t3
            return self.up(x)
        elif self.t3 <= x <= self.t4:
            self.minimum = self.t3
            self.maximum = self.t4
            return self.down(x)
        else:
            return 0
    def hot(self, x):
        # t3 - t4 = up
        # t4-.... = 1
        if self.t3 <= x <= self.t4:
            self.minimum = self.t3
            self.maximum = self.t4
            return self.up(x)
        elif x > self.t4:
            return 1
        else:
            return 0
    
    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        # freeze
        # 0 - t1 = 1 [1, 1]
        # t1 - t2 = down[1, 0]
        # t2- tn = 0 [0, 0]
        x_freeze = [0, self.t1, self.t2, self.tn]
        y_freeze = [1, 1, 0, 0]
        plt.plot(x_freeze, y_freeze, label='freeze', color=self.blue)
        # cold
        # 0 - t1 = 0 [0, 0] 
        # t1 - t2 = up [0, 1]
        # t2 - t3 = down [1, 0]
        # t3 - tn = 0 [0, 0]
        x_cold = [0, self.t1, self.t2, self.t3, self.tn]
        y_cold = [0, 0, 1, 0, 0]
        plt.plot(x_cold, y_cold, label='cold', color=self.green)
        # warm
        # 0 - t2 = 0 [0, 0]
        # t2 - t3 = up [0, 1]
        # t3 - t4 = down [1, 0]
        # t4 - tn = 0 [0, 0]
        x_warm = [0, self.t2, self.t3, self.t4, self.tn]
        y_warm = [0, 0, 1, 0, 0]
        plt.plot(x_warm, y_warm, label='warm', color=self.yellow)
        # hot
        # 0 - t3 = 0 [0, 0]
        # t3 - t4 = up [0, 1]
        # t4 - tn = 1 [1, 1]
        x_hot = [0, self.t3, self.t4, self.tn]
        y_hot = [0, 0, 1, 1]
        plt.plot(x_hot, y_hot, label='hot', color=self.red)

        if value:
            x_param = [0, value, value]
            freeze_value = temp.freeze(value)
            cold_value = temp.cold(value)
            warm_value = temp.warm(value)
            hot_value = temp.hot(value)
            # freeze
            y_freeze_values = [freeze_value, freeze_value, 0]
            plt.plot(x_param, y_freeze_values, label='freeze value', color=self.blue)
            # cold
            y_cold_values = [cold_value, cold_value, 0]
            plt.plot(x_param, y_cold_values, label='cold value', color=self.green)
            # warm
            y_warm_values = [warm_value, warm_value, 0]
            plt.plot(x_param, y_warm_values, label='warm value', color=self.yellow)
            # hot
            y_hot_values = [hot_value, hot_value, 0]
            plt.plot(x_param, y_hot_values, label='hot value', color=self.red)

        plt.legend(loc='upper right')
        plt.show()


class Pressure(BaseFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 8
        self.p3 = 15
        self.p4 = 20
        self.p5 = 28
        self.p6 = 30
        self.p7 = 37
        self.p8 = 40
        self.p9 = 47

    def very_low(self, x):
        # 0-p1 = 1
        # p1-p3 = down
        pass

    def low(self, x):
        # p2-p3 = up
        # p3-p4 = down
        pass
    def medium(self, x):
        # p3 - p4=up
        # p4-p5 = 1
        # p6-p7 = down
        pass
    def high(self, x):
        # p5-p8 = up
        # p8 - p9 = down
        pass
    def very_high(self, x):
        # p8 - p9 = up
        # p9-...= 1
        pass
        
    def graph(self, x):
        # very low
        # 0-p1 = 1
        # p1-p3 = down
        # low
        # p2-p3 = up
        # p3-p4 = down
        # medium
        # p3 - p4=up
        # p4-p5 = 1
        # p6-p7 = down
        # high
        # p5-p8 = up
        # p8 - p9 = down
        # very high
        # p8 - p9 = up
        # p9-...= 1
        pass


temp = Temp()
x = 43
print('freeze', temp.freeze(x))
print('cold', temp.cold(x))
print('warm', temp.warm(x))
print('hot', temp.hot(x))

temp.graph(x)
