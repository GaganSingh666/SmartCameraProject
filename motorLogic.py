import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin1 = [7,11,13,15]
ControlPin2 = [12,16,18,22]
"""
for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.optput(pin,0)
"""

"""
for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
        time.sleep(0.001)

GPIO.cleanup()
"""

seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,0]]
rev = [[1,0,0,0],[0,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0],[1,0,0,0]]
#control for motor 1

def setUpMotor1():
    GPIO.setmode(GPIO.BOARD)
    for pin in ControlPin1:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)

def setUpMotor2():
    GPIO.setmode(GPIO.BOARD)
    for pin in ControlPin2:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)

def moveRight():
    setUpMotor1()
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin1[pin], seq[halfstep][pin])
            time.sleep(0.001)
    GPIO.cleanup()

def moveLeft():
    setUpMotor1()
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin1[pin], rev[halfstep][pin])
            time.sleep(0.001)
    GPIO.cleanup()
#control for motor 2
def moveUp():
    setUpMotor2()
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin2[pin], seq[halfstep][pin])
            time.sleep(0.001)
    GPIO.cleanup()

def moveDown():
    setUpMotor2()
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin2[pin], rev[halfstep][pin])
            time.sleep(0.001)
    GPIO.cleanup()


