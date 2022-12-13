from gpiozero import Servo
from time import sleep



def statusCheck():
    return False

name = "Rear View Camera"


servo = Servo(25)

servo.min()
sleep(0.5)
servo.mid()
sleep(0.5)
servo.max()
sleep(0.5)