# -*- coding: utf-8 -*-

from m590_setup import m590
import time
import os, sys
import RPi.GPIO as GPIO


#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sendBTN = 18
playBTN = 23
deleteBTN = 24
oneBTN = 25
twoBTN = 12
threeBTN = 16
fourBTN = 20
fiveBTN = 4
sixBTN = 17
sevenBTN = 27
eightBTN = 22
nineBTN = 5
starBTN = 6
zeroBTN = 13
hashBTN = 19

GPIO.setup(sendBTN,GPIO.OUT)
GPIO.setup(playBTN,GPIO.OUT)
GPIO.setup(deleteBTN,GPIO.OUT)
GPIO.setup(oneBTN,GPIO.OUT)
GPIO.setup(twoBTN,GPIO.OUT)
GPIO.setup(threeBTN,GPIO.OUT)
GPIO.setup(fourBTN,GPIO.OUT)
GPIO.setup(fiveBTN,GPIO.OUT)
GPIO.setup(sixBTN,GPIO.OUT)
GPIO.setup(sevenBTN,GPIO.OUT)
GPIO.setup(eightBTN,GPIO.OUT)
GPIO.setup(nineBTN,GPIO.OUT)
GPIO.setup(starBTN,GPIO.OUT)
GPIO.setup(zeroBTN,GPIO.OUT)
GPIO.setup(hashBTN,GPIO.OUT)

GPIO.output(sendBTN,GPIO.LOW)
GPIO.output(playBTN,GPIO.LOW)
GPIO.output(deleteBTN,GPIO.LOW)
GPIO.output(oneBTN,GPIO.LOW)
GPIO.output(twoBTN,GPIO.LOW)
GPIO.output(threeBTN,GPIO.LOW)
GPIO.output(fourBTN,GPIO.LOW)
GPIO.output(fiveBTN,GPIO.LOW)
GPIO.output(sixBTN,GPIO.LOW)
GPIO.output(sevenBTN,GPIO.LOW)
GPIO.output(eightBTN,GPIO.LOW)
GPIO.output(nineBTN,GPIO.LOW)
GPIO.output(starBTN,GPIO.LOW)
GPIO.output(zeroBTN,GPIO.LOW)
GPIO.output(hashBTN,GPIO.LOW)
#end setup for LEDs#


#define function for text to speach
def speak(str):
	#speaking speed is default to 160 wpm
	os.system("espeak -v fr '" + str + "' -s 100 2>/dev/null")
#end of definintion od speak function for text to speach

def getchar():
   #Returns a single character from standard input
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def setUpPin():
	response = ""
	pin = ""

	# speak("Initialising")
	print ("Initialising Modem & Checking PIN..")

	while True:
		pin = "1234"
		m590.ser.write("at+cpin=\"1234\"\r")
		time.sleep(0.3)
		m590.ser.write("at+cpin?\r")
		response = m590.ser.readlines(None)
		
		print(response, '-response')
		
		
		if not response:
			print ("errrror")
		else:
			if response[0] == "OK\r\n" or response[1] == "OK\r\n" or response[2] == "OK\r\n":
				print ("pin okay. let's go.")
				# speak("pin okay. let's go.")
				break
			elif response[2] != "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
				print ("pin okay. let's go.")
				# speak("pin okay. let's go.")
				break
			elif response[2] == "+CPIN: SIM PIN\r\n":
				m590.ser.write("at+cpin=\"1234\"\r")
				time.sleep(0.5)
				continue
			elif response[1] == "ERROR/r/n" or response[2] == "ERROR/r/n":
				print (response[1] + "\n")
				print ("Error. Restart the Module")
			else:
				print (response[1] + "\n")
				print ("check your SIM card is inserted and the light on the GSM module is flashing./nIf all looks good, get Kris.")
		#else:
			#print ("error with gsm module")
def restart():
	command = "/usr/bin/sudo /sbin/shutdown -r now"
	import subprocess
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print (output)
	
def checkIfModuleFrozen():
	m590.ser.write("at\r")
	time.sleep(1.0)
	response = m590.ser.readlines(None)
	print(response)
 	#response = response[1]
	if response == "[]" or response == "":
		print ("response not okay")
		print (response)
		#os.system('sudo shutdown -r now') #does not work. just freezes the program.
		restart()
		print ("the raspberry pi should have just restarted.")
	else:
		print ("response is okay")
		print (response)

def allOn():
	ledOnFor = 0.2
	allOff()
	
	for x in xrange(3):
		GPIO.output(sendBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(sendBTN,GPIO.LOW)

		GPIO.output(sendBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(playBTN,GPIO.LOW)

		GPIO.output(deleteBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(deleteBTN,GPIO.LOW)

		GPIO.output(oneBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(oneBTN,GPIO.LOW)

		GPIO.output(twoBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(twoBTN,GPIO.LOW)

		GPIO.output(threeBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(threeBTN,GPIO.LOW)

		GPIO.output(fourBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(fourBTN,GPIO.LOW)

		GPIO.output(fiveBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(fiveBTN,GPIO.LOW)

		GPIO.output(sixBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(sixBTN,GPIO.LOW)

		GPIO.output(sevenBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(sevenBTN,GPIO.LOW)

		GPIO.output(eightBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(eightBTN,GPIO.LOW)

		GPIO.output(nineBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(nineBTN,GPIO.LOW)

		GPIO.output(starBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(starBTN,GPIO.LOW)

		GPIO.output(zeroBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(zeroBTN,GPIO.LOW)

		GPIO.output(hashBTN,GPIO.HIGH)
		time.sleep(ledOnFor)
		GPIO.output(hashBTN,GPIO.LOW)
	

def allOff():
	GPIO.output(sendBTN,GPIO.LOW)
	GPIO.output(playBTN,GPIO.LOW)
	GPIO.output(deleteBTN,GPIO.LOW)
	GPIO.output(oneBTN,GPIO.LOW)
	GPIO.output(twoBTN,GPIO.LOW)
	GPIO.output(threeBTN,GPIO.LOW)
	GPIO.output(fourBTN,GPIO.LOW)
	GPIO.output(fiveBTN,GPIO.LOW)
	GPIO.output(sixBTN,GPIO.LOW)
	GPIO.output(sevenBTN,GPIO.LOW)
	GPIO.output(eightBTN,GPIO.LOW)
	GPIO.output(nineBTN,GPIO.LOW)
	GPIO.output(starBTN,GPIO.LOW)
	GPIO.output(zeroBTN,GPIO.LOW)
	GPIO.output(hashBTN,GPIO.LOW)

def enterPhoneNumber():
	phoneNumber = ""
	while True:
		allOff()
		ch = getchar()

		if ch.strip() == "/":
			break
		if ch.strip() == "[":
			GPIO.output(sendBTN,GPIO.HIGH)
			print("sending to: " + phoneNumber)
			allOff()
			break
		elif ch.strip() == "]":
			if len(phoneNumber) > 0:
				GPIO.output(deleteBTN,GPIO.HIGH)
				os.system("espeak -v fr 'En suppression " +  phoneNumber[-1] + "' -s 100 2>/dev/null")
				tempChar = ""
				phoneNumber = phoneNumber[:-1]
				print(phoneNumber)
			else:
				speak("Aucun numéro")
		elif ch.strip() == "=":
			GPIO.output(playBTN,GPIO.HIGH)
			os.system("espeak -v fr '" +  phoneNumber + "' -s 100 2>/dev/null")
		else:
			if ch != "s" and ch != "h": 
				if len(phoneNumber) > 20:
					phoneNumber = ""
				else:
					phoneNumber = phoneNumber + ch
					print (phoneNumber)
			else: 
				phoneNumber = phoneNumber
				print (phoneNumber)
			if ch == "1":
				GPIO.output(oneBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "2":
				GPIO.output(twoBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "3":
				GPIO.output(threeBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "4":
				GPIO.output(fourBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "5":
				GPIO.output(fiveBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "6":
				GPIO.output(sixBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "7":
				GPIO.output(sevenBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "8":
				GPIO.output(eightBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "9":
				GPIO.output(nineBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "s":
				GPIO.output(starBTN,GPIO.HIGH)
# 				os.system("espeak -v fr 'You're a star.' -s 100 2>/dev/null")
# 				speak("You're a star.")
				ch = "astérisque"
				speak(ch)
			elif ch == "0":
				GPIO.output(zeroBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "h":
				GPIO.output(hashBTN,GPIO.HIGH)
# 				speak("Hashtag Grow Your Own Phone!")
				ch = "dièse"
				speak(ch)
			elif ch == "c":
				sys.exit("exited program.")
	return phoneNumber

def doSomething(message, tempChar):
	speak(speakChar)
	time.sleep(0.5) 
	print("test2")
	message = message + tempChar
	
def enterMessage():
	tempChar = ""
	oldButton = ""
	message = ""
	waitTime = 2 #in seconds
	timeUp = False
	timeLimit = 0
	while True:
	   
		allOff()

		newButton = getchar()
		newButton = str(newButton)
				
		if (tempChar != "") and (time.time() >= timeLimit) and (newButton.strip() != "*") and (newButton.strip() != "/") and (newButton.strip() != "="):
				message = message + tempChar
# 				os.system("espeak '" + message + "' -s 100 2>/dev/null")
				tempChar = ""
				print("time set " + message + tempChar)
				timeUp = True
				
		if newButton.strip() == "[":
			GPIO.output(sendBTN,GPIO.HIGH)
			message = message + tempChar
			os.system("espeak -v fr 'En envoi : " + message + "' -s 100 2>/dev/null")
			print("sending: " + message)
			allOff()
			break
		elif newButton.strip() == "]":
			if len(message) > 0:
				GPIO.output(deleteBTN,GPIO.HIGH)
				message = message + tempChar
				os.system("espeak -v fr 'En suppression " +  message[-1] + "' -s 100 2>/dev/null")
				tempChar = ""
				message = message[:-1]
			else:
				speak("Aucun message")
			print("new message " + message)
		elif newButton.strip() == "=":
			GPIO.output(playBTN,GPIO.HIGH)
			message = message + tempChar
			os.system("espeak -v fr '" +  message + "' -s 100 2>/dev/null")
			tempChar = ""
		else:
			#everytime a button is pressed it restarts the wait time for setting the character
			timeLimit = time.time() + waitTime
			
			if newButton != oldButton and oldButton != "":
				if (timeUp == False) or (newButton.strip() != "*") or (newButton.strip() != "="):
					message = message + tempChar
					#os.system("espeak 'new button " + message + "' -s 100 2>/dev/null")
					tempChar = ""
					print("new button set " + message + tempChar)
			if newButton == "1":
				GPIO.output(oneBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "1"
				elif(tempChar == "1"):
					tempChar = "1"
				print(message + tempChar)
				speak(tempChar)
			elif newButton == "2":
				GPIO.output(twoBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "a"
				elif(tempChar == "a"):
					tempChar = "b"
				elif(tempChar == "b"):
					tempChar = "c"
				elif(tempChar == "c"):
					tempChar = "2"
				elif(tempChar == "2"):
					tempChar = "a"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "3":
				GPIO.output(threeBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "d"
				elif(tempChar == "d"):
					tempChar = "e"
				elif(tempChar == "e"):
					tempChar = "f"
				elif(tempChar == "f"):
					tempChar = "3"
				elif(tempChar == "3"):
					tempChar = "d"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "4":
				GPIO.output(fourBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "g"
				elif(tempChar == "g"):
					tempChar = "h"
				elif(tempChar == "h"):
					tempChar = "i"
				elif(tempChar == "i"):
					tempChar = "4"
				elif(tempChar == "4"):
					tempChar = "g"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "5":
				GPIO.output(fiveBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "j"
				elif(tempChar == "j"):
					tempChar = "k"
				elif(tempChar == "k"):
					tempChar = "l"
				elif(tempChar == "l"):
					tempChar = "5"
				elif(tempChar == "5"):
					tempChar = "j"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "6":
				GPIO.output(sixBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "m"
				elif(tempChar == "m"):
					tempChar = "n"
				elif(tempChar == "n"):
					tempChar = "o"
				elif(tempChar == "o"):
					tempChar = "6"
				elif(tempChar == "6"):
					tempChar = "m"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "7":
				GPIO.output(sevenBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "p"
				elif(tempChar == "p"):
					tempChar = "q"
				elif(tempChar == "q"):
					tempChar = "r"
				elif(tempChar == "r"):
					tempChar = "s"
				elif(tempChar == "s"):
					tempChar = "7"
				elif(tempChar == "7"):
					tempChar = "p"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "8":
				GPIO.output(eightBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "t"
				elif(tempChar == "t"):
					tempChar = "u"
				elif(tempChar == "u"):
					tempChar = "v"
				elif(tempChar == "v"):
					tempChar = "8"
				elif(tempChar == "8"):
					tempChar = "t"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "9":
				GPIO.output(nineBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "w"
				elif(tempChar == "w"):
					tempChar = "x"
				elif(tempChar == "x"):
					tempChar = "y"
				elif(tempChar == "y"):
					tempChar = "z"
				elif(tempChar == "z"):
					tempChar = "9"
				elif(tempChar == "9"):
					tempChar = "w"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "s":
				GPIO.output(starBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "/r"
				elif(tempChar == "/r"):
					tempChar = "*"
				elif(tempChar == "*"):
					tempChar = "/r"
				speak(tempChar)
				print(message + tempChar)
			elif newButton == "0":
				GPIO.output(zeroBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = " "
					speak("Espace")
				elif(tempChar == " "):
					tempChar = "0"
					speak(tempChar)
				elif(tempChar == "0"):
					tempChar = " "
					speak("Espace")
				print(message + tempChar)
			elif newButton == "h":
				GPIO.output(hashBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "."
					speak("point")
				elif(tempChar == "."):
					tempChar = "?"
					speak("interrogation")
				elif(tempChar == "?"):
					tempChar = "!"
					speak("exclamation")
				elif(tempChar == "!"):
					tempChar = ","
					speak("virgule")
				elif(tempChar == ","):
					tempChar = "-"
					speak("trait")
				elif(tempChar == "-"):
					tempChar = "#"
					speak("dièse")
				elif(tempChar == "#"):
					tempChar = "."
					speak("point")
				speak(tempChar)
				print(message + tempChar)
			oldButton = newButton
		timeUp = False
			
	return message


def main():
	modem = m590()
	modem.init()
	
	checkIfModuleFrozen()
	setUpPin()

	while True:
		checkIfModuleFrozen()
		while True:
		 	speak("Entrer un numéro français de téléphone portable.")
			phoneNumber = enterPhoneNumber()
# 			phoneNumber = "0637165118"

			if len(phoneNumber) < 10:
				print len(phoneNumber)
				speak("Numéro de téléphone trop court. Essayer encore.")
				print ("Error. Too Short")
				continue
			elif len(phoneNumber) == 10 and (phoneNumber[:2] != "06" and phoneNumber[:2] != "07"):
				speak("Les numéros francais de téléphone portable commencent soit par un 06, soit par un 07. Essayer encore.")
				print ("Error. Not French.")
				print(phoneNumber[:2])
				continue
			elif len(phoneNumber) == 13 and (phoneNumber[:5] != "00336" and phoneNumber[:5] != "00337"):
				speak("Les numéros francais de téléphone portable commencent soit par un 00336, soit par un 00337. Essayer encore.")
				print ("Error. Not French.")
				print(phoneNumber[:5])
				continue
			elif len(phoneNumber) == 12:
				print len(phoneNumber)
				speak("Numéro de téléphone trop long. les numéros de téléphone commencent par un 06 ou un 07 et doivent seulement avoir 10 caractères. Essayer encore.")
				print ("Error. Too Short")
				continue
			elif len(phoneNumber) > 13:
				print len(phoneNumber)
				speak("Numéro de téléphone trop long. Essayer encore.")
				print ("Error. Too Short")
				continue
			else:
				speak("Envoi à" + phoneNumber.replace("", ", ")[1: -1])
				break


		#message = raw_input("Enter Message::\n")
		speak("Ecrire votre message.")
		print ("Enter message.\n")
		message = enterMessage()


		#SEND SMS
		print ("Sending text.")
		speak("Envoi message.")
		modem.send_sms(phoneNumber, message)
		
# 		time.sleep(1)
# 		response = m590.ser.readlines(None)
# 		print (response)
# 		if response == "":
# 			speak("Error!")
# 			print (response)
# 		elif response[0] == "\n":
# 			speak("Sent!")
# 			print ("Sent!")
# 		else:
# 			speak("error")
# 			print (response)

		allOn()
		allOff()


	modem.deinit()

if __name__ == "__main__":
    main()
