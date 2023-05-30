# List []
list1 = [1,2,3,4,5,6,7]
# tuple ()
tuple1 = (1,2,3,4,5,6,7)
# dictionary {key: value}
dict1 = {'name': 'Iwan', 'nilai': 80}

# print(list1)
# print('index 2:', list1[2])
# print(tuple1)
# print('index 2:', tuple1[2])
# print(dict1)
# print('name', dict1['name'])

def linear(x):
    return 2 * x

def garis(max):
    return [linear(x) for x in range(max)]