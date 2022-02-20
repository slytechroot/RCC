#GUITest4.py - Adding Picture
from guizero import App, Text, TextBox, PushButton, Slider

#define PushButton function
def say_my_name():
    welcome_message.value = my_name.value

#define Slider function
def change_text_size(slider_value):
    welcome_message.size = slider_value

#add App title
app = App(title = "Welcome Friends")

#add Text widget to GUI
welcome_message = Text(app, text = "Welcome to my app.")

#add TextBox to GUI
my_name = TextBox(app)

#add PushButton widget to GUI
update_text = PushButton(app, command = say_my_name, text = "Display my name.")

#add Slider widget to GUI
text_size = Slider(app, command = change_text_size, start=10, end=80)

app.display()


