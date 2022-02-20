#check boxes or button options for the interface
from tkinter import *

root = Tk()
root.geometry('300x200')

w = Label(root, text='Student Options for Courses', font = '50')
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text='Online', 
                    variable=Checkbutton1,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)       

Button2 = Checkbutton(root, text='Onsite', 
                    variable=Checkbutton2,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)

Button3 = Checkbutton(root, text='Hybdrid', 
                    variable=Checkbutton3,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()