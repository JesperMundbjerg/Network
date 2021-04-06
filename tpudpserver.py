# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:00:59 2021

@author: Jespe
"""
import socket
import time
import struct
import sys

script, port = sys.argv

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int(port)       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    while True:
        _, addr = s.recvfrom(8)

        print('Connected by', addr)
        t_1_jan_1970 = 2_208_988_800
        time_stamp = t_1_jan_1970 + int(time.time())
        data = struct.pack('>I', time_stamp) #pack data with big endian (>) as 32-bit unsigned integer (I)

        s.sendto(data, addr)