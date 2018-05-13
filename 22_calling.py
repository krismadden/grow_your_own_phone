from m590_setup import m590
import sys
import time
import os
import RPi.GPIO as GPIO
import keyboard


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


def setUpPin():
	response = ""
	
	print ("Initialising Modem & Checking PIN..")

	while True:
		m590.ser.write("at+cpin=\"1234\"\r")
		time.sleep(0.3)
		m590.ser.write("at+cpin?\r")
		response = m590.ser.readlines(None)
		time.sleep(0.5)
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
	time.sleep(1.0)
	print(response)
	time.sleep(1.0)
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
	
	file = open('responses.txt', 'a')
	
	
	while runProgram:
		if keyboard.is_pressed('space'):
			runProgram = False
# 		m590.ser.write("at/r")
		time.sleep(0.3)
		response = m590.ser.readline(2) # = 
		response2 = m590.ser.readline(3) # = /r/n
		response3 = m590.ser.readline(4) # = RING
		response4 = m590.ser.readline(5) # = /r/n
		print("b " + str(response) + "." + str(response2) + "." + str(response3) + "." + str(response4) + " e")
		response = m590.ser.readlines(10)
		print (response)
		
		if m590.ser.readline(4):
			while m590.ser.readline(4) == "RING":
				print ("Incoming Call")
				if keyboard.is_pressed('1'):
					m590.ser.write("ata\r")
					response = m590.ser.read(None)
					print(response)
					print ("picking up call")
					incomingCall = True
					break
				elif keyboard.is_pressed('0'):
					m590.ser.write("ath\r")
					response = m590.ser.read(None)
					print(response)
					print ("Rejecting Call - THIS END")
					outgoingCall = False
					incomingCall = False
					break
		if len(response) > 1:
			while response[1] == "RING\r\n":
				if keyboard.is_pressed('1'):
					m590.ser.write("ata\r")
					response = m590.ser.read(None)
					print(response)
					print ("picking up call")
					incomingCall = True
				elif keyboard.is_pressed('0'):
					m590.ser.write("ath\r")
					response = m590.ser.read(None)
					print(response)
					print ("Rejecting Call - THIS END")
					outgoingCall = False
					incomingCall = False
		if keyboard.is_pressed('1'):
			print ("placing call")
			m590.ser.write("atd" + phoneNumber +";\r")
			response = m590.ser.read(None)
			print (response)
			count = 0
			print ("1 - " + str(count))
			outgoingCall = True
		while outgoingCall == True or incomingCall == True:
			if keyboard.is_pressed('0'):
				m590.ser.write("ath\r")
				response = m590.ser.read(None)
				print(response)
				print ("hanging up - THIS END")
				outgoingCall = False
				incomingCall = False
			elif keyboard.is_pressed('space'):
				runProgram = False
			response = m590.ser.read(None)
			if len(response) > 0:
				if response[1] == "NO CARRIER\r\n":
					m590.ser.write("ath\r")
					response = m590.ser.read(None)
					print(response)
					print ("hanging up - OTHER END")
					outgoingCall = False
					incomingCall = False
				elif response[0] == "NO CARRIER\r\n":
					m590.ser.write("ath\r")
					response = m590.ser.read(None)
					print(response)
					print ("hanging up - OTHER END")
					outgoingCall = False
					incomingCall = False

	modem.deinit()

if __name__ == "__main__":
    main()
