from m590_setup import m590
import sys
import time
import os
import RPi.GPIO as GPIO

#not sure if i need this... if so add the file to github
#from pygame_functions import *

#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
#end setup for LEDs#




phoneNumber = "0637165118"





#define speak function for text to speach
def speak(str):
	os.system("espeak '" + str + "' 2>/dev/null")
#end of definintion od speak function for text to speach

def getChar():
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
	
	print ("Initialising Modem & Checking PIN..")

	while True:
		m590.ser.write("at+cpin=\"1234\"\r")
		time.sleep(0.3)
		m590.ser.write("at+cpin?\r")
		response = m590.ser.readlines(None)
		print (response)

		if response[0] == "OK\r\n" or response[1] == "OK\r\n" or response[2] == "OK\r\n":
			print ("pin okay. let's go.")
			break
		elif response[1] == "+CPIN: READY\r\n" or response[2] != "+CPIN: READY\r\n":
			print ("pin okay. let's go.")
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
		

def main():
	modem = m590()
	modem.init()
	
	checkIfModuleFrozen()
	setUpPin()
	
	outgoingCall = False
	incomingCall = False
	runProgram = True
	
	while runProgram:
		ch = getChar()
		if ch.strip() == "1":
			print (ch)
			print (ch.strip())
			print ("placing call")
			m590.ser.write("atd" + phoneNumber +";\r")
			response = m590.ser.readlines(None)
			print (response)
			count = 0
			print ("1 - " + str(count))
			outgoingCall = True
		while outgoingCall:
			ch = getChar()
			print (ch)
			if ch == "0":
				print ("4 - ")
				m590.ser.write("ath\r")
				response = m590.ser.readlines(None)
				print(response)
				print ("hanging up - THIS END")
				outgoingCall = False
			elif ch == "/":
				print ("5 - ")
				runProgram = False
			print ("2 - ")
# 				m590.ser.write("AT+CLCC\r")
			response = m590.ser.readlines(None)
			print (response)
			if len(response) > 0:
				if response[1] == "NO CARRIER\r\n":
					print ("3 - ")
					m590.ser.write("ath\r")
					response = m590.ser.readlines(None)
					print(response)
					print ("hanging up - OTHER END")
					outgoingCall = False

	modem.deinit()

if __name__ == "__main__":
    main()
