from gpiozero import Servo
from picamera import piCamera
from time import sleep

#Called only by SystemsCheck.py on startup
def statusCheck():
    return False
name = "Rear View Camera"
#--

camera = piCamera()
servo = Servo(25)
rightSignal = "pin 15"
leftSignal = "pin 14"

if rightSignal == "Hi" :
    camera.start_preview()
    servo.max()
    sleep(5)
    camera.stop_preview()
if leftSignal == "Hi" :
    camera.start_preview()
    servo.min()
    sleep(5)
    camera.start_preview()
servo.mid()

