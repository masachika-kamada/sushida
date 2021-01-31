import matplotlib.pyplot as plt
import numpy as np

dx = 1
x = np.arange(0, 250, dx)
x_1 = np.arange(70, 250, dx)
x_2 = np.arange(0, 170, dx)
x_3 = np.arange(0, 110, dx)
x_4 = np.arange(0, 120, dx)

y_1 = 2033000/(x_1*x_1)
y_2 = 2498000/(7500+x_2*x_2)
y_3 = 304-1.119*x_3
y_4 = 333-0.0136*x_4*x_4

plt.plot(x_1, y_1, label="y1")
plt.plot(x_2, y_2, label="y2")
plt.plot(x_3, y_3, label="y3")
plt.plot(x_4, y_4, label="y4")
plt.legend()
plt.show()
