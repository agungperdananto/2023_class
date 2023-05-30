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
    def cold():
        # t1 - t2 = up
        # t2 - t3 = down
        pass
    def warm():
        # t2 - t3 = up
        # t3 - t4 = down
        pass
    def hot():
        # t3 - t4 = up
        # t4-.... = 1
        pass
