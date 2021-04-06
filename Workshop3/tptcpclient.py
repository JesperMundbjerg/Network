# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:21:40 2021

@author: Jespe
"""
#!/usr/bin/env python3

import socket
import struct
import time
import sys

script, serverhost, port = sys.argv

HOST = serverhost  # The server's hostname or IP address
PORT = int(port)        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    data = s.recv(4) #receive 32 bits of data
    
    time_stamp = struct.unpack('>I', data) #unpack data with big endian (>) as 32-bit unsigned integer (I)
    t_1_jan_1970 = 2_208_988_800 
    time_curr = time_stamp[0] - t_1_jan_1970
    
    print(time.asctime(time.localtime(time_curr)))
