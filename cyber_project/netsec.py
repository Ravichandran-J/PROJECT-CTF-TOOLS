import os
import time
import argparse,sys
clear=lambda: os.system('clear')
clear()
def banner():
	
	print('@@@  @@@  @@@@@@@@  @@@@@@@      @@@@@@   @@@@@@@@   @@@@@@@ ')
	time.sleep(0.1)
	print('@@@@ @@@  @@@@@@@@  @@@@@@@     @@@@@@@   @@@@@@@@  @@@@@@@@')
	time.sleep(0.1)
	print('@@!@!@@@  @@!         @@!       !@@       @@!       !@@     ')
	time.sleep(0.1)
	print('!@!!@!@!  !@!         !@!       !@!       !@!       !@!     ')
	time.sleep(0.1)
	print('@!@ !!@!  @!!!:!      @!!       !!@@!!    @!!!:!    !@!     ')
	time.sleep(0.1)
	print('!@!  !!!  !!!!!:      !!!        !!@!!!   !!!!!:    !!!       ')
	time.sleep(0.1)
	print('!!:  !!!  !!:         !!:            !:!  !!:       :!!     ')
	time.sleep(0.1)
	print(':!:  !:!  :!:         :!:           !:!   :!:       :!:      ')
	time.sleep(0.1)
	print(' ::   ::   :: ::::     ::       :::: ::    :: ::::   ::: ::: ')
	time.sleep(0.1)
	print('::    :   : :: ::      :        :: : :    : :: ::    :: :: : ')
	time.sleep(0.1)
	print('\n')
	print('\t          !   By Cyber Lab BIT   !                  ')
banner()
print('''

1) ARP SCAN
2) PORT SCANNER
3) CIPHER 
4) HashExploit


0) EXIT
''')
#parser = argparse.ArgumentParser(description="HashExploit CLI. HashExpoit is Great Tool For Cracking Hash.It Supports 11 Hash Such as md5, sha1, sha223, sha3_384, blake2s, blake2b, sha384, sha3_224, sha512, sha256, sha3_256 etc. It Generates Rainbow Table. It Creates Sqlite Database in Current Directory and Mactch Hash With Rainbow Table. It Also Supports Prepend and Append Salt ")
parser=argparse.ArgumentParser(description="arp scanner,port scanner,cipher,hashexploit")
parser.add_argument('-1', '--arp', help = 'arp scan')
parser.add_argument('-2', '--port_scanner', help = 'for port scanning')
parser.add_argument('-3', '--cipher', help = 'encipher or decipher ')
parser.add_argument('-4', '--hashexploit', help = 'for crack and create hashes', nargs = 1)


# created argparse object
arg = parser.parse_args()

if arg.arp:
	os.system("python3 apr4.py")
	exit()
elif arg.port_scanner:
	os.system("python3 portscanner.py")
	exit()
elif arg.cipher:
	os.system("python3 cipher.py")
	exit()
elif arg.hashexploit:
	os.system("cd HashExploit && python3 HashExploit.py")
	exit()		
user_input=int(input("enter your choice:"))
if user_input==0:
	print("goodbye!!")
	time.sleep(1)
	clear()
	os.system('exit')
	exit()
def pro(user_input):
	if user_input==1:
		os.system("python3 apr4.py")
	elif user_input==2:
		os.system("python3 portscanner.py")
	elif user_input==3:
		os.system("python3 cipher.py")
	elif user_input==4:
		os.system("cd HashExploit && python3 HashExploit.py")
	
	
pro(user_input)
