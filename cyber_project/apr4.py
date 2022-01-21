import os 
import time 
clear=lambda: os.system('clear')
clear()
print('  AAA   RRRRRR  PPPPPP    SSSSS   CCCCC    AAA   NN   NN  ')
print(' AAAAA  RR   RR PP   PP  SS      CC    C  AAAAA  NNN  NN  ')
print('AA   AA RRRRRR  PPPPPP    SSSSS  CC      AA   AA NN N NN  ')
print('AAAAAAA RR  RR  PP            SS CC    C AAAAAAA NN  NNN  ')
print('AA   AA RR   RR PP        SSSSS   CCCCC  AA   AA NN   NN  ')

print('			!!By Cyber Lab Bit!!                     ')
print('\n')
time.sleep(2)
print('''
1) to run
2)exit
''')
while True:
	inp=int(input("enter the values:"))
	if inp==1:
		os.system("arp-scan --local")
	elif inp==2:
		print("returning main menu wait 3 seconds")
		time.sleep(3)
		os.system("python3 netsec.py")
		exit()

