from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout


class WalkApp(App):
    def build(self):
        gl = GridLayout(cols=4, padding=35, spacing=3)

        gl.add_widget(Button(text='7'))
        gl.add_widget(Button(text='8'))
        gl.add_widget(Button(text='9'))
        gl.add_widget(Button(text='X'))

        gl.add_widget(Button(text='4'))
        gl.add_widget(Button(text='5'))
        gl.add_widget(Button(text='6'))
        gl.add_widget(Button(text='-'))

        gl.add_widget(Button(text='1'))
        gl.add_widget(Button(text='2'))
        gl.add_widget(Button(text='3'))
        gl.add_widget(Button(text='+'))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='-'))
        gl.add_widget(Button(text='.'))
        gl.add_widget(Button(text='='))

        return gl


if __name__ == '__main__':
    WalkApp().run()
