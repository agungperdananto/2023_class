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
        pass
    
    def slow(self, x):
        # 0-s1 = 1
        if x < s1:
            return 1
        # s1-s2 = turun
        elif s1<=x<=s2:
            return self.turun(x)
        else:
            return 0

    def steady(self):
        # s1-s2 = naik
        # s2-s3 = 1
        # s3-s4 = turun
        pass
    
    def fast(self):
        # s3-s4 = naik
        # s4-... = 1
        pass
