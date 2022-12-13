from tkinter import *

##Start after systems check

w = Tk()
w.title("Systems Check")
w.configure(background='black')
screenWidth = w.winfo_screenwidth()
screenHeight = w.winfo_screenheight()
w.geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, -10, 0))

