# 💻 2025 Spring – Embedded Systems @ NTUEE

Welcome to the official lab repository for the **NTUEE Embedded Systems course (Spring 2025)**.  
This course involves hands-on embedded programming using STM32, Mbed OS, RTOS, BLE, and Linux-based tools.


## 🧪 Lab Overview

### 🔴 Lab 1: LED Blinking & RTOS API
- Handle user button interrupts (single tap / long press)
- Use a periodic timer callback
- Control LEDs with CMSIS OS and GPIO settings


### 📡 Lab 2: Wi-Fi & Sensor Data
- Connect to Wi-Fi and transmit LSM6DSL accelerometer data over TCP
- Visualize data on the host device
- Enable significant motion detection to trigger alerts via interrupts


### 🔗 Lab 3: BLE Central (RPi)
- Set up a Raspberry Pi as a BLE Central device
- Connect to a mobile BLE testing app
- Modify CCCD to configure notification behavior


### 🔁 Lab 4: BLE Peripheral (STM32) + Central (RPi)
- STM32 as BLE GATT server, RPi as client
- RPi writes to CCCD to set sampling frequency
- STM32 sends sensor data via notification; RPi prints it to screen

> 📁 Python code: `hw4-rpi-client.py`  
> ⚙️ STM32 code in accompanying files


### ⚙️ Lab 5: PWM & Logic Analyzer
- Use timers to generate PWM signals
- Analyze signal output via logic analyzer through Arduino-compatible headers


### 🌡️ Lab 6: Data Acquisition, DMA & Interrupt

**Part 1: Interrupt Mode**
- Timer triggers ADC read of on-board temperature sensor
- Data printed via UART

**Part 2: DMA Mode**
- ADC samples automatically
- DMA stores data in memory buffer
- DMA interrupt triggers UART output when buffer is half/full

---

### 📊 Lab 7: CMSIS-DSP Programming
- Apply a 3Hz low-pass FIR filter to z-axis accelerometer data
- Utilize ARM CMSIS-DSP math library for signal processing


## 👨‍💻 Maintainers

**NTU_student: R12525093 Yen-Yu Liu**  
**NTU_student: R13525042 Tsung-Kuang Liao**

---

Thanks for visiting this repository. Happy coding and good luck with embedded development!
