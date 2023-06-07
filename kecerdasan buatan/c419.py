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
        self.tn = 80

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
    
    def graph(self):
        plt.figure(figsize=(15, 10))
        # freeze
        # 0 - t1 = 1 [1, 1]
        # t1 - t2 = down[1, 0]
        # t2- tn = 0 [0, 0]
        x_freeze = [0, self.t1, self.t2, self.tn]
        y_freeze = [1, 1, 0, 0]
        plt.plot(x_freeze, y_freeze, label='freeze')
        # cold
        # 0 - t1 = 0 [0, 0] 
        # t1 - t2 = up [0, 1]
        # t2 - t3 = down [1, 0]
        # t3 - tn = 0 [0, 0]
        x_cold = [0, self.t1, self.t2, self.t3, self.tn]
        y_cold = [0, 0, 1, 0, 0]
        plt.plot(x_cold, y_cold, label='cold')
        # warm
        # hot
        plt.legend(loc='upper right')
        plt.show()

temp = Temp()
x = 18
print('freeze', temp.freeze(x))
print('cold', temp.cold(x))
print('warm', temp.warm(x))
print('hot', temp.hot(x))

temp.graph()
