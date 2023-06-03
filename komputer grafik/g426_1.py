# github.com/agungperdananto/2023_class

from matplotlib import pyplot as plt
x = [100, 150, 200, 220, 120, 100]
y = [100, 100, 150, 110, 110, 100]

x2 = [i + 20 for i in x]
y2 = y

x3 = [i - 20 for i in x]
y3 = [i + 20 for i in y]

plt.figure(figsize=(20, 10), dpi=80)

def fungsi_2(x):
    return x**2

def fungsi_3(x):
    return x*3

x_line = [x for x in range(100)]
y_line = [fungsi_2(x) for x in x_line]

# plt.plot(x_line, y_line)
plt.plot(x, y)
plt.plot(x2, y2)
plt.plot(x3, y3, color=[255/255, 182/255, 110/255])
plt.show()


