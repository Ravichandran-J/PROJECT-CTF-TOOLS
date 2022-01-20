import os
import time 
clear=lambda: os.system('clear')
clear()
L2I=dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L=dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
numb1=dict(zip("1234567890",range(10)))
numb2=dict(zip(range(10),"1234567890"))
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
	print("type file for  encipher and decipher  file (or) type text for encipher and decipher text  ")
	print("				(or) type exit to exit the process ")
	user_inp=input("enter file or text:")
	print("\n")
	if user_inp=="file":
	 
		file_type=input("enter the file name with extension:")
		file=open(file_type,'r')
		line_count=0
		for line in file:
			if line != "\n":
				line_count+=1
		#file.close()
		with open('{}'.format(file_type),mode='r',encoding='utf-8') as f:
			user=input("encipher (or) decipher (or) exit (or) clear:")
			if user=='encipher':
				text=""
				with open(file_type) as my_file:
					text=my_file.read()
					text=text.replace("\n"," ")
				print(text)
				ciphertext=""
				for c in text.upper():
					if c.isalpha(): 
						ciphertext += I2L[(L2I[c]+key)%26]
					else: 
						ciphertext+=c
				print("encipher value without number:",ciphertext)
				ciphertextwithnum=""
				for d in ciphertext.upper():
					if d.isnumeric():
						ciphertextwithnum+=numb2[(numb1[d]+key)%10]
					else: ciphertextwithnum+=d
				print("encipher value with number:",ciphertextwithnum)
					
						
			elif user=='decipher':
				text2=""
				with open(file_type) as my_file2:
					text2=my_file2.read()
					text2=text2.replace("\n"," ")
				print(text2)
				plaintext=""
				for c in text2.upper():
					if c.isalpha():
						plaintext+=I2L[(L2I[c]-key)%26]
					else:
						plaintext+=c
				print("decipher value without number:",plaintext)
				plaintextwithnum=""
				for e in plaintext.upper():
					if e.isnumeric():
						plaintextwithnum+=numb2[(numb1[e]-key)%10]
					else:
						plaintextwithnum+=e
				print("decipher value with number:",plaintextwithnum)
			elif user=='clear':
				clear()
			elif user=="exit":
				os.system('exit')
				exit()
	elif user_inp=="text":
		user=input("encipher (or) decipher (or) exit (or) clear:")
		if user=="encipher":
			def encipher():
				plaintext=input("enter your input here:")
				ciphertext2=""
				for c in plaintext.upper():
					if c.isalpha(): ciphertext2 += I2L[(L2I[c]+key)%26]
					else: ciphertext2+=c
				print(ciphertext2)
				#print("\n")
				ciphertextwithnum2=""
				for d in ciphertext2.upper():
					if d.isnumeric():
						ciphertextwithnum2+=numb2[(numb1[d]+key)%10]
					else: ciphertextwithnum2+=d
				print("encipher value with number:",ciphertextwithnum2)
				
			encipher()
		elif user=="decipher":
			def decipher():
				encoded_text=input("enter your encoded message here:")
				plaintext2=""
				for c in encoded_text.upper():
					if c.isalpha(): plaintext2+=I2L[(L2I[c]-key)%26]
					else: plaintext2+=c
				print(plaintext2)
				#print("\n")
				plaintextwithnum2=""
				for e in plaintext2.upper():
					if e.isnumeric():
						plaintextwithnum2+=numb2[(numb1[e]-key)%10]
					else:
						plaintextwithnum2+=e
				print("decipher value with number:",plaintextwithnum2)
			decipher()
		elif user=='clear':
			clear()
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
	elif user_inp=="exit":
		os.system('exit')
		exit()
		
					
			
'''				lin=[]
				with open(file_type) as myfile:
					lin=myfile.readlines()
					#lin=lin.replace("\n","")
				print(lin)'''
				
'''				for x in range(line_count):
					lin.append(x)
				print(lin)'''
			
'''				ciphertext=''
				for c in lin.upper:
					if c.isalpha(): ciphertext +=I2L[(L2I[c]+key)%26]
					else: ciphertext+=c
				print(ciphertext)
				print("\n")'''
			
