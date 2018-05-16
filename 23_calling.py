from m590_setup import m590
import sys
import time
import os
import RPi.GPIO as GPIO
# import keyboard



#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pad1 = 21
pad3 = 20

GPIO.setup(pad1, GPIO.IN)
GPIO.setup(pad3, GPIO.IN)

GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
#end setup for LEDs#




GPIO.setup(26,GPIO.OUT)
p = GPIO.PWM(26,50)


phoneNumber = "0637165118"





#define speak function for text to speach
def speak(str):
	os.system("espeak '" + str + "' 2>/dev/null")
#end of definintion od speak function for text to speach

def vibrate():
	print("vibrate")
	p.start(7.5)
	p.ChangeDutyCycle(12.5)
	time.sleep(0.75)
	p.ChangeDutyCycle(2.5)
	p.stop

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
	vibrate()
	
	checkIfModuleFrozen()
	setUpPin()
	
	outgoingCall = False
	incomingCall = False
	runProgram = True

	
	while runProgram:
# 		if keyboard.is_pressed('space'):
# 			runProgram = False
		#response = m590.ser.readlines(2) #changed monday morning
		response = m590.ser.readlines()
		print (response)
		ringing = False #added monday morning
		
		if len(response) > 1:
			if response[1] == "NO CARRIER\r\n":
				outgoingCall = False
				incomingCall = False
				ringing = False
			while ringing == True or response[1] == "RING\r\n":
				vibrate()
				ringing = True #changed monday morning
				if not GPIO.input(pad1):
					m590.ser.write("ata\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("picking up call")
					incomingCall = True
					ringing = False #added monday morning
					break
				elif not GPIO.input(pad3):
					m590.ser.write("ata\r")
					time.sleep(0.5)
					m590.ser.write("ath\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("Rejecting Call - THIS END")
					incomingCall = False
					ringing = False #added monday morning
					break
				response = m590.ser.readlines() #changed monday morning
				print (response)
				if len(response) > 1:
					if response[1] == "RING\r\n" and len(response) <= 0:
						print len(response)
						vibrate()
					else:
						ringing = False #added monday morning
		if not GPIO.input(pad1) and (ringing == False) and (outgoingCall == False) and (incomingCall == False): #changed monday morning
			print ("placing call")
			m590.ser.write("atd" + phoneNumber +";\r")
			response = m590.ser.readlines() #changed monday morning
			print (response)
			outgoingCall = True
		while outgoingCall == True or incomingCall == True:
			if not GPIO.input(pad3):
				m590.ser.write("ath\r")
				response = m590.ser.readlines() #changed monday morning
				print(response)
				print ("hanging up - THIS END")
				outgoingCall = False
				incomingCall = False
# 			elif keyboard.is_pressed('space'):
# 				runProgram = False
				
			response = m590.ser.readlines() #changed monday morning
			
			if len(response) > 0:
				if response[1] == "NO CARRIER\r\n":
					m590.ser.write("ath\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("hanging up - OTHER END")
					outgoingCall = False
					incomingCall = False
				#is this needed?????????????????????????????????????????????????????????????????????	
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
