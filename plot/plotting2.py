from matplotlib import pyplot as plt

# low
# 0 - 50 = 1
# 50 - 100 1=>0
plt.figure(figsize=(20, 10), dpi=80)
x_low = [0, 50, 100]
y_low = [1, 1, 0]
plt.plot(x_low, y_low, label='low')
# medium
# 50 - 100 0=>1
# 100-150 1=>1
# 150-200 1=>0 
x_medium = [50, 100, 150, 200]
y_medium = [0, 1, 1, 0]
plt.plot(x_medium, y_medium, label='medium')
# high
# 150-200 0=>1
# 200-250 1=>0
x_high = [150, 200, 250]
y_high = [0, 1, 0]
plt.plot(x_high, y_high, label='high')
# extreme
# 200-250 0=>1
# 250-500 1=>1
x_extreme = [200, 250, 400]
y_extreme = [0, 1, 1]

plt.plot(x_extreme, y_extreme, label='extreme')

# # x high value 
# # 220-200/250-200 = 0.4
# x_hvalue = [0, 220, 220]

# y_hvalue = [0.4, 0.4, 0]
# plt.plot(x_hvalue, y_hvalue, label='x[high]')

# # x extreme value
# # 250 - 220/250-200 = 0.6
# x_xvalue = [0, 220, 220]
# y_xvalue = [0.6, 0.6, 0]
# plt.plot(x_xvalue, y_xvalue, label='x[extreme]')

# x = 70
# medium up
# low down

# low 
# max - x / max - min
# 100 - 70/100-50 = 30/50 = 0.6

x_lowv = [70, 70, 0]
y_lowv = [0, 0.6, 0.6]

plt.plot(x_lowv, y_lowv)
plt.legend(loc="upper left")
plt.show()