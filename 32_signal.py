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

bar1max = 8
bar2max = 10
bar3max = 12




ser = serial.Serial("/dev/ttyAMA0", 12800, timeout=0.5)

def main():
	
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
			if signal[6] == ",":
				strength = signal[5]
			elif signal[7] == ",":
				strength = signal[5:7]
			else:
				strength = 0
		if strength > bar3max:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.HIGH)
			GPIO.output(bar4,GPIO.HIGH)
			print ("4 bars")
		elif strength > bar2max:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.HIGH)
			GPIO.output(bar4,GPIO.LOW)
			print ("3 bars")
		elif strength > bar1max:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.HIGH)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print ("2 bars")
		elif strength > 0:
			GPIO.output(bar1,GPIO.HIGH)
			GPIO.output(bar2,GPIO.LOW)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print ("1 bar")
		else: 
			GPIO.output(bar1,GPIO.LOW)
			GPIO.output(bar2,GPIO.LOW)
			GPIO.output(bar3,GPIO.LOW)
			GPIO.output(bar4,GPIO.LOW)
			print ("no bars")
		
		time.sleep(5)
			


if __name__ == "__main__":
    main()