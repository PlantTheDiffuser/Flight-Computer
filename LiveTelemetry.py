import tkinter as tk
import tkinter.ttk as ttk
import SetUp
import random
import time

##Start after systems check

TotalLaps = SetUp.TotalLaps
Lap = 0
qualifying = SetUp.qualifying
LapTimes = [0] * TotalLaps

##TESTING LAP BUTTON
def lapButtonPressed():
    global LapButtonPressed
    LapButtonPressed = True
    w.update()
    time.sleep(1)
    LapButtonPressed = False

def updateThrottle():
    throttle['value'] = random.randint(0, 100) #get throttle value
    w.after(1, updateThrottle)
def updateBrake():
    brake['value'] = random.randint(0, 100) #get brake value
    w.after(1, updateBrake)

def lapTimeToString(lapTime):
    lapTimeS = int((lapTime / 1000) % 60)
    lapTimeMS = int(lapTime % 1000)
    lapTimeM = int(lapTime / 60000)
    return ("%02d:%02d.%03d" % (lapTimeM, lapTimeS, lapTimeMS))

currentLapTime = 0
def updateLap():
    global Lap
    if qualifying != 0:
        lap['text'] = ("Q%d" % (qualifying))
        return
    if TotalLaps == 0 or Lap == TotalLaps:
        return
    if Lap == 0:
        Lap = 1
        updateCurrentLap()
        lap['text'] = ("LAP %d/%d" % (Lap, TotalLaps))
        return
    LapTimes[Lap - 1] = currentLapTime
    Lap += 1
    lap['text'] = ("LAP %d/%d" % (Lap, TotalLaps))
    t1 = updateLastLap()
    t2 = updateBestLap()
    updateCurrentLap(True)
    if t1 == t2:
        lastLap['fg'] = "purple"
        bestLap['fg'] = "purple"
    else:
        lastLap['fg'] = "white"
        bestLap['fg'] = "white"

def updateDeltaTime():
    #get delta time
    deltaTime['text'] = "+/- %s" % ("--:--.---") 
    w.after(1, updateDeltaTime)
def updateLastLap():
    if Lap == 0:
        lastLap['text'] = ("LAST --:--.---")
    else:
        lastLap['text'] = ("LAST " + lapTimeToString(int(LapTimes[Lap - 2] * 1000)))
        return int(LapTimes[Lap - 2] * 1000)
def updateBestLap():
    min = 0
    minv = 1000
    for i in LapTimes:
        if i < minv and i > 0:
            min = i
            minv = i
    if Lap == 0:
        bestLap['text'] = ("BEST --:--.---")
    else:
        bestLap['text'] = ("BEST " + lapTimeToString(int(min * 1000)))
        return int(min * 1000)

lapStart = 0
def updateCurrentLap(restart: bool = False):
    global currentLapTime
    global lapStart
    if (restart):
        lapStart = 0
    if (lapStart == 0):
        currentLap['text'] = ("00:00.000")
        lapStart = time.time()
    if (currentLap['text'] == "--:--.---"):
        return

    currentLapTime = (time.time() - lapStart)
    currentLap['text'] = (lapTimeToString(int(currentLapTime * 1000)))
    w.after(1, updateCurrentLap)
def updateDeltaTime():
    #get delta time
    deltaTime['text'] = "DELTA +/- %s" % ("--:--.---") 
    w.after(1, updateDeltaTime)

w = tk.Tk()
w.title("Systems Check")
w.configure(background='black')
screenWidth = 800#w.winfo_screenwidth()
screenHeight = 480#w.winfo_screenheight()
w.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, 0, 0))

#Pedal position indicators
throttle = ttk.Progressbar(w, orient='vertical', length=200, mode='determinate', value=0)
brake = ttk.Progressbar(w, orient='vertical', length=200, mode='determinate', value=0)
barSpacing = 10
PPIxRef = screenWidth - (2 * (barSpacing + throttle.winfo_reqwidth()))
PPIyRef = screenHeight - (barSpacing + throttle.winfo_reqheight())

brake.place(x = PPIxRef, y = PPIyRef)
throttle.place(x = PPIxRef + barSpacing + throttle.winfo_reqwidth(), y = PPIyRef)
w.after(1, updateThrottle)
w.after(1, updateBrake)

#Lap time information
LapTimeFrame = tk.Frame(w, width = 220, height = 250, highlightbackground="#FFFFFF", highlightthickness=3, bg="black")
race = tk.Label(w, text="RACE", bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=8, height=1)
lap = tk.Label(w, text="LAP --/--", bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=8, height=1)
deltaTime = tk.Label(w, text="DLTA +/- --:--.---", bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=16, height=1)
lastLap = tk.Label(w, text="LAST --:--.---", bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=16, height=1)
bestLap = tk.Label(w, text="BEST --:--.---", bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=16, height=1)
currentLap = tk.Label(w, text="--:--.---", bg="black", fg="#FFFFFF", font="helvetica 42 bold", width=9, height=1)

LapTimeFrame['width'] = race.winfo_reqwidth() + lap.winfo_reqwidth() + 6
LapTimeFrame.place(x = -3, y = -3)
race.place(x = 0, y = 0)
lap.place(x = race.winfo_reqwidth(), y = 0)
deltaTime.place(x = 0, y = race.winfo_reqheight())
lastLap.place(x = 0, y = race.winfo_reqheight() + deltaTime.winfo_reqheight())
bestLap.place(x = 0, y = race.winfo_reqheight() + deltaTime.winfo_reqheight() + lastLap.winfo_reqheight())
currentLap.place(x = 0, y = LapTimeFrame.winfo_reqheight() - (6 + currentLap.winfo_reqheight()))
w.after(1, updateDeltaTime)

#Vehicle information
gear = tk.Label(w, text="N", bg="black", fg="#FFFFFF", font="helvetica 100 bold")
revs = tk.Label(w, text="-----", bg="black", fg="#FFFFFF", font="helvetica 80 bold")
brakeBal = tk.Label(w, text="BRAKE  62%", bg="black", fg="#FFFFFF", font="helvetica 24 bold")
speed = tk.Label(w, text="---", bg="black", fg="#FFFFFF", font="helvetica 36 bold")
drs = tk.Label(w, text="DRS       CLOSED", bg="black", fg="#FFFFFF", font="helvetica 24 bold")
strat = tk.Label(w, text="STRAT   6", bg="black", fg="#FFFFFF", font="helvetica 24 bold")

gear.place(x = LapTimeFrame.winfo_reqwidth() + deltaTime.winfo_reqheight(), y = (LapTimeFrame.winfo_reqheight() - gear.winfo_reqheight()) / 2)
revs.place(x = LapTimeFrame.winfo_reqwidth() + deltaTime.winfo_reqheight() + gear.winfo_reqheight(), y = (LapTimeFrame.winfo_reqheight() - revs.winfo_reqheight()) / 2)
brakeBal.place(x = 10, y = LapTimeFrame.winfo_reqheight())
speed.place(x = screenWidth - speed.winfo_reqwidth() - 10, y = 0)
drs.place(x = 10, y = LapTimeFrame.winfo_reqheight() + brakeBal.winfo_reqheight())
strat.place(x = 10, y = LapTimeFrame.winfo_reqheight() + brakeBal.winfo_reqheight() + strat.winfo_reqheight())

#Temporary lap button for testing. Actual button will be on steering wheel
lapbutton = tk.Button(w, text="LAP", command=updateLap, bg="black", fg="#FFFFFF", font="helvetica 24 bold", width=8, height=1)
lapbutton.pack()

w.mainloop()