import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
pwm_s = GPIO.PWM(3,500)
pwm_s.start(0)


try:
    while True:
        GPIO.output(11, True)
        GPIO.output(12, False)
        pwm_s.ChangeDutyCycle(120)

except KeyboardInterrupt:
    print('stop')
finally:
    pwm_s.stop()
    GPIO.cleanup()