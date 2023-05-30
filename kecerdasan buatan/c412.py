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