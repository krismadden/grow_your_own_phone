
import time
import os
import RPi.GPIO as GPIO
import serial




def setUpPin():
	response = ""
	pin = ""

	# speak("Initialising")
	print ("Initialising Modem & Checking PIN..")

	while True:
		pin = "1234"
		ser.write("at+cpin=\"1234\"\r")
		time.sleep(0.3)
		ser.write("at+cpin?\r")
		response = ser.readlines(None)
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
			ser.write("at+cpin=\"1234\"\r")
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
	ser.write("at\r")
	time.sleep(1.0)
	response = ser.readlines(None)
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
	

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=5.0)

def main():
	
	checkIfModuleFrozen()
	setUpPin()

	while True:
		ser.write("at+CSQ\r")
		time.sleep(1.0)
		response = ser.readlines(None)
	
	modem.deinit()

if __name__ == "__main__":
    main()
