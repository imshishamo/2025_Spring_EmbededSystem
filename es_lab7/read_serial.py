import serial
import matplotlib.pyplot as plt

input_data = []
filtered_data = []

# 請根據實際情況修改 COM port
ser = serial.Serial('COM3', 115200, timeout=1)
print("Reading from serial port... Press Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if ',' in line:
            parts = line.split(',')
            if len(parts) == 2:
                try:
                    input_val = float(parts[0])
                    filtered_val = float(parts[1])
                    input_data.append(input_val)
                    filtered_data.append(filtered_val)
                    print(f"Input: {input_val:.2f}, Filtered: {filtered_val:.2f}")
                except ValueError:
                    continue
except KeyboardInterrupt:
    ser.close()
    print("\nSerial port closed. Now plotting...")

    # 畫圖
    plt.figure(figsize=(12, 6))
    plt.plot(input_data, label='Original Input')
    plt.plot(filtered_data, label='Filtered Output')
    plt.legend()
    plt.title('Sensor Data (Input vs Filtered)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    # 存成 CSV
    with open('output_data.csv', 'w') as f:
        f.write('Input,Filtered\n')
        for i, f_val in zip(input_data, filtered_data):
            f.write(f"{i},{f_val}\n")
    print("Data saved to output_data.csv!")
