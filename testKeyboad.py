import curses

while True:
	try:
		if keyboard.is_pressed('q'):
			print("You pressed a key!!!")
			break
		else:
			pass
	except: break
