from matplotlib import pyplot as plt
import numpy as np

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

x_c = [0, 10, 20, 30]
y_c = [10, 20, 30, 10]
y_flat = [10, 10, 10 , 10]
 
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

ax1.plot(x_c, y_c, color='C0')
ax1.plot(x_c, y_flat, color='C1')

ax1.fill_between(x_c, y_flat, y_c)

# ax1.fill_between(x_b, y_b, y_a, color='C0')

x = np.linspace(0, 10, 20)
y_sin = np.sin(x)
y_cos = np.cos(x)

ax2.plot(x, y_sin, color='C5')
ax3.plot(x, y_cos, color='C1')

plt.show()

# github.com/agungperdananto/2023_class