

import curses


import sys
import pyttsx

voiceEngine = pyttsx.init()
voiceEngine.setProperty('rate', 150)

def speak(str):
	if len(sys.argv) > 1:
		str = sys.argv[1]
	voiceEngine.say(str)
	voiceEngine.runAndWait()


def main(stdscr):
    stdscr.nodelay(True)
    key=""
    stdscr.clear()                
    stdscr.addstr("Detected key:")
    while 1:          
        try:                 
           key = stdscr.getkey()         
           stdscr.clear()                
           stdscr.addstr("Detected key:")
           stdscr.addstr(str(key)) 
           speak(str(key))
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)


# import curses  
# while True:
#     try: #used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):#if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break#finishing the loop
#         else:
#             pass
#     except:
#         break #if user pressed a key other than the given key the loop will break
