import matplotlib.pyplot as plt
import serial

x, y = [], []  # 描画データ
CNT = 200      # 受信（＝描画）回数

fig, ax = plt.subplots()
lines, = ax.plot(x, y)

ax.set_xlim((0, CNT))
ax.set_ylim((0, 3000))

com = serial.Serial('COM7', 9600, timeout=100)
for i in range(CNT):
    res = com.read(1)
    n = int.from_bytes(res, 'little')
    print(res, n)
    x.append(i)
    y.append(n)
    lines.set_data(x, y)

    plt.pause(0.01) # これが重要！

com.close()