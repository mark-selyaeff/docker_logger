#!/usr/bin/env python3

import os
import socket

HOST = ''
PORT = 65432

f = open('/var/log/server.log', 'ab')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print("Connected by", addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			# print("Got:", data)
			f.write(data)
			conn.sendall("OK:".encode('utf-8') + data)
f.close()
