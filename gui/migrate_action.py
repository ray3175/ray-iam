import threading
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from fonts import RAYIAM_FONT
from src.action import Action


class TerminalTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)

    def update_text(self, text):
        self.text = text


class TerminalLayout(GridLayout):
    def __init__(self, **kwargs):
        kwargs.update({
            "size_hint": [0.8, 0.75],
            "pos_hint": {"center_x": 0.5, "center_y": 0.575},
            "rows": 1
        })
        super().__init__(**kwargs)
        self.text = ""
        self._init_terminal_text_input()

    def _init_terminal_text_input(self):
        self.__terminal_text = TerminalTextInput(text=self.text)
        self.add_widget(self.__terminal_text)

    def migrate_active(self):
        self.__action = Action()
        threading.Thread(target=lambda : self.__action.db_data_remote2local(lambda text: self.append_text(text, "\n")), args=()).start()

    def append_text(self, text, split=None):
        if split:
            text += split
        self.text += text
        self.__terminal_text.update_text(self.text)


class StartButton(Button):
    def __init__(self, terminal, **kwargs):
        kwargs.update({
            "text": "开始",
            "size_hint": [0.3, 0.125],
            "pos_hint": {"x": 0.15, "y": 0.05},
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "background_color": [0.247, 0.195, 0.24, 0.5]
        })
        super().__init__(**kwargs)
        self.terminal = terminal

    def on_release(self):
        self.terminal.migrate_active()


class ReturnButton(Button):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "返回",
            "size_hint": [0.3, 0.125],
            "pos_hint": {"x": 0.55, "y": 0.05},
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "background_color": [0.247, 0.195, 0.24, 0.5]
        })
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.goto_main()

