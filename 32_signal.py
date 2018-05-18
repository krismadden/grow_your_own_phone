import time
# import os
import RPi.GPIO as GPIO
import serial


#setup LEDs#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#left bottom pins near power usb mini after ground
bar1 = 6
bar2 = 13
bar3 = 19
bar4 = 26

GPIO.setup(bar1,GPIO.OUT)
GPIO.setup(bar2,GPIO.OUT)
GPIO.setup(bar3,GPIO.OUT)
GPIO.setup(bar4,GPIO.OUT)

GPIO.output(bar1,GPIO.LOW)
GPIO.output(bar2,GPIO.LOW)
GPIO.output(bar3,GPIO.LOW)
GPIO.output(bar4,GPIO.LOW)

#end setup for LEDs#

bar1max = 10
bar2max = 15
bar3max = 20




ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

def main():
	ser.write("AT+IPR=9600/r")
	time.sleep(0.1)
	response = ser.readlines(None)
	print(response)
	time.sleep(1)
	checkSignalStrength = True
	
	print("checking signal strength")
	
	strength = 0
	
	while checkSignalStrength:
		ser.write("at+CSQ\r")
		response = ser.readlines(None)
		print(response)
		
		if len(response) > 1:
			signal = response[1]
			#+CSQ:18,99
			if len(signal) > 7:
				if signal[7] == ",":
					strength = signal[6]
				elif signal[8] == ",":
					strength = signal[6:8]
				else:
					strength = 0
		if int(strength) > 23:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.HIGH)
			GPIO.output(bar4,GPIO.HIGH)
			print (int(strength))
			print ("4 bars")
		elif int(strength) > 14:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.HIGH)
			GPIO.output(bar4,GPIO.LOW)
			print (strength)
			print ("3 bars")
		elif int(strength) > 8:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print (strength)
			print ("2 bars")
		elif int(strength) > 0:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.LOW)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print (strength)
			print ("1 bar")
		else: 
			GPIO.output(bar1,GPIO.LOW)
			GPIO.output(bar2,GPIO.LOW)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print (strength)
			print ("no bars")
		
		time.sleep(5)
			


if __name__ == "__main__":
    main()
