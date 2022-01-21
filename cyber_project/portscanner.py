import os
import time 
def banner():
	print('      ___         ___           ___                  ')
	print('     /  /\       /  /\         /  /\          ___    ')
	print('    /  /::\     /  /::\       /  /::\        /  /\   ')
	print('   /  /:/\:\   /  /:/\:\     /  /:/\:\      /  /:/   ')
	print('  /  /:/~/:/  /  /:/  \:\   /  /:/~/:/     /  /:/    ')
	print(' /__/:/ /:/  /__/:/ \__\:\ /__/:/ /:/___  /  /::\    ')
	print(' \  \:\/:/   \  \:\ /  /:/ \  \:\/:::::/ /__/:/\:\   ')
	print('  \  \::/     \  \:\  /:/   \  \::/~~~~  \__\/  \:\  ')
	print('   \  \:\      \  \:\/:/     \  \:\           \  \:\ ')
	print('    \  \:\      \  \::/       \  \:\           \__\/ ')
	print('     \__\/       \__\/         \__\/                 ')
	print('      ___           ___           ___           ___           ___            ___           ___     ')
	print('     /  /\         /  /\         /  /\         /__/\         /__/\          /  /\         /  /\    ')
	print('    /  /:/_       /  /:/        /  /::\        \  \:\        \  \:\        /  /:/_       /  /::\   ')
	print('   /  /:/ /\     /  /:/        /  /:/\:\        \  \:\        \  \:\      /  /:/ /\     /  /:/\:\  ')
	print('  /  /:/ /::\   /  /:/  ___   /  /:/~/::\   _____\__\:\   _____\__\:\    /  /:/ /:/_   /  /:/~/:/  ')
	print(' /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/\:\ /__/::::::::\ /__/::::::::\  /__/:/ /:/ /\ /__/:/ /:/___')
	print(' \  \:\/:/~/:/ \  \:\ /  /:/ \  \:\/:/__\/ \  \:\~~\~~\/ \  \:\~~\~~\/  \  \:\/:/ /:/ \  \:\/:::::/')
	print('  \  \::/ /:/   \  \:\  /:/   \  \::/       \  \:\  ~~~   \  \:\  ~~~    \  \::/ /:/   \  \::/~~~~ ')
	print('   \__\/ /:/     \  \:\/:/     \  \:\        \  \:\        \  \:\         \  \:\/:/     \  \:\     ')
	print('     /__/:/       \  \::/       \  \:\        \  \:\        \  \:\         \  \::/       \  \:\    ')
	print('     \__\/         \__\/         \__\/         \__\/         \__\/          \__\/         \__\/    ')
	
	print(' 				!!By Cyber Lab Bit!!                                              ')

banner()

#	user_inp=int(input("enter the value:"))
#	ip=input("enter ip address:")
while True:
	print('''
1)agressive scan
2)os detection
3)perform a tcp null scan to  fool firewall 
4)fingerprinting os and services running on a target hosts
5)TCP scan
6)perform a stealthy scan
7)scan UDP
8)scan remote host using TCP ACK and TCP Syn (PS)
9)scan remote hot for TCP and ACK
10)script scan with thread
11)for fast scan 
12)all ports available
0) return to main menu
32) exit

''')
	user_inp=int(input("enter the value:"))
	if user_inp==0:
			print("returning main menu wait for 2 seconds")
			time.sleep(2)
			os.system("python3 netsec.py")
			exit()
	elif user_inp==32:
		exit(0)

	def fun(user_inp):
		
		ip=input("enter the ip (or) website (eg:scanme.nmap.org):")
		if user_inp==1:
			os.system("nmap -A "+ip)
		elif user_inp==2:
			os.system("nmap -O "+ip)
		#return user_inp
		elif user_inp==3:
			os.system("nmap -sN "+ip)
		elif user_inp==4:
			os.system("nmap -sv "+ip)
		elif user_inp==5:
			os.system("nmap -sT "+ip)
		elif user_inp==6:
			os.system("nmap -sS "+ip)
		elif user_inp==7:
			os.system("nmap -sU "+ip)
		elif user_inp==8:
			os.system("nmap -PS "+ip)
		elif user_inp==9:
			os.system("nmap -PA "+ip)
		elif user_inp==10:
			os.system("nmap -sC "+ip+" -T4")
		elif user_inp==11:
			os.system("nmap -F "+ip)
		elif user_inp==12:
			os.system("nmap -p- "+ip)
	fun(user_inp)
	

