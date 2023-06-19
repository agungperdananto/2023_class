from matplotlib import pyplot as plt

x = [0, 2, 4]
y = [0, 8, 0]

# naik 2 = x-0/2-0 * 4
# x= 1
# trapesium
x1 = [0, 0.5, 3.5, 4]
y1 = [0, 2, 2, 0]
y0 = [0, 0, 0, 0]

# flat

plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x1, y0, 'o--')

plt.fill_between(x1, y1, y0)
plt.show()