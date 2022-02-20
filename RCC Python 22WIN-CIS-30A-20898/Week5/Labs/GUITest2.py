#GUITest2.py    
from guizero import App, Text

#add App title
app = App(title = "Welcome Friends")

#add Text widget to GUI
welcome_message = Text(app, text = "Welcome to my app.")

app.display()

