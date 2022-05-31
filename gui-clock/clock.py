from tkinter import *
from tkinter.ttk import *
from time import strftime

clock = Tk()
clock.title("TheClock!")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(clock, font = ("Trebuchet MS", 80), background = "black", foreground = "cyan")
label.pack(anchor = 'center')

time()


mainloop()

