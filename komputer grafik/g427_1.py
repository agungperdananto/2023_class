from matplotlib import pyplot as plt

# x = [0, 100, 100, 0]
# y = [100, 200, 300, 100]

x = [x_ for x_ in range( -5, 20)]
y = [y_**2 for y_ in x]

x_1 = [x_ for x_ in range( -5, 20)]
y_1 = [y_**2 + 20 for y_ in x_1]

x_a = [10, 20, 10, 15, 25, 25, 10, 10]
y_a = [100, 100, 50, 50, 100, 110, 110, 100]

x_b = [ x + 10 for x in x_a]
y_b = [y - 10 for y in y_a]
 
# plt.plot(x, y)
# plt.plot(x_1, y_1)
plt.plot(x_a, y_a)
plt.plot(x_b, y_b)
plt.show()

# github.com/agungperdananto/2023_class