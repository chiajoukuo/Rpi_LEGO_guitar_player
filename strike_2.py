import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
pwm_s = GPIO.PWM(17,500)
pwm_s.start(0)
pwm_s.ChangeDutyCycle(100)

try:
    while True:
        GPIO.output(17, True)
        GPIO.output(18, False)

except KeyboardInterrupt:
    print('stop')
finally:
    pwm.stop()
    GPIO.cleanup()