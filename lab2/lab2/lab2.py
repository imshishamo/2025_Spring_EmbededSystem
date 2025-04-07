import socket
import matplotlib.pyplot as plt
import time

HOST = '0.0.0.0'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Listening on", (HOST, PORT))

conn, addr = s.accept()
print("Connected by", addr)

plt.ion()  # 開啟互動模式
fig, ax = plt.subplots()
x_vals, y_vals, z_vals = [], [], []
line_x, = ax.plot([], [], label='X')
line_y, = ax.plot([], [], label='Y')
line_z, = ax.plot([], [], label='Z')
ax.legend()

while True:
    data = conn.recv(1024)
    if not data:
        break
    text = data.decode().strip()
    # 假設格式是 "ACC X=123, Y=-45, Z=678"
    # 這裡要先解析字串，取出 X/Y/Z 數值
    try:
        # 簡易解析示範
        parts = text.replace("ACC ","").split(",")
        x_str = parts[0].split("=")[1]
        y_str = parts[1].split("=")[1]
        z_str = parts[2].split("=")[1]
        x_val = float(x_str)
        y_val = float(y_str)
        z_val = float(z_str)
        # 加到序列中
        x_vals.append(x_val)
        y_vals.append(y_val)
        z_vals.append(z_val)

        # 即時更新圖表
        line_x.set_xdata(range(len(x_vals)))
        line_x.set_ydata(x_vals)
        line_y.set_xdata(range(len(y_vals)))
        line_y.set_ydata(y_vals)
        line_z.set_xdata(range(len(z_vals)))
        line_z.set_ydata(z_vals)

        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)
    except:
        pass

conn.close()
