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
        pass
    
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

        
