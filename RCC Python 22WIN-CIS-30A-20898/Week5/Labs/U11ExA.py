import tkinter as tk #import tkinter and use alias

#create a new window
window = tk.Tk()

#configure the window size
window.geometry("400x400")

#adding widget
welcome = tk.Label(window, text="Hello, friends.")
welcome.pack()

#adding label event
label = tk.Label(
    text = 'Hello, Friends',
    fg = 'white',
    bg = 'black',
    width = 10, 
    height=10
)
label.pack()

#adding a button
button = tk.Button(
    text = 'Click me!',
    width = 25,
    height= 5,
    bg = 'white',
    fg = 'black',
)
button.pack()

#to listen to events
window.mainloop(0)
