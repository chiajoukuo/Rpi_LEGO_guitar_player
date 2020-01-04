import RPi.GPIO as GPIO
import time
# import curses
# from curses import wrapper

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# stdscr = curses.initscr()
# stdscr.clear()
# while True:
#     ch = stdscr.getkey()

#     if ch == 'q':
#         curses.endwin()
#         GPIO.output(17, False)
#         GPIO.output(18, False)
#         break
#     if ch == 'x':
#         GPIO.output(17, False)
#         GPIO.output(18, False)
try:
    while True:
        GPIO.output(17, True)
        GPIO.output(18, False)
except KeyboardInterrupt:
    print(stop)
finally:
    GPIO.cleanup()