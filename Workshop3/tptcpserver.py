# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:01:50 2021

@author: Jespe
"""
#!/usr/bin/env python3

import socket
import time
import struct
import sys

script, port = sys.argv

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int(port)       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            t_1_jan_1970 = 2_208_988_800
            time_stamp = t_1_jan_1970 + int(time.time())
            data = struct.pack('>I', time_stamp) #pack data with big endian (>) as 32-bit unsigned integer (I)

            conn.send(data)