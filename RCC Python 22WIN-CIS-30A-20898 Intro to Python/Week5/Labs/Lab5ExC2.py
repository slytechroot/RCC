#creating a label that contains an image
#always use a .gif, do not use .jpg or .png
#keep in the same folder as the script file

from tkinter import *
import time
import os

root = Tk()              #setup a window
frameCnt = 12              #frame count
frames = [PhotoImage(file='PC.gif', format = 'gif -index %i' %(i)) 
        for i in range(1)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    w1.configure(image=frame)
    root.after(100, update, ind)

explanation = 'moving image'

w2 = Label(root,
            justify=LEFT,
            padx = 10,
            text= explanation).pack(side='left')
w1 = Label(root)
w1.pack()
root.after(0, update, 0)
root.mainloop()

