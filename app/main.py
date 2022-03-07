from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


class AppWidget(Widget):
    pass


class OSCWApp(MDApp):
    def build(self):
        return MDLabel(text="Hello world", halign="center")


if __name__ == "__main__":
    OSCWApp().run()
