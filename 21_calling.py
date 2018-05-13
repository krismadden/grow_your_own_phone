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
	ringing = False
	
	file = open('responses.txt', 'a')
	
	
	while runProgram:
		if keyboard.is_pressed('space'):
			runProgram = False
			
			
# 		response = m590.ser.read(30)
# 		time.sleep(0.5) 
		
	
		while True:
			if m590.ser.inWaiting() > 0:
				break;
			if keyboard.is_pressed('1'):
				break;
			time.sleep(0.05)
		response = m590.ser.read(30)
		print("1" + response + "1")
		
		while response[2:6] == "RING":
			print("fuck yes2")
			
			if keyboard.is_pressed('1'):
				m590.ser.write("ata\r")
				print ("picking up call")
				incomingCall = True
				break
			elif keyboard.is_pressed('0'):
				m590.ser.write("ath\r")
				print ("Rejecting Call - THIS END")
				outgoingCall = False
				incomingCall = False
				break
				
		if keyboard.is_pressed('1') and (outgoingCall == False and incomingCall == False) :
			print ("placing call")
			m590.ser.write("atd" + phoneNumber +";\r")
			outgoingCall = True
			
			callConnected = True
			
			while outgoingCall:
				while True:
					if m590.ser.inWaiting() > 0:
						break;
					if keyboard.is_pressed('0'):
						outgoingCall = False
						break;
					time.sleep(0.05)
				response = m590.ser.read(30)
				print("2" + response + "2")
				if response[2:12] == "NO CARRIER":
					print("fuck yes3")
					outgoingCall = False
				
			
# 		while outgoingCall == True or incomingCall == True:
# 			if keyboard.is_pressed('0'):
# 				m590.ser.write("ath\r")
# 				response = m590.ser.read(None)
# 				print(response)
# 				print ("hanging up - THIS END")
# 				outgoingCall = False
# 				incomingCall = False
# 			elif keyboard.is_pressed('space'):
# 				runProgram = False
# 			response = m590.ser.read(None)
# 			if len(response) > 0:
# 				if response[1] == "NO CARRIER\r\n":
# 					m590.ser.write("ath\r")
# 					response = m590.ser.read(None)
# 					print(response)
# 					print ("hanging up - OTHER END")
# 					outgoingCall = False
# 					incomingCall = False
# 				elif response[0] == "NO CARRIER\r\n":
# 					m590.ser.write("ath\r")
# 					response = m590.ser.read(None)
# 					print(response)
# 					print ("hanging up - OTHER END")
# 					outgoingCall = False
# 					incomingCall = False

	modem.deinit()

if __name__ == "__main__":
    main()
