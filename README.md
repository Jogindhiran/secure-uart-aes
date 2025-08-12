# Secure UART Command Interface with AES Encryption
## Overview
This project demonstrates a secure communication interface between a Python GUI and an STM32 microcontroller over UART, using the AES-128 encryption algorithm. It is designed to showcase both embedded systems programming and Python-based GUI development for secure data exchange.
## Features
• AES-128 Encryption & Decryption for UART commands  
• Python Tkinter GUI for sending encrypted commands  
• Command parsing logic on STM32 to execute actions  
• Example commands:  
  • LED_BLINK – Blink onboard LED  
  • Extendable for other ECU-style commands  
## Project Structure
Core/           # STM32CubeIDE source files (Inc, Src, Startup)  
Drivers/        # HAL and CMSIS drivers  
Python/         # Python GUI script  
AES_UART_Config.ioc  # STM32CubeMX configuration file  
## Hardware and Software Requirements
• Hardware:  
  • STM32F446 Nucleo or similar board  
  • USB-UART connection  
• Software:  
  • STM32CubeIDE  
  • Python 3 with pyserial and tkinter  
  • STM32 HAL libraries  
## How to run?
1. Flash the STM32 firmware generated in Core/ and Drivers/ using STM32CubeIDE.
2. Run the Python GUI
3. Select the COM port and send commands.
