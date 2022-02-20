#GuiTest6.py - adding Combo
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo

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

#add Combo widget to GUI
user_choice = Combo(app, options =["Option 1", "Option 2", "Option 3"], grid = [1, 0], align = 'left')

#add Combo widget to GUI
choice_description = Text(app, text ="Select an option (1, 2, 3)", grid=[0,0], align='left')

app.display()
#success!!!
