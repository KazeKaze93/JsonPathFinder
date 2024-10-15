from kivy.app import App
from kivy.core.window import Window
from gui import JSONPathFinderGUI

class JSONPathFinderApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return JSONPathFinderGUI()

if __name__ == '__main__':
    JSONPathFinderApp().run()
