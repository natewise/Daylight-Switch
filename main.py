import RPi.GPIO as GPIO
# from suntime import Sun
from datetime import datetime
import time

# For Postal Code 92083
latitude = 33.201374
longitude = -117.252914
# sun = Sun(latitude, longitude)

# GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

high = False
while True:
    print("HIGH" if high else "LOW")
    GPIO.output(12, high)
    high = ~high
    time.sleep(10)

'''
while True:
	sunrise = sun.get_sunrise_time()
	sunset = sun.get_sunset_time()
	now = datetime.now()
	
	if(now >= sunset): # Nighttime
		GPIO.output(18, GPIO.HIGH) # Turn on relay
	elif(now <= sunset and now >= sunrise): # Daytime
		GPIO.output(18, GPIO.LOW) # Turn off relay
	
	time.sleep(600) # Loop every 10 mins/600 seconds
'''
GPIO.cleanup()
