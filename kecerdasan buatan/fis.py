from matplotlib import pyplot as plt

class BaseFuzzy():
    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum )/ (self.maximum - self.minimum)
    def down(self, x):
        return (self.maximum - x)/ (self.maximum - self.minimum)
# def down(x, xmin, xmax):
#     return (xmax - x) / (xmax - xmin)

# def up(x, xmin, xmax):
#     return (x - xmin) / (xmax - xmin)

class Permintaan(BaseFuzzy):

    def __init__(self):
        self.p1 = 2100
        self.p2 = 3500
        self.pn = 4000
    def turun(self, x):
        if x >= self.p2:
            return 0
        elif x<= self.p1:
            return 1
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.down(x)

    def naik(self, x):
        if x >= self.p2:
            return 1
        elif x<= self.p1:
            return 0
        else:
            self.maximum = self.p2
            self.minimum = self.p1
            return self.up(x)
    
    def graph(self, ax, value=None):
        # turun
        x = [0, self.p1, self.p2, self.pn]
        y_trn = [1, 1, 0, 0]
        ax.plot(x, y_trn, label='turun')
        # naik
        y_naik = [0, 0, 1, 1]
        ax.plot(x, y_naik, label='naik')

class Persediaan():

    def __init__(self):
        self.p1 = 100
        self.p2 = 250
        self.pn = 300

    def sedikit(self, x):
        if x >= self.p2:
            return 0
        elif x<= self.p1:
            return 1
        else:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.down(x)

    def banyak(self, x):
        if x >= self.p2:
            return 1
        elif x<= self.p1:
            return 0
        else:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.up(x)
        
    def graph(self, ax, value=None):
        # sedikit
        x = [0, self.p1, self.p2, self.pn]
        y_sdk = [1, 1, 0, 0]
        ax.plot(x, y_sdk, label='sedikit')
        # banyak
        y_byk = [0, 0, 1, 1]
        ax.plot(x, y_byk, label='banyak')


class Produksi():
    minimum = 1000
    maximum = 5000
    permintaan = 0
    persediaan = 0

    def __init__(self):
        self.p1 = 1000
        self.p2 = 5000
        self.pn = 6000
        self.permintaan = 0
        self.persediaan = 0

    def _berkurang(self, a):
        return self.p2 - a*(self.p2 - self.p1)

    def _bertambah(self, a):
        return a*(self.p2 - self.p1) + self.p1

    def _inferensi(self, pmt=Permintaan(), psd=Persediaan()):
        result = []
        # [R1] JIKA Permintaan TURUN, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        z1 = self._berkurang(a1)
        result.append((a1, z1))
        # [R2] JIKA Permintaan TURUN, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERKURANG.
        a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        z2 = self._berkurang(a2)
        result.append((a2, z2))
        # [R3] JIKA Permintaan NAIK, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERTAMBAH.
        a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        z3 = self._bertambah(a3)
        result.append((a3, z3))
        # [R4] JIKA Permintaan NAIK, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        z4 = self._bertambah(a4)
        result.append((a4, z4))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a
    
    def graph(self):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
        pmt = Permintaan()
        psd = Persediaan()

        pmt.graph(ax1)
        psd.graph(ax2)
         # sedikit
        x = [0, self.p1, self.p2, self.pn]
        y_sdk = [1, 1, 0, 0]
        ax3.plot(x, y_sdk, label='berkurang')
        # banyak
        y_byk = [0, 0, 1, 1]
        ax3.plot(x, y_byk, label='bertambah')

        plt.show()

produksi = Produksi()
produksi.graph()