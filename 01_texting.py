from m590_setup import m590
import time
import os
import RPi.GPIO as GPIO


#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sendBTN = 18
playBTN = 23
deleteBTN = 24
oneBTN = 25
twoBTN = 8
threeBTN = 7
fourBTN = 12
fiveBTN = 16
sixBTN = 20
sevenBTN = 2
eightBTN = 3
nineBTN = 4
starBTN = 17
zeroBTN = 27
hashBTN = 22

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

GPIO.setup(sendBTN,GPIO.LOW)
GPIO.setup(playBTN,GPIO.LOW)
GPIO.setup(deleteBTN,GPIO.LOW)
GPIO.setup(oneBTN,GPIO.LOW)
GPIO.setup(twoBTN,GPIO.LOW)
GPIO.setup(threeBTN,GPIO.LOW)
GPIO.setup(fourBTN,GPIO.LOW)
GPIO.setup(fiveBTN,GPIO.LOW)
GPIO.setup(sixBTN,GPIO.LOW)
GPIO.setup(sevenBTN,GPIO.LOW)
GPIO.setup(eightBTN,GPIO.LOW)
GPIO.setup(nineBTN,GPIO.LOW)
GPIO.setup(starBTN,GPIO.LOW)
GPIO.setup(zeroBTN,GPIO.LOW)
GPIO.setup(hashBTN,GPIO.LOW)
#end setup for LEDs#


#define speak function for text to speach
def speak(str):
	os.system("espeak '" + str + "' 2>/dev/null")
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
		print (response)

		if response[0] == "OK\r\n" or response[1] == "OK\r\n" or response[2] == "OK\r\n":
			print ("pin okay. let's go.")
	# 		speak("pin okay. let's go.")
			break
		elif response[2] != "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
			print ("pin okay. let's go.")
	# 		speak("pin okay. let's go.")
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
	GPIO.setup(sendBTN,GPIO.HIGH)
	GPIO.setup(playBTN,GPIO.HIGH)
	GPIO.setup(deleteBTN,GPIO.HIGH)
	GPIO.setup(oneBTN,GPIO.HIGH)
	GPIO.setup(twoBTN,GPIO.HIGH)
	GPIO.setup(threeBTN,GPIO.HIGH)
	GPIO.setup(fourBTN,GPIO.HIGH)
	GPIO.setup(fiveBTN,GPIO.HIGH)
	GPIO.setup(sixBTN,GPIO.HIGH)
	GPIO.setup(sevenBTN,GPIO.HIGH)
	GPIO.setup(eightBTN,GPIO.HIGH)
	GPIO.setup(nineBTN,GPIO.HIGH)
	GPIO.setup(starBTN,GPIO.HIGH)
	GPIO.setup(zeroBTN,GPIO.HIGH)
	GPIO.setup(hashBTN,GPIO.HIGH)

def allOff():
	GPIO.setup(sendBTN,GPIO.LOW)
	GPIO.setup(playBTN,GPIO.LOW)
	GPIO.setup(deleteBTN,GPIO.LOW)
	GPIO.setup(oneBTN,GPIO.LOW)
	GPIO.setup(twoBTN,GPIO.LOW)
	GPIO.setup(threeBTN,GPIO.LOW)
	GPIO.setup(fourBTN,GPIO.LOW)
	GPIO.setup(fiveBTN,GPIO.LOW)
	GPIO.setup(sixBTN,GPIO.LOW)
	GPIO.setup(sevenBTN,GPIO.LOW)
	GPIO.setup(eightBTN,GPIO.LOW)
	GPIO.setup(nineBTN,GPIO.LOW)
	GPIO.setup(starBTN,GPIO.LOW)
	GPIO.setup(zeroBTN,GPIO.LOW)
	GPIO.setup(hashBTN,GPIO.LOW)

def enterPhoneNumber():
	phoneNumber = ""
	while True:
		allOff()
		ch = getchar()
		
		if ch.strip() == "/":
			break
		if ch.strip() == "[":
			GPIO.setup(sendBTN,GPIO.HIGH)
			os.system("espeak sending: '" + phoneNumber + "' 2>/dev/null")
			print("sending to: " + phoneNumber)
			allOff()
			break
		elif ch.strip() == "]":
			GPIO.setup(deleteBTN,GPIO.HIGH)
			os.system("espeak 'deleting " +  phoneNumber[-1] + "' 2>/dev/null")
			tempChar = ""
			phoneNumber = phoneNumber[:-1]
			print(phoneNumber)
		elif ch.strip() == "=":
			GPIO.setup(playBTN,GPIO.HIGH)
			os.system("espeak '" +  phoneNumber + "' 2>/dev/null")
		else:
			if ch != "*" or "#" or "*": 
				phoneNumber = phoneNumber + ch
				print (phoneNumber)
			else: 
				phoneNumber = phoneNumber + 00
				print (phoneNumber)
			if ch == "1":
				GPIO.setup(oneBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "2":
				GPIO.setup(twoBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "3":
				GPIO.setup(threeBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "4":
				GPIO.setup(fourBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "5":
				GPIO.setup(fiveBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "6":
				GPIO.setup(sixBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "7":
				GPIO.setup(sevenBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "8":
				GPIO.setup(eightBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "9":
				GPIO.setup(nineBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "*":
				GPIO.setup(starBTN,GPIO.HIGH)
				speak("You're a star.")
			elif ch == "0":
				GPIO.setup(zeroBTN,GPIO.HIGH)
				speak(ch)
			elif ch == "#":
				GPIO.setup(hashBTN,GPIO.HIGH)
				speak("Hashtag Grow Your Own Phone!")
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
	   
		GPIO.setup(sendBTN,GPIO.LOW)
		GPIO.setup(playBTN,GPIO.LOW)
		GPIO.setup(deleteBTN,GPIO.LOW)
		GPIO.setup(oneBTN,GPIO.LOW)
		GPIO.setup(twoBTN,GPIO.LOW)
		GPIO.setup(threeBTN,GPIO.LOW)
		GPIO.setup(fourBTN,GPIO.LOW)
		GPIO.setup(fiveBTN,GPIO.LOW)
		GPIO.setup(sixBTN,GPIO.LOW)
		GPIO.setup(sevenBTN,GPIO.LOW)
		GPIO.setup(eightBTN,GPIO.LOW)
		GPIO.setup(nineBTN,GPIO.LOW)
		GPIO.setup(starBTN,GPIO.LOW)
		GPIO.setup(zeroBTN,GPIO.LOW)
		GPIO.setup(hashBTN,GPIO.LOW)

		newButton = getchar()
		newButton = str(newButton)
				
		if (tempChar != "") and (time.time() >= timeLimit) and (newButton.strip() != "*") and (newButton.strip() != "/") and (newButton.strip() != "="):
				message = message + tempChar
# 				os.system("espeak '" + message + "' 2>/dev/null")
				tempChar = ""
				print("time set " + message + tempChar)
				timeUp = True
				
		if newButton.strip() == "[":
			GPIO.setup(sendBTN,GPIO.HIGH)
			message = message + tempChar
			os.system("espeak sending: '" + message + "' 2>/dev/null")
			print("sending: " + message)
			allOff()
			break
		elif newButton.strip() == "]":
			GPIO.setup(deleteBTN,GPIO.HIGH)
			message = message + tempChar
			os.system("espeak 'deleting " +  message[-1] + "' 2>/dev/null")
			tempChar = ""
			message = message[:-1]
			print("new message " + message)
		elif newButton.strip() == "=":
			GPIO.setup(playBTN,GPIO.HIGH)
			message = message + tempChar
			os.system("espeak '" +  message + "' 2>/dev/null")
			tempChar = ""
		else:
			#everytime a button is pressed it restarts the wait time for setting the character
			timeLimit = time.time() + waitTime
			
			if newButton != oldButton and oldButton != "":
				if (timeUp == False) or (newButton.strip() != "*") or (newButton.strip() != "="):
					message = message + tempChar
					#os.system("espeak 'new button " + message + "' 2>/dev/null")
					tempChar = ""
					print("new button set " + message + tempChar)
			if newButton == "1":
				GPIO.setup(oneBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "1"
				elif(tempChar == "1"):
					tempChar = "1"
				print(message + tempChar)
# 				timeLimit = time.time()
			elif newButton == "2":
				GPIO.setup(twoBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "3":
				GPIO.setup(threeBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "4":
				GPIO.setup(fourBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "5":
				GPIO.setup(fiveBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "6":
				GPIO.setup(sixBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "7":
				GPIO.setup(sevenBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "8":
				GPIO.setup(eightBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "9":
				GPIO.setup(nineBTN,GPIO.HIGH)
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
# 				timeLimit = time.time()
			elif newButton == "*":
				GPIO.setup(starBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "/r"
				elif(tempChar == "/r"):
					tempChar = "*"
				elif(tempChar == "*"):
					tempChar = "/r"
				speak(tempChar)
				print(message + tempChar)
# 				timeLimit = time.time()
			elif newButton == "0":
				GPIO.setup(zeroBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = " "
				elif(tempChar == " "):
					tempChar = "0"
				elif(tempChar == "0"):
					tempChar = " "
				speak(tempChar)
				print(message + tempChar)
# 				timeLimit = time.time()
			elif newButton == "#":
				GPIO.setup(hashBTN,GPIO.HIGH)
				if(tempChar == ""):
					tempChar = "."
				elif(tempChar == "."):
					tempChar = "?"
				elif(tempChar == "?"):
					tempChar = "!"
				elif(tempChar == "!"):
					tempChar = ","
				elif(tempChar == ","):
					tempChar = "-"
				elif(tempChar == "-"):
					tempChar = "#"
				elif(tempChar == "#"):
					tempChar = "."
				speak(tempChar)
				print(message + tempChar)
# 				timeLimit = time.time()
			oldButton = newButton
			
# 		if tempChar != "" and time.time() >= timeLimit:
# 			message = message + tempChar
# 			tempChar = ""
# 			print("time set " + message + tempChar)
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
		 	speak("Enter a french mobile phone number")
			phoneNumber = enterPhoneNumber()

			if len(phoneNumber) < 10:
				print len(phoneNumber)
				speak("Phone number too short. Try again.")
				print ("Error. Too Short")
				continue
			elif len(phoneNumber) == 10 and (phoneNumber[:2] != "06" or phoneNumber[:2] != "07")
			elif len(phoneNumber) == 13 and (phoneNumber[:5] != "00336" or phoneNumber[:5] != "00337"):
				speak("French mobile numbers begin with either 06 or 07. Try again.")
				print ("Error. Not French.")
				print(phoneNumber[:2])
				print(phoneNumber[:5])
				continue
			elif len(phoneNumber) == 12:
				print len(phoneNumber)
				speak("Phone number too long. Phone numbers starting with 06 or 07 should only be 10 digits. Try again.")
				print ("Error. Too Short")
				continue
			elif len(phoneNumber) > 13:
				print len(phoneNumber)
				speak("Phone number too long. Try again.")
				print ("Error. Too Short")
				continue
			else:
				speak("Sending to " + phoneNumber)
				break

		phoneNumber = "0637165118"

		#message = raw_input("Enter Message::\n")
		speak("Enter your message")
		print ("Enter message.\n")
		message = enterMessage()


		#SEND SMS
		print ("Sending text..")
		speak("Sending text")
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
		time.sleep(2)
		allOff()


	modem.deinit()

if __name__ == "__main__":
    main()
