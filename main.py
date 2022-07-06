import RPi.GPIO as GPIO
from suntime import Sun
from datetime import datetime
import time
import pytz

utc=pytz.UTC

# For Postal Code 92083
latitude = 33.201374
longitude = -117.252914
sun = Sun(latitude, longitude)

# GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

'''
# Test GPIO
high = False
while True:
    print("HIGH" if high else "LOW")
    GPIO.output(12, high)
    high = ~high
    time.sleep(10)
'''
while True:
    sunrise = sun.get_sunrise_time().replace(tzinfo=utc)
    sunset = sun.get_sunset_time().replace(tzinfo=utc)
    now = datetime.now().replace(tzinfo=utc)
    print("Sunrise:", sunrise, "Sunset:", sunset, "Now:", now)

    if(now >= sunset): # Nighttime
        print("Turning on relay...")
        GPIO.output(12, GPIO.LOW) # Turn on relay (GPIO.LOW because of transistor logic)
    elif(now <= sunset and now >= sunrise): # Daytime
        print("Turning off relay...")
        GPIO.output(12, GPIO.HIGH) # Turn off relay

    time.sleep(600) # Loop every 10 mins/600 seconds
 
GPIO.cleanup()
  