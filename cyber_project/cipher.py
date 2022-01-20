import os
import time 
clear=lambda: os.system('clear')
clear()
L2I=dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L=dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key=3
print(" @@@@@@@  @@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   @@@  @@@  ")
print("@@@@@@@@  @@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  ")
print("!@@       @@!  @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  !@@  ")
print("!@!       !@!  !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!  @!!  ")
print("!@!       !!@  @!@@!@!   @!@!@!@!  @!!!:!    @!@!!@!    !@@!@!   ")
print("!!!       !!!  !!@!!!    !!!@!!!!  !!!!!:    !!@!@!      @!!!    ")
print(":!!       !!:  !!:       !!:  !!!  !!:       !!: :!!    !: :!!   ")
print(":!:       :!:  :!:       :!:  !:!  :!:       :!:  !:!  :!:  !:!  ")
print(" ::: :::   ::   ::       ::   :::   :: ::::  ::   :::   ::  :::  ")
print(" :: :: :  :     :         :   : :  : :: ::    :   : :   :   ::   ")

print("                    !By CyberLab Bit!                                             ")
print("\n")
while True:
	print("IF YOU WANT TO EXIT THE PROGRAM TYPE EXIT:")
	print("                (Or) type main to return main menu ")
	user=input("encipher (or) decipher:")
	if user=="encipher":
		def encipher():
			plaintext=input("enter your input here:")
			ciphertext=""
			for c in plaintext.upper():
				if c.isalpha(): ciphertext += I2L[(L2I[c]+key)%26]
				else: ciphertext+=c
			print(ciphertext)
			print("\n")
		encipher()
	elif user=="decipher":
		def decipher():
			encoded_text=input("enter your encoded message here:")
			plaintext2=""
			for c in encoded_text.upper():
				if c.isalpha(): plaintext2+=I2L[(L2I[c]-key)%26]
				else: plaintext2+=c
			print(plaintext2)
			print("\n")
		decipher()
	elif user=="exit":
		#from time import sleep
		#def printd(text,delay=0.5):
			#print(end=text)
			#n_dots=0
			#if n_dots==5:
				#print(end="\b\b\b",flush=True)
				#print(end="    ",flush=True)
				#print(end="\b\b\b",flush=True)
				#n_dots=0
			#else:
				#print(end=".",flush=True)
				#n_dots+=1
			#sleep(delay)
		#printd("exiting",delay=0.5)
		exit("exiting \n")
	elif user =="main":
		print("returning main menu wait for 2 seconds")
		time.sleep(2)
		os.system("python3 cyberlab_pentest.py")
		exit()
	
		

