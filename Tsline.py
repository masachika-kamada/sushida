import matplotlib.pyplot as plt
import numpy as np
import math

initial = 0.02176
first = 0.2361
second = 0.2
dx = 0.001
x1 = np.arange(initial, initial + first, dx)
x2 = np.arange(initial + first, initial + first + second, dx)
x3 = np.arange(initial, initial + first + second, dx)

y1 = 1120.78 * math.e ** ((x1 - initial) / 0.718)
y2 = 1557.14 * math.e ** ((x2 - initial - first) / 1.005)
y3 = 370 * math.e ** ((x3 - initial) / 0.718)

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 0.5)
ax.set_ylim(0, 2000)

ax.vlines(x=initial, ymin=370, ymax=1120.78, colors='blue')
ax.vlines(x=initial + first + second, ymin=679.18, ymax=1900, colors='blue')

plt.plot(x1, y1, color='blue')
plt.plot(x2, y2, color='blue')
plt.plot(x3, y3, color='blue')

# plt.axvline(x=initial)
# plt.axvline(x=initial + first + second)  # , ymin=679.18, ymax=1900

plt.show()
plt.savefig("Ts.png")
