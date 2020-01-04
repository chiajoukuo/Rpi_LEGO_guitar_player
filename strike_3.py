import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
pwm_s = GPIO.PWM(11,500)
pwm_s.start(0)
pwm_s.ChangeDutyCycle(0.2)

try:
    while True:
        GPIO.output(11, True)
        GPIO.output(12, False)

except KeyboardInterrupt:
    print('stop')
finally:
    pwm_s.stop()
    GPIO.cleanup()