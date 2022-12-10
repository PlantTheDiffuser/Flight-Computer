from tkinter.ttk import Progressbar
from tkinter import *

w = Tk()
w.title("Systems Check")
w.configure(background='black')
screenWidth = w.winfo_screenwidth()
screenHeight = w.winfo_screenheight()
w.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, -10, 0))


checkListSize = 5

statusHeight = screenHeight / checkListSize


for i in range(checkListSize):
    ypos = statusHeight + (i * screenHeight)
    s1 = Label(w, text="Status " + str(i), bg="black", fg="white", font=("Helvetica", 16))
    s1.place(x=0, y=ypos)

w.mainloop()