from kivy.app import App
from kivy.uix.textinput import TextInput


def on_enter(instance, value):
    print("User pressed enter in", instance)


class PongApp(App):
    textinput = TextInput(text='Hello world', multiline=False)
    textinput.bind(on_text_validate=on_enter)


if __name__ == "__name__":
    PongApp().run()
