import RPi.GPIO as GPIO
import dht11
import time
# intialise GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

segments = (6, 19, 25, 12, 20, 26, 23, 21)

for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 0)

digits = (16, 13, 5)

for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, 1)

num = {' ':(0, 0, 0, 0, 0, 0, 0),
        '0':(1, 1, 1, 1, 1, 1, 0),
        '1':(0, 1, 1, 0, 0, 0, 0),
        '2':(1, 1, 0, 1, 1, 0, 1),
        '3':(1, 1, 1, 1, 0, 0, 1),
        '4':(0, 1, 1, 0, 0, 1, 1),
        '5':(1, 0, 1, 1, 0, 1, 1),
        '6':(1, 0, 1, 1, 1, 1, 1),
        '7':(1, 1, 1, 0, 0, 0, 0),
        '8':(1, 1, 1, 1, 1, 1, 1),
        '9':(1, 1, 1, 1, 0, 1, 1)}


while True:
	instance = dht11.DHT11(pin = 22)
	result = instance.read()
	if result.is_valid():
	#if(1): 
		#result1 = str(470)
		result1 = str(result.temperature * 10).rjust(3)
		print("Temperature: %-3.1f C" % result.temperature, "Humidity: %-3.1f %%" % result.humidity, end = "\r")
		print(result1)
		for i in range(200):
			for digit in range(3):
				for loop in range(0, 7):
					GPIO.output(segments[loop], num[result1[digit]][loop])
				if digit == 1:	
					GPIO.output(21, 1)
				else:
					GPIO.output(21, 0)

				GPIO.output(digits[digit], 0)
				time.sleep(0.001)
				GPIO.output(digits[digit], 1)

