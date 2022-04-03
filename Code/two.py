from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class FirstApp(App):
    ''' App class '''

    __slots__ = ()

    def build(self):
        container = BoxLayout(padding=40)
        container.add_widget(Button(text="hello"))
        container.add_widget(Button(text="There"))
        return container

if __name__ == '__main__':
    FirstApp().run()
