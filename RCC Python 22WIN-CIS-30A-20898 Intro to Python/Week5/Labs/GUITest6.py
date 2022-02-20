#GuiTest6.py - adding Picture
from guizero import App, Text, TextBox, PushButton, Slider, Picture

#define PushButton function
def say_my_name():
    welcome_message.value = my_name.value

#define Slider function
def change_text_size(slider_value):
    welcome_message.size = slider_value

#add App title
app = App(title="Hello world")

#add Text widget
welcome_message = Text(app, text = "Welcome to my app.")

#add TextBox widget
my_name = TextBox(app)

#add PushButton widget to GUI
update_text = PushButton(app, command = say_my_name, text = "Display my name.")

#add Slider widget to GUI
text_size = Slider(app, command = change_text_size, start = 10, end = 80)

#add Picture widget to GUI
my_pic = Picture(app, image = "PC.gif")

app.display()
#success!!!
