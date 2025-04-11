# scan_and_connect_ble.py
from bluepy.btle import Scanner, DefaultDelegate, Peripheral, UUID

class MyScanDelegate(DefaultDelegate):
    def __init__(self):
        super().__init__()

    def handleDiscovery(self, device, is_new, has_new_data):
        if is_new:
            print("New device found:", device.addr)
        elif has_new_data:
            print("Updated device:", device.addr)

# 初始化掃描器並設定委派類別
scanner = Scanner().withDelegate(MyScanDelegate())
print("Scanning for BLE devices...")
scan_results = scanner.scan(10.0)

device_addresses = []
for idx, device in enumerate(scan_results):
    print(f"{idx}: Device {device.addr} ({device.addrType}), RSSI={device.rssi} dB")
    device_addresses.append(device.addr)
    for (ad_type, description, val) in device.getScanData():
        print(f" {description} = {val}")

# 選擇要連接的裝置
choice = input("Select device index to connect: ")
selected_index = int(choice)
selected_addr = device_addresses[selected_index]
print("Selected device address:", selected_addr)

# 建立連線
print("Attempting to connect...")
peripheral = Peripheral(selected_addr, 'random')

try:
    print("Retrieving services...")
    service = peripheral.getServiceByUUID(UUID(0xfff0))

    print("Available characteristics:")
    for char in service.getCharacteristics():
        print(f" - {char}")

    # 讀取 characteristic 0xfff1
    char1 = peripheral.getCharacteristics(uuid=UUID(0xfff1))[0]
    if char1.supportsRead():
        print("0xfff1 value:", char1.read())

    # 讀取 characteristic 0xfff2
    char2 = peripheral.getCharacteristics(uuid=UUID(0xfff2))[0]
    if char2.supportsRead():
        print("0xfff2 value:", char2.read())

    # 開始等待通知
    print("Waiting for notifications on 0xfff2...")
    while True:
        if peripheral.waitForNotifications(1.0):
            print("Notification received:", char2.read().decode('utf-8'))
            break
        else:
            print("Still waiting...")

finally:
    print("Disconnecting...")
    peripheral.disconnect()
