from matplotlib import pyplot as plt
import numpy as np

# plt.figure(figsize=(15, 10))

fig, (ax_sin, ax_cos, ax_circle) = plt.subplots(3, 1, sharex=False)

x = np.linspace(0, 2, 100)
ysin = np.sin(x)
ycos = np.cos(x)
ytan = np.tan(x)
y_flat = np.linspace(0.25, 0.25, 100)


ax_sin.plot(x, ysin,  color='C0')
ax_sin.plot(x, ytan, color='C2')
ax_sin.fill_between(x, ysin, ytan, color='C1', alpha=0.3)

ax_cos.plot(x, ycos, color='C1')
ax_cos.plot(x, y_flat, color='C0')
ax_cos.fill_between(x, ycos, y_flat, color='C0', alpha=0.3)

circle = np.linspace(0, 2 * np.pi, 150)

x_circle = 0.5 * np.sin(circle)
y_circle = 0.5 * np.cos(circle)

ax_circle.plot(x_circle, y_circle)
ax_circle.fill_between(x_circle, y_circle, color='C0', alpha=0.3)

plt.show()