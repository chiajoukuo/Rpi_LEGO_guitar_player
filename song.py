import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)
pwm1=GPIO.PWM(5, 50)
pwm1.start(0)

GPIO.setup(7, GPIO.OUT)
pwm2=GPIO.PWM(7, 50)
pwm2.start(0)

G1, G2 = 0, 50
GB1, GB2 = 37.5, 50
Fm71, Fm72 = 75, 125
C1, C2 = 112.5, 87.5
Am71, Am72 = 75, 87.5

motor1 = [C1, GB1, Fm71, G1,
		  C1, GB1, Fm71, G1, 
		  C1, GB1, Fm71, G1, 
		  C1, GB1, Fm71, G1,
		  C1, Am71, Fm71, G1, 
		  C1, Am71, Fm71, C1,
		  C1, C1, Am71, Fm71,
		  G1, C1, Am71, Fm71,
		  C1, C1, C1, GB1,
		  Fm71, G1, C1, GB1,
		  Fm71, G1, Fm71, C1]

motor2 = [C2, GB2, Fm72, G2,
		  C2, GB2, Fm72, G2, 
		  C2, GB2, Fm72, G2, 
		  C2, GB2, Fm72, G2,
		  C2, Am72, Fm72, G2, 
		  C2, Am72, Fm72, C2,
		  C2, C2, Am72, Fm72,
		  G2, C2, Am72, Fm72,
		  C2, C2, C2, GB2,
		  Fm72, G2, C2, GB2,
		  Fm72, G2, Fm72, C2]

def setAngle1(angle):
	duty = angle / 18 + 2
	GPIO.output(5, True)
	pwm1.ChangeDutyCycle(duty)
	sleep(0.2)
	GPIO.output(5, False)
	pwm1.ChangeDutyCycle(0)

def setAngle2(angle):
	duty = angle / 18 + 2
	GPIO.output(7, True)
	pwm2.ChangeDutyCycle(duty)
	sleep(0.2)
	GPIO.output(7, False)
	pwm2.ChangeDutyCycle(0)

def setAngles(idx):
	duty1 = motor1[idx] / 18 + 2
	duty2 = motor2[idx] / 18 + 2
	GPIO.output(5, True)
	GPIO.output(7, True)
	pwm1.ChangeDutyCycle(duty1)
	pwm2.ChangeDutyCycle(duty2)
	sleep(3)
	# GPIO.output(7, False)
	# pwm1.ChangeDutyCycle(0)
try:
	for idx in range(len(motor1)):
		setAngles(idx)

except KeyboardInterrupt:
    print('stop')
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()



# Chord 
'''
C GB Fm7 G 
C GB Fm7 G 前奏end

C GB Fm7 G
C GB Fm7 G
C Am7 Fm7 G
C Am7 (Fm7 G) C 
C C Am7 Fm7 
G C Am7 (Fm7 G) 
C C C GB
Fm7 G C GB 
Fm7 G (Fm7 G) C


'''