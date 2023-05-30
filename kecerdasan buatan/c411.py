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

