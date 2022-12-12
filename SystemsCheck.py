from tkinter import *
import sys
import DRS
import RearViewCamera
import SideViewCamera
import HeadsUpDisplay
import WaterBottle
import ScoutDrones

systems = [DRS, RearViewCamera, WaterBottle, SideViewCamera, HeadsUpDisplay, ScoutDrones]

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

counter = 0
def updateStatus():
    global counter
    if systems[counter].statusCheck() == True:
        sysLab[counter]['text'] = text=("%s: Online" % (systems[counter].name))
        sysLab[counter]['fg'] = "#75fb4c"
    else:
        sysLab[counter]['text'] = text=("%s: Offline" % (systems[counter].name))
        sysLab[counter]['fg'] = "#ea3323"
    counter = counter + 1
    if counter < len(systems):
        w.after(500, updateStatus)

def systemComplete():
    f1 = Frame(w, width = 10, height = 10, highlightbackground="#75fb4c", highlightthickness=3)
    l1 = Label(w, text="Systems Check Complete", bg="black", fg="#75fb4c", font="verdana 20 bold", width=30, height=2)
    f1['width'] = l1.winfo_reqwidth()+6
    f1['height'] = l1.winfo_reqheight()+6
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)
    l1.place(relx=0.5, rely=0.5, anchor=CENTER)

w = Tk()
w.title("Systems Check")
w.configure(background='black')
screenWidth = w.winfo_screenwidth()
screenHeight = w.winfo_screenheight()
w.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, 0, 0))

sysLab = [Label] * len(systems)

for i in range(len(systems)):
    
    
    sysLab[i] = Label(w, text=("%s: Checking..." % (systems[i].name)), bg="black", fg="white", font="verdana 20 bold")
    sysLab[i].place(x=0, y=sysLab[i].winfo_reqheight() * i)

w.after(1500, updateStatus)
w.after(500 * (len(systems) + 4), systemComplete)
w.after(500 * (len(systems) + 8), w.destroy)

w.mainloop()