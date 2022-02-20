import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "\n Hello World \n (click me) \n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        #print('\n')
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone! Do you like clicking buttons? ")

root = tk.Tk() #this create a Tk window
app = Application(master=root) #object called App. This is called to call 
                                #the mainloop()
app.mainloop()  #infinite loop. 
