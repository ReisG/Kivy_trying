import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class But(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        #if not self.collide_point(touch.x, touch.y):
        #    return False
        print("I'm touched")


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        # initializing GridLayout
        super().__init__(**kwargs)

        self.cols = 2
        self.add_widget( Label(text='User name') )
        # adding username field
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget( Label(text='password') )
        # adding password field
        self.password = TextInput(password=True, multiline=False)
        self.add_widget( self.password )
        self.add_widget( But(text="Click here") )

    def on_touch_move(self, touch):
        print('Moved')
        return True
    
    def on_touch_up(self, touch):
        print('UP')
        return True


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    # help(Button)
    MyApp().run()
