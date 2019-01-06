__author__="Ben Hart"
__version__="0.1.0"

from gpiozero import PWMOutputDevice
from time import sleep
import curses

PWM_FORWARD_LEFT_PIN = 27
PWM_REVERSE_LEFT_PIN = 22

PWM_FORWARD_RIGHT_PIN = 24
PWM_REVERSE_RIGHT_PIN = 23

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0

def forwardDrive():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 1.0

def reverseDrive():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0

def spinLeft():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 1.0
	reverseRight.value = 0

def SpinRight():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 1.0

def forwardTurnLeft():
	forwardLeft.value = 0.2
	reverseLeft.value = 0
	forwardRight.value = 0.8
	reverseRight.value = 0

def forwardTurnRight():
	forwardLeft.value = 0.8
	reverseLeft.value = 0
	forwardRight.value = 0.2
	reverseRight.value = 0

def reverseTurnLeft():
	forwardLeft.value = 0
	reverseLeft.value = 0.2
	forwardRight.value = 0
	reverseRight.value = 0.8

def reverseTurnRight():
	forwardLeft.value = 0
	reverseLeft.value = 0.8
	forwardRight.value = 0
	reverseRight.value = 0.2

if __name__ == "__main__":

	run_time = 0.1
	while True:
    	key = stdscr.getch()
    	if key == ord('w'):
			forwardDrive()
			sleep(run_time)
		elif key == ord('s'):
			reverseDrive()
			sleep(run_time)
		elif key == ord('a'):
			spinLeft()
			sleep(run_time)
		elif key == ord('d'):
			SpinRight()
			sleep(run_time)
		elif key == ord('q'):
			forwardTurnLeft()
			sleep(run_time)
		elif key == ord('e'):
			forwardTurnRight()
			sleep(run_time)
		elif key == ord('z'):
			reverseTurnLeft()
			sleep(run_time)
		elif key == ord('x'):
			reverseTurnRight()
			sleep(run_time)
		elif key == ord('n'):
			allStop()
			break
		else:
			allStop()


	#end
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
