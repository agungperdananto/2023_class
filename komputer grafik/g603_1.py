from matplotlib import pyplot as plt

x = [100, 150, 150, 200, 200, 100, 100]
y = [100, 100, 150, 120, 80, 80, 100]

def duplicate(x, y, num_x=0, num_y=0):
    x_ = [i + num_x for i in x]
    y_ = [i + num_y for i in y]
    return x_, y_

plt.figure(figsize=(20, 10))
plt.plot(x, y)
new_x, new_y = duplicate(x, y, 20, -10)
plt.plot(new_x, new_y)
new_x1, new_y1 = duplicate(x, y, -20, 20)
plt.plot(new_x1, new_y1)
plt.show()









# github.com/agungperdananto/2023_class