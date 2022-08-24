from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

#start
main = Tk()
main.geometry("260x79+300+300")
main.title("Ahmet")

def rnd():
    a = ["#"+''.join([random.choice('ABCDEF0123456789') for p in range(6)])]
    return a

def tms():
    text = strftime('%H:%M:%S')
    l.after(1000, tms)
    l.config(text=text)

l = Label(
    main,
    font=('Roboto', 50, 'normal'),
    background=rnd(),
    foreground=rnd()
)

l.pack(anchor='center')
tms()
mainloop()
#end