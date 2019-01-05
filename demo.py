__author__="Ben Hart"
__version__="0.1.0"

from gpiozero import PWMOutputDevice
from time import sleep

PWM_FORWARD_LEFT_PIN = 27
PWM_REVERSE_LEFT_PIN = 22

PWM_FORWARD_RIGHT_PIN = 24
PWM_REVERSE_RIGHT_PIN = 23

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0

def forwardDrive():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0

def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 1.0

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


run_time = 2
def main():
	allStop()
	forwardDrive()
	sleep(run_time)
	reverseDrive()
	sleep(run_time)
	spinLeft()
	sleep(run_time)
	SpinRight()
	sleep(run_time)
	forwardTurnLeft()
	sleep(run_time)
	forwardTurnRight()
	sleep(run_time)
	reverseTurnLeft()
	sleep(run_time)
	reverseTurnRight()
	sleep(run_time)
	allStop()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
