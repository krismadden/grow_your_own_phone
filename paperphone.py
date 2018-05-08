#!/usr/bin/python

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

letter = ""
message = ""
number = ""
numberstring = ""
number_kris = "0033637165118"
response = ""
pin = ""

print "Initialising Modem & Checking PIN.."
speak("Initialising Modem & Checking PIN")

modem = m590()
modem.init()

while True:
	m590.ser.write("at+cpin?\r")
	response = m590.ser.readlines(None)
	print response

	if response[2] == "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
		print "pin okay. let's go."
		speak("pin okay. let's go.")
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

while True:
	speak("Enter a Phone number")
	number = raw_input("Enter Phone number::\n")

	if number == "Kris" or number == "kris" or number == "KRIS":
		number = number_kris
		speak("texting kris")
		print "texting kris..."
		break
	elif len(number) > 13 or len(number) < 10:
		print "Error. Try entering your number in one of the following formatts::" + "\n" + "0637165118 +33637165118 or 0033637165118"
		continue
	else:
		break

#message = raw_input("Enter Message::\n")
speak("Enter your message")
print "Enter message.\n- Press 2-9 for letters.\n- Enter 0 for spaces and punctuation.\n- Press enter after each character.\n- Enter 01 as the last character to send."
while True:
    letter = raw_input("Message = " + message + "\n")

    if letter == "2":
        message = message + "a"
    elif letter == "22":
        message = message + "b"
    elif letter == "222":
        message = message + "c"
    elif letter == "2222":
        message = message + "2"

    elif letter == "3":
        message = message + "d"
    elif letter == "33":
        message = message + "e"
    elif letter == "333":
        message = message + "f"
    elif letter == "3333":
        message = message + "3"

    elif letter == "4":
        message = message + "g"
    elif letter == "44":
        message = message + "h"
    elif letter == "444":
        message = message + "i"
    elif letter == "4444":
        message = message + "4"

    elif letter == "5":
        message = message + "j"
    elif letter == "55":
        message = message + "k"
    elif letter == "555":
        message = message + "l"
    elif letter == "5555":
        message = message + "5"

    elif letter == "6":
        message = message + "m"
    elif letter == "66":
        message = message + "n"
    elif letter == "666":
        message = message + "o"
    elif letter == "6666":
        message = message + "6"

    elif letter == "7":
        message = message + "p"
    elif letter == "77":
        message = message + "q"
    elif letter == "777":
        message = message + "r"
    elif letter == "7777":
        message = message + "s"
    elif letter == "77777":
        message = message + "7"

    elif letter == "8":
        message = message + "t"
    elif letter == "88":
        message = message + "u"
    elif letter == "888":
        message = message + "v"
    elif letter == "8888":
        message = message + "8"

    elif letter == "9":
        message = message + "w"
    elif letter == "99":
        message = message + "x"
    elif letter == "999":
        message = message + "y"
    elif letter == "9999":
        message = message + "z"
    elif letter == "99999":
        message = message + "9"

    elif letter == "0":
        message = message + " "
    elif letter == "00":
        message = message + "."
    elif letter == "000":
        message = message + "?"
    elif letter == "0000":
        message = message + "!"
    elif letter == "00000":
        message = message + "0"

    elif letter == "1":
        message = message + "1"
        #break

    elif letter == "01":
        print "Sending: " + message
	speak(message)
        break

    else:
        print "\"" + letter + "\" is not recognized. Try again."
	speak("\"" + letter + "\" is not recognized. Try again.")

    continue


#SEND SMS
print "Sending text.."
speak("Sending text")
modem.send_sms(number, message)

response = m590.ser.readlines(None)
if response[0] == "\n":
	print "Sent!"
	speak("Sent!")
else:
	print response

#READ ALL SMS
#modem.read_sms(4)
#print modem.SMS

modem.deinit()
