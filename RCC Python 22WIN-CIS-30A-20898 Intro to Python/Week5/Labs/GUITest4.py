#GUITest4.py - Adding PushButton

from guizero import App, Text, TextBox, PushButton

#define PushButton function
def say_my_name():
    welcome_message.value = my_name.value

#add App title
app = App(title = "Welcome Friends")

#add Text widget to GUI
welcome_message = Text(app, text = "Welcome to my app.")

#add TextBox to GUI
my_name = TextBox(app)

#add PushButton widget to GUI
update_text = PushButton(app, command = say_my_name, text = "Display my name.")

app.display()
