from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from fonts import RAYIAM_FONT
from src.action import Action


class LocalMSGLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "本地数据库配置",
            "size_hint": [0.6, 0.2],
            "pos_hint": {"x": 0.2, "y": 0.8},
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "color": [1, 0, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalUserLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "用户名：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.05, "y": 0.7},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalUserTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "hint_text": "请输入用户名。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.25, "y": 0.7},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalPwdLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "密码：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.55, "y": 0.7},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalPwdTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "password": True,
            "hint_text": "请输入密码。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.75, "y": 0.7},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalHostLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "IP地址：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.05, "y": 0.55},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalHostTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "hint_text": "请输入IP地址。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.25, "y": 0.55},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalPortLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "端口：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.55, "y": 0.55},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalPortTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "hint_text": "请输入端口。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.75, "y": 0.55},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalDBLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "数据库名称：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.05, "y": 0.4},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalDBTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "hint_text": "请输入数据库名称。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.25, "y": 0.4},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalCharsetLabel(Label):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "编码方式：",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.55, "y": 0.4},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "color": [1, 1, 0, 1],
            "halign": "center",
            "valign": "middle"
        })
        super().__init__(**kwargs)


class LocalCharsetTextInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.update({
            "hint_text": "请输入编码方式。。。",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.75, "y": 0.4},
            "font_name": RAYIAM_FONT,
            "font_size": 21,
            "background_color": [0, 0, 0, 0.5],
            "foreground_color": [1, 0, 1, 1]
        })
        super().__init__(**kwargs)


class LocalSaveButton(Button):
    def __init__(self, obj_dict, **kwargs):
        kwargs.update({
            "text": "保存",
            "size_hint": [0.3, 0.125],
            "pos_hint": {"x": 0.35, "y": 0.2},
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "background_color": [0.247, 0.195, 0.24, 0.5]
        })
        super().__init__(**kwargs)
        self.__obj_dict = obj_dict
        self.__action = Action()
        self._init_data()

    def _init_data(self):
        for key, value in self.__action.get_local_db_config().items():
            self.__obj_dict[key].text = value

    def on_release(self):
        user = self.__obj_dict["user"].text
        pwd = self.__obj_dict["pwd"].text
        host = self.__obj_dict["host"].text
        port = self.__obj_dict["port"].text
        db = self.__obj_dict["db"].text
        charset = self.__obj_dict["charset"].text
        if self.__action.set_local_db_config(user, pwd, host, port, db, charset):
            self.__obj_dict["msg"].text = "保存成功！"


class LocalReturnButton(Button):
    def __init__(self, **kwargs):
        kwargs.update({
            "text": "返回",
            "size_hint": [0.3, 0.125],
            "pos_hint": {"x": 0.35, "y": 0.05},
            "font_name": RAYIAM_FONT,
            "font_size": 30,
            "background_color": [0.247, 0.195, 0.24, 0.5]
        })
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.goto_main()


