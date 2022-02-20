#GUITest3.py    
from guizero import App, Text, TextBox

#add App title
app = App(title = "Welcome Friends")

#add Text widget to GUI
welcome_message = Text(app, text = "Welcome to my app.")

#add TextBox to GUI
my_name = TextBox(app)

app.display()

