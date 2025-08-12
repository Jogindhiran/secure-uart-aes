# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 12:20:35 2025

@author: Jogindhiran
"""

import tkinter as tk
import serial
from Crypto.Cipher import AES

# ---------- CONFIGURATION ----------
AES_KEY = b'TestKey123456789'  # Must match STM32 key
PORT = 'COM5'                  # Replace with your STM32 COM port
BAUD_RATE = 115200             # Must match STM32 baud rate

# ---------- ENCRYPTION ----------
def encrypt_command(command):
    padded = command.ljust(16, '_')[:16].encode()  # Pad or trim to 16 bytes
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(padded)
    return encrypted

# ---------- UART ----------
def send_encrypted_command(command):
    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser:
            encrypted_data = encrypt_command(command)
            ser.write(encrypted_data)
            print(f"Sent: {command}")
    except serial.SerialException:
        print("Could not open serial port. Is STM32 connected?")

# ---------- GUI ----------
def create_gui():
    root = tk.Tk()
    root.title("Encrypted LED Command Sender")
    root.geometry("300x200")

    tk.Label(root, text="Select LED Command", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="LED ON", width=20, command=lambda: send_encrypted_command("LED_ON")).pack(pady=5)
    tk.Button(root, text="LED OFF", width=20, command=lambda: send_encrypted_command("LED_OFF")).pack(pady=5)
    tk.Button(root, text="LED BLINK", width=20, command=lambda: send_encrypted_command("LED_BLINK")).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
