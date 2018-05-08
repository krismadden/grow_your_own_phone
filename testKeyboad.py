import curses

def main(win):
    win.nodelay(False)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
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
