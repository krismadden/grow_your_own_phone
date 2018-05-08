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

phoneNumber = ""
def enterPhoneNumber():
	phoneNumber = ""
	while 1:
		ch = getchar()
		if ch.strip() == '':
			print(phoneNumber)
# 			speak("Sending to " + phoneNumber)
			break
		else:
			print 'You pressed', ch
			speak(ch)
			phoneNumber = phoneNumber + ch
	
	
	
letter = ""
message = ""
number = ""
numberstring = ""
number_kris = "0033637165118"
response = ""
pin = ""

speak("Initialising")
print "Initialising Modem & Checking PIN.."

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
# 	number = raw_input("Enter Phone number::\n")
	enterPhoneNumber()

	if len(phoneNumber) > 13 or len(phoneNumber) < 10:
		print "Error. Try entering your number in one of the following formatts::" + "\n" + "0637165118 +33637165118 or 0033637165118"
		continue
	else:
		speak("Sending to " + phoneNumber)
		break

#message = raw_input("Enter Message::\n")
speak("Enter your message")
print "Enter message.\n- Press 2-9 for letters.\n- Enter 0 for spaces and punctuation.\n- Press enter after each character.\n- Enter 01 as the last character to send."
while True:
    letter = raw_input("Message = " + message + "\n")

    if letter == "2":
	speak("a")
        message = message + "a"
    elif letter == "22":
        speak("b")
	message = message + "b"
    elif letter == "222":
        speak("c")
	message = message + "c"
    elif letter == "2222":
        speak("2")
	message = message + "2"

    elif letter == "3":
        speak("d")
	message = message + "d"
    elif letter == "33":
        speak("e")
	message = message + "e"
    elif letter == "333":
        speak("f")
	message = message + "f"
    elif letter == "3333":
        speak("3")
	message = message + "3"

    elif letter == "4":
        speak("g")
	message = message + "g"
    elif letter == "44":
        speak("h")
	message = message + "h"
    elif letter == "444":
        speak("i")
	message = message + "i"
    elif letter == "4444":
        speak("4")
	message = message + "4"

    elif letter == "5":
        speak("j")
	message = message + "j"
    elif letter == "55":
        speak("k")
	message = message + "k"
    elif letter == "555":
        speak("l")
	message = message + "l"
    elif letter == "5555":
        speak("5")
	message = message + "5"

    elif letter == "6":
        speak("m")
	message = message + "m"
    elif letter == "66":
        speak("n")
	message = message + "n"
    elif letter == "666":
        speak("o")
	message = message + "o"
    elif letter == "6666":
        speak("6")
	message = message + "6"

    elif letter == "7":
        speak("p")
	message = message + "p"
    elif letter == "77":
        speak("q")
	message = message + "q"
    elif letter == "777":
        speak("r")
	message = message + "r"
    elif letter == "7777":
        speak("s")
	message = message + "s"
    elif letter == "77777":
        speak("7")
	message = message + "7"

    elif letter == "8":
        speak("t")
	message = message + "t"
    elif letter == "88":
        speak("u")
	message = message + "u"
    elif letter == "888":
        speak("v")
	message = message + "v"
    elif letter == "8888":
        speak("8")
	message = message + "8"

    elif letter == "9":
        speak("w")
	message = message + "w"
    elif letter == "99":
        speak("x")
	message = message + "x"
    elif letter == "999":
        speak("y")
	message = message + "y"
    elif letter == "9999":
        speak("z")
	message = message + "z"
    elif letter == "99999":
        speak("9")
	message = message + "9"

    elif letter == "0":
        speak("space")
	message = message + " "
    elif letter == "00":
        speak("period")
	message = message + "."
    elif letter == "000":
        speak("question mark")
	message = message + "?"
    elif letter == "0000":
        speak("exclamation mark")
	message = message + "!"
    elif letter == "00000":
        speak("0")
	message = message + "0"

    elif letter == "1":
        message = message + "1"
        #break

    elif letter == "01":
	speak(message)
        print "Sending: " + message
        break

    else:
	speak("\"" + letter + "\" is not recognized. Try again.")
        print "\"" + letter + "\" is not recognized. Try again."

    continue


#SEND SMS
print "Sending text.."
speak("Sending text")
modem.send_sms(number, message)

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
