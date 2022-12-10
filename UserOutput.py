from tkinter.ttk import Progressbar
from tkinter import *
import random

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

import sys
sys.stdout = Unbuffered(sys.stdout)

counter = 0

def updateStatus():
    global counter
    rand = random.randint(0, 100)
    if rand < 50:
        s1[counter]['text'] = "System Name: Offline"
        s1[counter]['fg'] = "red"
    else:
        s1[counter]['text'] = "System Name: Online"
        s1[counter]['fg'] = "green"
    counter = counter + 1
    if counter < checkListSize:
        w.after(500, updateStatus)

def systemComplete():
    l1 = Label(w, text="Systems Check Complete", bg="Green", fg="black", font="verdana 20 bold", width=30, height=2)
    l1.place(relx=0.5, rely=0.5, anchor=CENTER)

w = Tk()
w.title("Systems Check")
w.configure(background='black')
screenWidth = w.winfo_screenwidth()
screenHeight = w.winfo_screenheight()
w.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, -10, 0))

checkListSize = 10
s1 = [Label] * checkListSize

for i in range(checkListSize):
    s1[i] = Label(w, text="System Name: Checking...", bg="black", fg="white", font="verdana 20 bold")
    s1[i].place(x=0, y=38 * i)

w.after(500, updateStatus)
w.after(500 * (checkListSize + 2), systemComplete)
w.after(500 * (checkListSize + 6), w.destroy)

w.mainloop()