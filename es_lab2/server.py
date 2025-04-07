import socket
import json
import time
import matplotlib.pyplot as plt

# 伺服器 IP & PORT
HOST = '192.168.50.54'  # 請確保這是你的電腦 IP
PORT = 5000  # 確保 STM32 設定的 Port 是相同的

# 設定 TCP 伺服器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"✅ Server started. Listening on {HOST}:{PORT}")

# 等待 STM32 連線（加入超時提示）
server_socket.settimeout(5)  # 每 5 秒檢查一次
while True:
    try:
        print("⌛ Waiting for STM32 connection...")
        conn, addr = server_socket.accept()
        print(f"🎉 Connected by STM32 device: {addr}")
        break
    except socket.timeout:
        print("⏳ Still waiting for STM32... (Make sure STM32 is trying to connect)")
    
# Matplotlib 初始化
plt.ion()  # 互動模式
fig, ax = plt.subplots()

# 儲存數據
accel_data = {"x": [], "y": [], "z": []}

while True:
    try:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            print("❌ STM32 connection lost.")
            break

        print(f"📩 Received: {data}")

        # 修正可能的 JSON 格式錯誤
        try:
            obj = json.loads(data)
        except json.JSONDecodeError:
            print("⚠️ JSON Decode Error: 跳過這筆數據")
            continue

        # 儲存數據
        accel_data["x"].append(obj.get('x', 0))
        accel_data["y"].append(obj.get('y', 0))
        accel_data["z"].append(obj.get('z', 0))

        # 繪製即時圖
        ax.clear()
        ax.plot(accel_data["x"], label="X-Axis", color='blue')
        ax.plot(accel_data["y"], label="Y-Axis", color='red')
        ax.plot(accel_data["z"], label="Z-Axis", color='green')
        ax.legend()
        plt.xlabel("Time")
        plt.ylabel("Acceleration")
        plt.title("Real-time Accelerometer Data from STM32")
        plt.grid(True)
        plt.draw()
        plt.pause(0.1)

    except Exception as e:
        print(f"❌ Error: {e}")
        break

print("🚪 Closing connection...")
conn.close()
server_socket.close()
