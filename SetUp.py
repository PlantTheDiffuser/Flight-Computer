#SetUp.py is where all predetermined race info goes
#To be set up before race start

#Explination of all files
""""
SystemsCheck.py - Program that runs on startup to display a check on all systems
DRS.py - Controller that manages rear wing DRS system
HeadsUpDisplay.py - Controller that manages a heads up display mounted in the dash in front of the driver
NitrousOxide.py - Controller that manages the Nitrous oxide injection system
RearViewCamera.py - Controller that manages the camera mounted in the rear of the car
ScoutDrones.py - Controller that manages the system of drones mounted in the roof used for reconnaissance
SideViewCamera.py - Controller that manages cameras mounted to the side of the car to replace the existing side view mirrors
WaterBottle.py - Controller that manages the driver hydration system
"""

TotalLaps = 10
#Number of laps for race
#Ignored if qualifying != 0
#0 = Not racing

qualifying = 0
#0 = Race, 
#1 = Q1
#2 = Q2
#3 = Q3

strat = 6
#strat 1 = 
#strat 2 = 
#strat 3 = 
#strat 4 = 
#strat 5 = 
#strat 6 = Driver Default

brakeBias = 62
#The percent of brake pressure that goes to the front brakes
#62 = 62% brake pressure goes to front brakes, 38% goes to rear brakes