from m590_setup import m590
import sys
import time
import os
import RPi.GPIO as GPIO
import keyboard

from threading import Thread, Event
import time



#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sendBTN = 13
endBTN = 19

GPIO.setup(sendBTN,GPIO.OUT)
GPIO.setup(endBTN,GPIO.OUT)

GPIO.output(sendBTN,GPIO.LOW)
GPIO.output(endBTN,GPIO.LOW)

# pad1 = 21
# pad3 = 20

# GPIO.setup(pad1, GPIO.IN)
# GPIO.setup(pad3, GPIO.IN)

GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
#end setup for LEDs#





GPIO.setup(26,GPIO.OUT)
p = GPIO.PWM(26,50)


phoneNumber = "0637165118"


stop_it = Event()




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

	i = 0
	while True:
		i += 1
		print(i)
		time.sleep(1)
	
		if stop_it.is_set():
	    		break

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
		if len(response) > 0:
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
	
	response1 = ""
	response2 = ""
	response3 = ""
	response4 = ""
	response5 = ""
	response6 = ""
	response7 = ""
	response8 = ""
	response9 = ""
	response10 = ""

	
	while runProgram:
		ch = getchar()
# 		if keyboard.is_pressed('space'):
# 			runProgram = False
		#response = m590.ser.readlines(2) #changed monday morning
		response = m590.ser.readlines()
		print (response)
		ringing = False #added monday morning
		
		
		if len(response) > 1:
			ch = getchar()
			if response[1] == "NO CARRIER\r\n":
				outgoingCall = False
				incomingCall = False
				ringing = False
			while len(response) > 1 and (ringing == True or response[1] == "RING\r\n"):
				ch = getchar()
				response = m590.ser.readlines() #changed monday morning
				ringing = True #changed monday morning
				if ch == '9':
					GPIO.output(sendBTN,GPIO.HIGH)
					m590.ser.write("ata\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("picking up call")
					speak("answering call")
					incomingCall = True
					ringing = False #added monday morning
					time.sleep(0.5)
					GPIO.output(sendBTN,GPIO.LOW)
					break
				elif ch == '8':
					GPIO.output(endBTN,GPIO.HIGH)
					m590.ser.write("ata\r")
					time.sleep(0.5)
					m590.ser.write("ath\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("Rejecting Call - THIS END")
					speak("rejecting call")
					incomingCall = False
					ringing = False #added monday morning
					time.sleep(0.5)
					GPIO.output(endBTN,GPIO.LOW)
					break
				response10 = response9
				response9 = response8
				response8 = response7
				response7 = response6
				response6 = response5
				response5 = response4
				response4 = response3
				response3 = response2
				response2 = response1
				response1 = response
				print("response1: " + str(response1))
				print("response2: " + str(response2))
				print("response3: " + str(response3))
				print("response4: " + str(response4))
				print("response5: " + str(response5))
				print("response6: " + str(response6))
				print("response7: " + str(response7))
				vibrate()
				if (len(response1) > 1 and response1[1] == "RING\r\n") or (len(response2) > 1 and response2[1] == "RING\r\n") or (len(response3) > 1 and response3[1] == "RING\r\n") or (len(response4) > 1 and response4[1] == "RING\r\n") or (len(response5) > 1 and response5[1] == "RING\r\n") or (len(response6) > 1 and response6[1] == "RING\r\n") or (len(response7) > 1 and response7[1] == "RING\r\n") or (len(response8) > 1 and response8[1] == "RING\r\n") or (len(response9) > 1 and response9[1] == "RING\r\n") or (len(response10) > 1 and response10[1] == "RING\r\n"):
					ringing = True
				else:
					ringing = False #added monday morning
		if ch == '9' and (ringing == False) and (outgoingCall == False) and (incomingCall == False): #changed monday morning
			GPIO.output(sendBTN,GPIO.HIGH)
			print ("placing call")
			speak("calling")
			m590.ser.write("atd" + phoneNumber +";\r")
			response = m590.ser.readlines() #changed monday morning
			print (response)
			outgoingCall = True
			time.sleep(0.5)
			GPIO.output(sendBTN,GPIO.LOW)
		while outgoingCall == True or incomingCall == True:
			ch = getchar()
			if ch == '8':
				GPIO.output(endBTN,GPIO.HIGH)
				m590.ser.write("ath\r")
				response = m590.ser.readlines() #changed monday morning
				print(response)
				print ("hanging up - THIS END")
				speak("hanging up")
				outgoingCall = False
				incomingCall = False
				time.sleep(0.5)
				GPIO.output(endBTN,GPIO.LOW)
# 			elif keyboard.is_pressed('space'):
# 				runProgram = False
				
			response = m590.ser.readlines() #changed monday morning
			
			if len(response) > 0:
				if response[1] == "NO CARRIER\r\n":
					m590.ser.write("ath\r")
					response = m590.ser.readlines() #changed monday morning
					print(response)
					print ("hanging up - OTHER END")
					speak("Hanging up")
					outgoingCall = False
					incomingCall = False
				#is this needed?????????????????????????????????????????????????????????????????????	
				elif response[0] == "NO CARRIER\r\n":
					m590.ser.write("ath\r")
					response = m590.ser.read(None)
					print(response)
					print ("hanging up - OTHER END")
					speak("Hanging up")
					outgoingCall = False
					incomingCall = False

	modem.deinit()

if __name__ == "__main__":
	main()
	# Create a thread that needs to run for 5 seconds
	stuff_doing_thread = Thread(target=getchar)

	stuff_doing_thread.start()
	stuff_doing_thread.join(timeout=.05)

	stop_it.set()

