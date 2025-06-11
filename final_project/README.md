# 🌟 Motion-Triggered UART Notification Project

**🎯 STM32L4S5VIT6 + SR505 PIR + FreeRTOS + USART1**

## ✨ Project Overview

This project uses an SR505 passive infrared sensor (PIR) to detect motion. When someone is continuously detected in front of the sensor for 3 seconds, the STM32L4S5VIT6 microcontroller sends a UART message `"start\n"` to a PC or Raspberry Pi using a USB-TTL adapter. Perfect for building a smart trash bin or an automatic door!

## 🔌 Hardware Connections

| Component        | STM32 Pin         | Notes                         |
|------------------|-------------------|-------------------------------|
| **SR505 PIR**    | VCC → 5V          | External power (optional)     |
|                  | GND → GND         | Common ground                 |
|                  | OUT → PA0         | GPIO Input                    |
| **LED Indicator**| PB0 → LED → GND   | 220Ω resistor (optional)      |
| **USART1**       | PA9 (TX) → USB-TTL RX / Pi GPIO15 (RXD) | TX only needed for debug |
|                  | PA10 (RX) ← USB-TTL TX / Pi GPIO14 (TXD) | Optional, not used here |
|                  | GND → USB-TTL GND / Pi GND | Ground reference |

## 🗂️ Software Structure

📂 **Src/**  
- `main.c`: Main application, FreeRTOS tasks  
- `hc_sr505.c`: SR505 sensor GPIO logic  
- `usart.c`: UART initialization and printf retarget  

📂 **Inc/**  
- `hc_sr505.h`: SR505 header  
- `usart.h`: UART header  

## 🚀 How to Build & Test

1. Open the `.ioc` file in STM32CubeIDE and **Generate Code**  
2. Build the project and **flash** it to your board  
3. Connect the hardware as shown above  
4. Open PuTTY or `minicom` at **115200 baud**, 8 data bits, no parity, 1 stop bit, no flow control  
5. You should see `"Hello World\n"` or `"start\n"` messages when motion is detected!  


