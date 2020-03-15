import os
os.environ["KIVY_WINDOW"] = "sdl2"
os.environ["KIVY_TEXT"] = "sdl2"

import kivy
kivy.require("1.11.1")

from kivy.app import App
from root import RootLayout


class RayIamApp(App):
    def build(self):
        self.root = RootLayout()
        return self.root


if __name__ == '__main__':
    x = RayIamApp()
    x.run()

