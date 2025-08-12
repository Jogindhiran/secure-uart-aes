# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 11:34:31 2025

@author: Jogindhiran
"""

from Crypto.Cipher import AES

key = b'TestKey123456789'  # 16-byte key
cipher = AES.new(key, AES.MODE_ECB)

cmd = b'LED_OFF_________'  # 16 bytes
encrypted_data = cipher.encrypt(cmd)

print(encrypted_data.hex())

with open("led_off_encrypted.bin", "wb") as f:
    f.write(encrypted_data)

