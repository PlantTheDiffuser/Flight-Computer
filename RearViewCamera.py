from gpiozero import Servo
from time import sleep

#Called only by SystemsCheck.py on startup
def statusCheck():
    return False
name = "Rear View Camera"
#--


servo = Servo(25)
rightSignal = "pin 15"
leftSignal = "pin 14"

if rightSignal == "Hi" :
    servo.max()
    sleep(5)
if leftSignal == "Hi" :
    servo.min()
    sleep(5)
servo.mid()