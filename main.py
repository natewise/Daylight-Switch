import RPi.GPIO as GPIO
from suntime import Sun
from datetime import datetime, timedelta
import time
import pytz

pst=pytz.timezone('US/Pacific')
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
    sunrise = sun.get_sunrise_time().astimezone(pst)
    sunset = sun.get_sunset_time().astimezone(pst)
    if sunrise > sunset: # Bug in API, time is behind
        sunset = sunset + timedelta(days=1)
    now = datetime.now(pst) # Needed for "TypeError: can't compare offset-naive and offset-aware datetimes"
    print("Sunrise:", sunrise.strftime("%m %d %Y %H:%M:%S %Z"),
          "Sunset:", sunset.strftime("%m %d %Y %H:%M:%S %Z"),
          "Now:", now.strftime("%m %d %Y %H:%M:%S %Z"))
    
    if(now >= sunset): # Nighttime
        print("Turning on relay...")
        GPIO.output(12, GPIO.LOW) # Turn on relay (GPIO.LOW because of transistor logic)
    elif(now <= sunset and now >= sunrise): # Daytime
        print("Turning off relay...")
        GPIO.output(12, GPIO.HIGH) # Turn off relay

    time.sleep(600) # Loop every 10 mins/600 seconds

GPIO.cleanup()
  