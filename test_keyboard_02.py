import sys
import pyttsx

voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', 150)

message = ""

def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str)
	voiceEngine.runAndWait()

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
   
while 1:
	ch = getchar()
	if ch.strip() == '':
		print('bye!')
		speak("bye")
		break
	if ch.strip() == '=':
		speak(message)

	else:
		print 'You pressed', ch
		speak(ch)
		message = message + ch
