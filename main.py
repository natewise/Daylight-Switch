import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import time
import pytz

pst=pytz.timezone('US/Pacific')
sunrise = datetime.now(pst).replace(hour=7, minute=0, second=0) # 7am
sunset = sunrise + timedelta(hours=12) # 7pm 

# GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
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
  