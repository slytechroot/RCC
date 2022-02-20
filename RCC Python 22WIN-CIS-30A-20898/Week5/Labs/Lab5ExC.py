#creating a label that contains an image
#always use a .gif, do not use .jpg or .png
#keep in the same folder as the script file

from email.mime import image
import tkinter as tk

root = tk.Tk()                          #setup a window
logo = tk.PhotoImage(file='Logo.gif')   #keep the same name

w1 = tk.Label(root, image = logo).pack(side = 'right')

explanation = '''At present, only GIF and PPM/PGM format are
supported, but an interface exists to allow additional image file formats
to be added easily'''

w2 = tk.Label(root,
            justify=tk.LEFT,
            padx = 10,
            text= explanation).pack(side= 'left')
root.mainloop()

