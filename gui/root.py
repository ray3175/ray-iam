from kivy.graphics import BorderImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from fonts import RAYSSO_FONT
from local_data_config import LocalMSGLabel, LocalUserLabel, LocalUserTextInput, LocalPwdLabel, LocalPwdTextInput, LocalHostLabel, LocalHostTextInput, LocalPortLabel, LocalPortTextInput, LocalDBLabel, LocalDBTextInput, LocalCharsetLabel, LocalCharsetTextInput, LocalSaveButton, LocalReturnButton
from remote_data_config import RemoteMSGLabel, RemoteUserLabel, RemoteUserTextInput,RemotePwdLabel, RemotePwdTextInput, RemoteHostLabel, RemoteHostTextInput, RemotePortLabel, RemotePortTextInput, RemoteDBLabel, RemoteDBTextInput, RemoteCharsetLabel, RemoteCharsetTextInput, RemoteSaveButton, RemoteReturnButton
from migrate_action import TerminalLayout, StartButton, ReturnButton


class LocalDataConfigButton(Button):
    def __init__(self, **kwargs):
        self.__root = kwargs.pop("root", None)
        kwargs.update({
            "text": "本地数据库配置",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.1, "y": 0.7},
            "font_name": RAYSSO_FONT,
            "font_size": 21,
            "background_color": [0.69, 0.12, 0.240, 0.5]
        })
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.goto_local_data_config()


class RemoteDataConfigButton(Button):
    def __init__(self, **kwargs):
        self.__root = kwargs.pop("root", None)
        kwargs.update({
            "text": "远程数据库配置",
            "size_hint": [0.2, 0.1],
            "pos_hint": {"x": 0.7, "y": 0.7},
            "font_name": RAYSSO_FONT,
            "font_size": 21,
            "background_color": [0.69, 0.12, 0.240, 0.5]
        })
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.goto_remote_data_config()


class MigrateActionButton(Button):
    def __init__(self, **kwargs):
        self.__root = kwargs.pop("root", None)
        kwargs.update({
            "text": "开始迁移",
            "size_hint": [0.3, 0.15],
            "pos_hint": {"x": 0.35, "y": 0.25},
            "font_name": RAYSSO_FONT,
            "font_size": 30,
            "background_color": [0.247, 0.195, 0.24, 0.5]
        })
        super().__init__(**kwargs)

    def on_release(self):
        self.parent.goto_migrate_action()


class RootLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_background()
        self.init_main()

    def _init_background(self):
        with self.canvas.before:
            self.__background = BorderImage(
                border=[20, 20, 20, 20],
                source="./background/nepgear.png"
            )
        self.bind(pos=self._update_background, size=self._update_background)

    def _update_background(self, instance, value):
        self.__background.pos = instance.pos
        self.__background.size = instance.size

    def init_main(self):
        self.add_widget(LocalDataConfigButton())
        self.add_widget(RemoteDataConfigButton())
        self.add_widget(MigrateActionButton())

    def init_local_data_config(self):
        obj_dict = {
            "msg": LocalMSGLabel(),
            "user": LocalUserTextInput(),
            "pwd": LocalPwdTextInput(),
            "host": LocalHostTextInput(),
            "port": LocalPortTextInput(),
            "db": LocalDBTextInput(),
            "charset": LocalCharsetTextInput(),
        }
        self.add_widget(obj_dict["msg"])
        self.add_widget(LocalUserLabel())
        self.add_widget(obj_dict["user"])
        self.add_widget(LocalPwdLabel())
        self.add_widget(obj_dict["pwd"])
        self.add_widget(LocalHostLabel())
        self.add_widget(obj_dict["host"])
        self.add_widget(LocalPortLabel())
        self.add_widget(obj_dict["port"])
        self.add_widget(LocalDBLabel())
        self.add_widget(obj_dict["charset"])
        self.add_widget(LocalCharsetLabel())
        self.add_widget(obj_dict["db"])
        self.add_widget(LocalSaveButton(obj_dict))
        self.add_widget(LocalReturnButton())

    def init_remote_data_config(self):
        obj_dict = {
            "msg": RemoteMSGLabel(),
            "user": RemoteUserTextInput(),
            "pwd": RemotePwdTextInput(),
            "host": RemoteHostTextInput(),
            "port": RemotePortTextInput(),
            "db": RemoteDBTextInput(),
            "charset": RemoteCharsetTextInput(),
        }
        self.add_widget(obj_dict["msg"])
        self.add_widget(RemoteUserLabel())
        self.add_widget(obj_dict["user"])
        self.add_widget(RemotePwdLabel())
        self.add_widget(obj_dict["pwd"])
        self.add_widget(RemoteHostLabel())
        self.add_widget(obj_dict["host"])
        self.add_widget(RemotePortLabel())
        self.add_widget(obj_dict["port"])
        self.add_widget(RemoteDBLabel())
        self.add_widget(obj_dict["charset"])
        self.add_widget(RemoteCharsetLabel())
        self.add_widget(obj_dict["db"])
        self.add_widget(RemoteSaveButton(obj_dict))
        self.add_widget(RemoteReturnButton())

    def init_migrate_action(self):
        terminal = TerminalLayout()
        self.add_widget(terminal)
        self.add_widget(StartButton(terminal))
        self.add_widget(ReturnButton())

    def goto_main(self):
        self.clear_widgets()
        self.init_main()

    def goto_local_data_config(self):
        self.clear_widgets()
        self.init_local_data_config()

    def goto_remote_data_config(self):
        self.clear_widgets()
        self.init_remote_data_config()

    def goto_migrate_action(self):
        self.clear_widgets()
        self.init_migrate_action()


