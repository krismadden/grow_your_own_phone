from m590_setup import m590
import os, pygame, sys, time, math
import RPi.GPIO as GPIO
from pygame.locals import *

#not sure if i need this... if so add the file to github
#from pygame_functions import *

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

def checkIfModuleFrozen():
	m590.ser.write("at\r".encode())
	time.sleep(1.0)
	response = m590.ser.readlines(None)
	print(response)
	response = response[1].decode()
	if response == "":
		print ("response not okay")
		print (response)
		os.system('sudo shutdown -r now') #does not work. just freezes the program.
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
	waitTime = 2 #in seconds
	timeUp = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				print(self.input)
			if event.key == pygame.K_ESCAPE:
				self.quit()
			if event.key == K_1:
				speak("1")
			elif event.key == K_2:
				speak("2")
			elif event.key == K_3:
				speak("3")
			elif event.key == K_4:
				speak("4")
			elif event.key == K_5:
				speak("5")
			elif event.key == K_6:
				speak("6")
			elif event.key == K_7:
				speak("7")
			elif event.key == K_8:
				speak("8")
			elif event.key == K_9:
				speak("9")
			elif event.key == K_0:
				speak("0")
			elif event.key == K_LEFTBRACKET:
				speak("Send / Enter")
			elif event.key == K_RIGHTBRACKET:
				speak("Backspace")
			elif event.key == K_EQUALS:
				speak("play back")
			else:
				speak("Something else")
			
			
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
