import time

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


def enterMessage():
	message = ""
  submitCharacter = False
	while True:
		ch = getchar()
		if ch.strip() == '':
			print(phoneNumber)
			break
		else:
      time1 = time.time()
      time2 = time1 + timeConstrant
      while submitCharacter:
        if(time.time() > time2):
          message = message + ch
          submitCharacter = True
          break
        else:
          
          
          
          
          continue
# 			phoneNumber = phoneNumber + ch
# 			print "numbers typed " , len(phoneNumber)
# 			print 'You pressed', ch
# 			speak(ch)
	return message
	
	
