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

def enterPhoneNumber():
	phoneNumber = ""
	while True:
		ch = getchar()
		if ch.strip() == '/':
			print(phoneNumber)
			break
		else:
			phoneNumber = phoneNumber + ch
			print ("numbers typed " , len(phoneNumber))
			print ('You pressed', ch)
			speak(ch)
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
	waitTime = 1 #in seconds
	timeUp = False
	timeLimit = 0
	lastBTN = ""
	while True:
# 		ch = getchar()
		
# 		GPIO.setup(sendBTN,GPIO.LOW)
# 		GPIO.setup(playBTN,GPIO.LOW)
# 		GPIO.setup(deleteBTN,GPIO.LOW)
# 		GPIO.setup(oneBTN,GPIO.LOW)
# 		GPIO.setup(twoBTN,GPIO.LOW)
# 		GPIO.setup(threeBTN,GPIO.LOW)
# 		GPIO.setup(fourBTN,GPIO.LOW)
# 		GPIO.setup(fiveBTN,GPIO.LOW)
# 		GPIO.setup(sixBTN,GPIO.LOW)
# 		GPIO.setup(sevenBTN,GPIO.LOW)
# 		GPIO.setup(eightBTN,GPIO.LOW)
# 		GPIO.setup(nineBTN,GPIO.LOW)
# 		GPIO.setup(starBTN,GPIO.LOW)
# 		GPIO.setup(zeroBTN,GPIO.LOW)
# 		GPIO.setup(hashBTN,GPIO.LOW)
		
# # 		if keyboard.is_pressed("["):
# 		if ch == "[":
# 			print("pressed")
# 			GPIO.setup(sendBTN,GPIO.HIGH)
# 			lastBTN = "["
# 			if lastBTN != "[":
# 				message = message + tempChar
# 				tempChar = ""
# 			speak("sending " + message)
# 			print("sending: " + message)
# 			break
# # 		else:
# # 			GPIO.setup(sendBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("="):
# 		elif ch == "=":
# 			print("pressed")
# 			GPIO.setup(playBTN,GPIO.HIGH)
# 			speak(message)
# 			if lastBTN != "=":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "="
# # 		else:
# # 			GPIO.setup(playBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("]"):
# 		elif ch == "]":
# 			print("pressed")
# 			GPIO.setup(deleteBTN,GPIO.HIGH)
# 			if lastBTN != "]":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "]"
# 			os.system("espeak 'deleting " +  message[-1] + "' 2>/dev/null")
# 			message = message[:-1]
# # 		else:
# # 			GPIO.setup(deleteBTN,GPIO.LOW)
			
# 		elif ch == "1":
# # 		if keyboard.is_pressed("1"):
# 			GPIO.setup(oneBTN,GPIO.HIGH)
# 			if lastBTN != "1":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "1"
# 			if(tempChar == ""):
# 				tempChar = "1"
# 			elif(tempChar == "1"):
# 				tempChar = "1"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(oneBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("2"):
# 		elif ch == "2":
# 			print("pressed")
# 			GPIO.setup(twoBTN,GPIO.HIGH)
# 			if lastBTN != "2":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "2"
# 			if(tempChar == ""):
# 				tempChar = "a"
# 			elif(tempChar == "a"):
# 				tempChar = "b"
# 			elif(tempChar == "b"):
# 				tempChar = "c"
# 			elif(tempChar == "c"):
# 				tempChar = "2"
# 			elif(tempChar == "2"):
# 				tempChar = "a"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(twoBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("3"):
# 		elif ch == "3":
# 			print("pressed")
# 			GPIO.setup(threeBTN,GPIO.HIGH)
# 			if lastBTN != "3":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "3"
# 			if(tempChar == ""):
# 				tempChar = "d"
# 			elif(tempChar == "d"):
# 				tempChar = "e"
# 			elif(tempChar == "e"):
# 				tempChar = "f"
# 			elif(tempChar == "f"):
# 				tempChar = "3"
# 			elif(tempChar == "3"):
# 				tempChar = "d"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(threeBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("4"):
# 		elif ch == "4":
# 			print("pressed")
# 			GPIO.setup(fourBTN,GPIO.HIGH)
# 			if lastBTN != "4":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "4"
# 			if(tempChar == ""):
# 				tempChar = "g"
# 			elif(tempChar == "g"):
# 				tempChar = "h"
# 			elif(tempChar == "h"):
# 				tempChar = "i"
# 			elif(tempChar == "i"):
# 				tempChar = "4"
# 			elif(tempChar == "4"):
# 				tempChar = "g"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(fourBTN,GPIO.LOW)
			
# 		elif ch == "5":
# # 		if keyboard.is_pressed("5"):
# 			print("pressed 'a'")
# 			GPIO.setup(fiveBTN,GPIO.HIGH)
# 			if lastBTN != "5":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "5"
# 			if(tempChar == ""):
# 				tempChar = "j"
# 			elif(tempChar == "j"):
# 				tempChar = "k"
# 			elif(tempChar == "k"):
# 				tempChar = "l"
# 			elif(tempChar == "l"):
# 				tempChar = "5"
# 			elif(tempChar == "5"):
# 				tempChar = "j"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(fiveBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("6"):
# 		elif ch == "6":
# 			print("pressed 'a'")
# 			GPIO.setup(sixBTN,GPIO.HIGH)
# 			if lastBTN != "6":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "6"
# 			if(tempChar == ""):
# 				tempChar = "m"
# 			elif(tempChar == "m"):
# 				tempChar = "n"
# 			elif(tempChar == "n"):
# 				tempChar = "o"
# 			elif(tempChar == "o"):
# 				tempChar = "6"
# 			elif(tempChar == "6"):
# 				tempChar = "m"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(sixBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("7"):
# 		elif ch == "7":
# 			print("pressed 'a'")
# 			GPIO.setup(sevenBTN,GPIO.HIGH)
# 			if lastBTN != "7":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "7"
# 			if(tempChar == ""):
# 				tempChar = "p"
# 			elif(tempChar == "p"):
# 				tempChar = "q"
# 			elif(tempChar == "q"):
# 				tempChar = "r"
# 			elif(tempChar == "r"):
# 				tempChar = "s"
# 			elif(tempChar == "s"):
# 				tempChar = "7"
# 			elif(tempChar == "7"):
# 				tempChar = "p"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(sevenBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("8"):
# 		elif ch == "8":
# 			print("pressed")
# 			GPIO.setup(eightBTN,GPIO.HIGH)
# 			if lastBTN != "8":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "8"
# 			if(tempChar == ""):
# 				tempChar = "t"
# 			elif(tempChar == "t"):
# 				tempChar = "u"
# 			elif(tempChar == "u"):
# 				tempChar = "v"
# 			elif(tempChar == "v"):
# 				tempChar = "8"
# 			elif(tempChar == "8"):
# 				tempChar = "t"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(eightBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("9"):
# 		elif ch == "9":
# 			print("pressed")
# 			GPIO.setup(nineBTN,GPIO.HIGH)
# 			if lastBTN != "9":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "9"
# 			if(tempChar == ""):
# 				tempChar = "w"
# 			elif(tempChar == "w"):
# 				tempChar = "x"
# 			elif(tempChar == "x"):
# 				tempChar = "y"
# 			elif(tempChar == "y"):
# 				tempChar = "z"
# 			elif(tempChar == "z"):
# 				tempChar = "9"
# 			elif(tempChar == "9"):
# 				tempChar = "w"
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 			speak(tempChar)
# # 		else:
# # 			GPIO.setup(nineBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("*"):
# 		elif ch == "*":
# 			print("pressed")
# 			GPIO.setup(starBTN,GPIO.HIGH)
# 			if lastBTN != "*":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "*"
# 			if(tempChar == ""):
# 				tempChar = "/r"
# 				speak("return")
# 			elif(tempChar == "/r"):
# 				tempChar = "*"
# 				speak("asterix")
# 			elif(tempChar == "*"):
# 				tempChar = "/r"
# 				speak("return")
# 			print(message + tempChar)
# 			timeLimit = time.time()
# 		   	speak(tempChar)
# # 		else:
# # 			GPIO.setup(starBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("0"):
# 		elif ch == "0":
# 			print("pressed 'a'")
# 			GPIO.setup(zeroBTN,GPIO.HIGH)
# 			if lastBTN != "*":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "0"
# 			if(tempChar == ""):
# 				tempChar = " "
# 				speak("space")
# 			elif(tempChar == " "):
# 				tempChar = "0"
# 				speak("zero")
# 			elif(tempChar == "0"):
# 				tempChar = " "
# 				speak("space")
# 			print(message + tempChar)
# 			timeLimit = time.time()
# # 		else:
# # 			GPIO.setup(zeroBTN,GPIO.LOW)
			
# # 		if keyboard.is_pressed("#"):
# 		elif ch == "#":
# 			print("pressed 'a'")
# 			GPIO.setup(hashBTN,GPIO.HIGH)
# 			if lastBTN != "*":
# 				message = message + tempChar
# 				tempChar = ""
# 			lastBTN = "#"
# 			if(tempChar == ""):
# 				tempChar = "."
# 			elif(tempChar == "."):
# 				tempChar = "?"
# 			elif(tempChar == "?"):
# 				tempChar = "!"
# 			elif(tempChar == "!"):
# 				tempChar = ","
# 			elif(tempChar == ","):
# 				tempChar = "-"
# 			elif(tempChar == "-"):
# 				tempChar = "0"
# 			elif(tempChar == "0"):
# 				tempChar = "."
# 			print(message + tempChar)
# 			timeLimit = time.time()
# # 			speak("tempChar")
# # 		else:
# # 			GPIO.setup(hashBTN,GPIO.LOW)
			
# 		if (time.time() + waitTime) > timeLimit:
# 			timeLimit = 0
# 			message = message + tempChar
# 			tempChar = ""
# 			speak("okay")
# 		ch = ""
		
				   
				   	   
		newButton = getchar()
		newButton = str(newButton)
		if (tempChar != "") and (time.time() >= timeLimit) and (newButton.strip() != "*") and (newButton.strip() != "/") and (newButton.strip() != "="):
				message = message + tempChar
				os.system("espeak '" + message + "' 2>/dev/null")
				tempChar = ""
				print("time set " + message + tempChar)
				timeUp = True
				
		if newButton.strip() == "[":
			message = message + tempChar
			os.system("espeak sending: '" + message + "' 2>/dev/null")
			print("sending: " + message)
			break
		elif newButton.strip() == "]":
			message = message + tempChar
			os.system("espeak 'deleting " +  message[-1] + "' 2>/dev/null")
			tempChar = ""
			message = message[:-1]
			print("new message " + message)
		elif newButton.strip() == "=":
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
				if(tempChar == ""):
					tempChar = "1"
				elif(tempChar == "1"):
					tempChar = "1"
				print(message + tempChar)
			elif newButton == "2":
				GPIO.output(23,GPIO.HIGH)
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
				GPIO.output(23,GPIO.LOW)
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
			elif newButton == "0":
				if(tempChar == ""):
					tempChar = " "
				elif(tempChar == " "):
					tempChar = "."
				elif(tempChar == "."):
					tempChar = "?"
				elif(tempChar == "?"):
					tempChar = "!"
				elif(tempChar == "!"):
					tempChar = ","
				elif(tempChar == ","):
					tempChar = "0"
				elif(tempChar == "0"):
					tempChar = " "
				speak(tempChar)
				print(message + tempChar)
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
		# while True:
		#  	speak("Enter a Phone number")
		# 	phoneNumber = enterPhoneNumber()

		# 	if len(phoneNumber) > 13 or len(phoneNumber) < 10:
		# 		print len(phoneNumber)
		# 		print "Error. Try entering your number in one of the following formatts::" + "\n" + "0637165118 +33637165118 or 0033637165118"
		# 		continue
		# 	else:
		# 		speak("Sending to " + phoneNumber)
		# 		break

		phoneNumber = "0637165118"

		#message = raw_input("Enter Message::\n")
		speak("Enter your message")
		print ("Enter message.\n")
		message = enterMessage()


		#SEND SMS
		print ("Sending text..")
		speak("Sending text")
		modem.send_sms(phoneNumber, message)

		response = m590.ser.readlines(None)
		print (response)
		if response == "":
			speak("Error!")
			print (response)
		elif response[0] == "\n":
			speak("Sent!")
			print ("Sent!")
		else:
			speak("error")
			print (response)

		#READ ALL SMS
		#modem.read_sms(4)
		#print modem.SMS

	modem.deinit()

if __name__ == "__main__":
    main()
