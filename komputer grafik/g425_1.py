# github.com/agungperdananto/2023_class

from matplotlib import pyplot as plt

x = [100, 120, 100, 100]
y = [10, 0, 0, 10]

x1 = [ x_ + 10 for x_ in x]
y1 = y

plt.figure(figsize=(20, 10), dpi=80)

# plt.plot(x, y)
# plt.plot(x1, y1)

# object1 
x_obj = [100, 120, 110, 110, 125, 125, 100, 100]
y_obj = [100, 100, 50, 20, 100, 110, 110, 100]

x_obj1 = [x + 10 for x in x_obj]
y_obj1 = [y - 10 for y in y_obj]

# plt.plot(x_obj, y_obj)
# plt.plot(x_obj1, y_obj1)

def fungsi(x):
    return x**2

x_line = [i for i in range(-10, 11)]
y_line = [fungsi(x) for x in x_line]

print('x', x_line)
print('y', y_line)

plt.plot(x_line, y_line)

plt.show()