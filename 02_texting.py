from m590_setup import m590
import time
import os
import RPi.GPIO as GPIO

#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
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
		m590.ser.write("at+cpin=\"1234\"\r".encode())
		m590.ser.write("at+cpin?\r".encode())
		response = m590.ser.readlines(None)
		print (response)

		if response[0].decode() == "OK\r\n" or response[1].decode() == "OK\r\n" or response[2].decode() == "OK\r\n":
			print ("pin okay. let's go.")
	# 		speak("pin okay. let's go.")
			break
		elif response[2].decode() != "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
			print ("pin okay. let's go.")
	# 		speak("pin okay. let's go.")
			break
		elif response[2].decode() == "+CPIN: SIM PIN\r\n":
			m590.ser.write("at+cpin=\"1234\"\r".encode())
			time.sleep(0.5)
			continue
		elif response[1].decode() == "ERROR/r/n" or response[2].decode() == "ERROR/r/n":
			print (response[1].decode() + "\n")
			print ("Error. Restart the Module")
		else:
			print (response[1].decode() + "\n")
			print ("check your SIM card is inserted and the light on the GSM module is flashing./nIf all looks good, get Kris.")

	

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
	waitTime = 2 #in seconds
	timeUp = False
	while True:
		
		newButton = getchar()
		newButton = str(newButton)
		if (tempChar != "") and (time.time() >= timeLimit) and (newButton.strip() != "*") and (newButton.strip() != "/") and (newButton.strip() != "="):
				message = message + tempChar
				os.system("espeak '" + message + "' 2>/dev/null")
				tempChar = ""
				print("time set " + message + tempChar)
				timeUp = True
				
		if newButton.strip() == "/":
			message = message + tempChar
			os.system("espeak sending: '" + message + "' 2>/dev/null")
			print("sending: " + message)
			break
		elif newButton.strip() == "*":
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
					os.system("espeak 'new button " + message + "' 2>/dev/null")
					tempChar = ""
					print("new button set " + message + tempChar)
			if newButton == "1":
				if(tempChar == ""):
					tempChar = "1"
				elif(tempChar == "1"):
					tempChar = "1"
				print(message + tempChar)
			elif newButton == "2":
				GPIO.output(18,GPIO.HIGH)
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
				print(message + tempChar)
			elif newButton == "3":
				GPIO.output(18,GPIO.LOW)
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
	
	setUpPin()

	while True:
		
		m590.ser.write("at\r".encode())
		time.sleep(1.0)
		response = m590.ser.readlines(None)
		print(response)
		response = response[1].decode()
		print(response)
		if response != "OK" or response != "+PBREADY" or response != "ERROR":
			print ("response not okay")
			print (response)
			#os.system('sudo shutdown -r now')
		else:
			print (response)
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
		if response[0].decode() == "\n":
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
