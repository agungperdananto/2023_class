# List []
l1 = [1, 2, 3, 4, 5, 6]
# Tuple ()
t1 = [11, 12, 13, 14, 15, 16]
# Dictionary {key: value}
d1 ={'name': 'Dudi'}

# print(l1)
# print('index ke 2 list', l1[2])
# print(t1)
# print('index ke 2 tuple', t1[2])
# print(d1)
# print('nama', d1['name'])

def fungsi(x):
    return 2 * x

def garis(num):
    return [fungsi(x) for x in range(num)]


data_siswa = [
    {'name': 'Dudi', 'nilai':88, 'hadir':13},
    {'name': 'Ferry', 'nilai':70, 'hadir':12},
    {'name': 'Angga', 'nilai':60, 'hadir':14},
    {'name': 'Rita', 'nilai':75, 'hadir':14},
    {'name': 'Ricky', 'nilai':77, 'hadir':12},
    {'name': 'Panji', 'nilai':64, 'hadir':11},
              ]

def cetak_nilai(data, max_hadir=14):
    # presentase kehadiran masing2 siswa = hadir/max * 100, default=14
    # rata2 keseluruhan nilai jumlah nilai/ jumlah siswa
    # total nilai masing2 siswa absensi 20% nilai 80%
    total_nilai = 0
    for siswa in data:
        presentase_kehadiran = round(siswa['hadir']/max_hadir * 100, 2)
        print(
            'Nama:', siswa['name'],
            'kehadiran:', presentase_kehadiran, '%',
            'total nilai:', round(siswa['nilai'] * 0.8 + presentase_kehadiran * 0.2, 2)
        )
        total_nilai += siswa['nilai']
    print('Rata2 nilai:', round(total_nilai/len(data), 2))

cetak_nilai(data_siswa)
