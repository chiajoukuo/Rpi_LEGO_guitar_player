import RPi.GPIO as GPIO
import time

pwm_freq = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

pwm_s = GPIO.PWM(4, pwm_freq)
pwm_s.start(0)

dc = 20
pwm_s.ChangeDutyCycle(dc)


try:
    while True:
        GPIO.output(17, True)
        GPIO.output(18, False)

except KeyboardInterrupt:
    print('stop')
finally:
    pwm_s.stop()
    GPIO.cleanup()