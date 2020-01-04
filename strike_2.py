import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(17, True)
        GPIO.output(18, False)

except KeyboardInterrupt:
    print('stop')
finally:
    GPIO.cleanup()