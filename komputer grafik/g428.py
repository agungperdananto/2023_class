# contoh code 

# list []
l1 = [1,2,3,4,5,6]
# tuple ()
t1 = (10, 11, 12, 13)
# dictionary {key: value}
d1 ={'name': 'Rudi', 'nilai': 75}


# print(l1)
# print('index ke 2:', l1[2])
# print(t1)
# print('index ke 2:', t1[2])
# print(d1)
# print('nama: ', d1['name'])

def graph1(x):
    return x ** 2 + 2 * x

def get_data(num):
    return [graph1(i) for i in range(num)]

# print(graph1(12))

# data1 = [graph1(i) for i in range(100)]
# print(data1)

data_siswa = [
    {'name': 'Rudi', 'nilai': 75, 'kehadiran':12},
    {'name': 'Imam', 'nilai': 80, 'kehadiran':14},
    {'name': 'Rita', 'nilai': 60, 'kehadiran':10},
    {'name': 'Indra', 'nilai': 85, 'kehadiran':14},
    {'name': 'Ferry', 'nilai': 90, 'kehadiran':12}
    ]

def hitung_nilai(data, max_kehadiran=14):
    # rata2 nilai
    # masing2 presentase kehadiran (max_kehadiran)
    nilai_total = 0
    for item in data:
        print('nama: ', item['name'], 'kehadiran:', round(item['kehadiran']/max_kehadiran * 100, 2), '%')
        nilai_total += item['nilai']
    print('nilai rata2:', round(nilai_total/len(data), 2))

# hitung_nilai(data_siswa)