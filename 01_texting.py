from m590_setup import m590
import time

#start setup for text to speach
import sys
import pyttsx
voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', 150)
#end setup for text to speach

#define speak function for text to speach
def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str)
	voiceEngine.runAndWait()
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

def enterPhoneNumber():
	phoneNumber = ""
	while True:
		ch = getchar()
		if ch.strip() == '/':
			print(phoneNumber)
			break
		else:
			phoneNumber = phoneNumber + ch
			print "numbers typed " , len(phoneNumber)
			print 'You pressed', ch
			speak(ch)
	return phoneNumber

def enterMessage():
	tempChar = ""
	oldButton = ""
	message = "Test: "
	waitTime = 2 #in seconds
	timeLimit = time.time() + waitTime
	while True:
		newButton = getchar()
		newButton = str(newButton)
		if newButton.strip() == "/":
			print("sending: " + message)
			print("newButton.strip() == ")
			break
		else:
			if tempChar != "" and time.time() >= timeLimit:
				message = message + tempChar
				tempChar = ""
				timeLimit = time.time() + waitTime
				print("time set " + message + tempChar)
			elif newButton != oldButton and oldButton != "":
				message = "set " + message + tempChar
				tempChar = ""
				timeLimit = time.time() + waitTime
				print("new button set " + message + tempChar)
			else:
				if newButton == "1":
					if(tempChar == ""):
						tempChar = "1"
						timeLimit = time.time() + waitTime
					elif(tempChar == "1"):
						tempChar = "1"
					print(message + tempChar)
				elif newButton == "2":
					if(tempChar == ""):
						tempChar = "a"
						timeLimit = time.time() + waitTime
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
					if(tempChar == ""):
						tempChar = "d"
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
						timeLimit = time.time() + waitTime
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
	return message


response = ""
pin = ""

# speak("Initialising")
print "Initialising Modem & Checking PIN.."

modem = m590()
modem.init()

while True:
	m590.ser.write("at+cpin?\r")
	response = m590.ser.readlines(None)
	print response

	if response[2] == "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
		print "pin okay. let's go."
# 		speak("pin okay. let's go.")
		break
	elif response[2] == "+CPIN: SIM PIN\r\n":
		pin = raw_input("Enter your SIM's PIN code::\n")
		m590.ser.write("at+cpin=\"" + pin + "\"\r")
		time.sleep(0.5)
		continue
	elif response[2] == "+CPIN: SIM PUK\r\n":
		pin = raw_input("Enter your PUK code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	elif response[2] == "+CPIN: SIM PIN2\r\n":
		pin = raw_input("Enter your PIN2 code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	elif response[2] == "+CPIN: SIM PUK2\r\n":
		pin = raw_input("Enter your PUK2 code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	else:
		print response[2] + "\n"
		print "check your SIM card. If all looks good, get Kris."

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
print "Enter message.\n"
message = enterMessage()


#SEND SMS
print "Sending text.."
speak("Sending text")
modem.send_sms(phoneNumber, message)

response = m590.ser.readlines(None)
if response[0] == "\n":
	speak("Sent!")
	print "Sent!"
else:
	speak("error")
	print response

#READ ALL SMS
#modem.read_sms(4)
#print modem.SMS

modem.deinit()
