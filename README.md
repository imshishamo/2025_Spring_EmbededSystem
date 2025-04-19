# 2025_Spring_EmbededSystem
The repository for the NTUEE embedded system labs course.

### Lab 1: LED blinking and RTOS API
This lab incorporates the basics of user interrupt, CMSIS OS and GPIO configuration to perform different behaviors under the three scenarios:
1. User button single tap.
2. User button long press.
3. A fixed-interval timer callback.

### Lab 2: Wifi and Sensor data
This lab focuses on the Wifi and the LSM6DSL modules. The accelerometer sensor values are continously transmitted to a host in the local network by TCP connection and then visualized at the host. In addition, the significant motion function is enabled in the LSM6DSL module. An interrupt is implemented to send a unique signal to the host when such events are detected.

### Lab 3: BLE programming
In this lab, a BLE central is established on a RPI to communicate with the BLE testing app on a phone. The server also supports setting the CCCD value on the client side.

### Lab 4: BLE Programming
This lab inherits parts of code in Lab 3 -- using RPi as a BLE client. Also, a STM32 is used as a BLE server. The RPi builds the connection and write a CCCD value of the server to assign a sampling frequency. Then, STM32 notifies RPi with the sensor values. Rpi then print the value on screen.

The Python file is named as 'hw4-rpi-client.py' under the folder, and all the remaining files are for STM32.

### Lab 5: PWM and Logic Analyzer
In this lab, we use a built-in timer as a counter and PWM generator. The generated waveform is then passed to a logic analyzer via the Arduino connector on board.

### Lab 6: Data Acquisition, DMA, and Interrupt
- 6-1: Use a timer to generate interrupts. When an interrupt arrives, the ADC read the value of the on-board temperature sensor and prints out its value to computer via UART.
- 6-2: Instead of using a timer, in this part, we use DMA instead. ADC automatically read values at a fixed rate, and DMA store the value to a designated address in the memory. When the array provided for DMA is full/half-full, DMA generates an interrupt to inform the other thread. The thread then prints the values stored in the array to computer via UART.

### Lab 7: CMSIS-DSP programming
This lab aims to utilize the DSP functions provided by the arm math library. A 3Hz low-pass filter is applied to the z-axis data from the accelero to demostrate the usage of the fir function.
