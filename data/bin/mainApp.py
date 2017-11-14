# logging
# import logging
# from kivy.logger import Logger
# Logger.setLevel(logging.ERROR)

# Window size settings
from kivy.config import Config
Config.set('kivy', 'window_icon', 'res/logo.png')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '500')
from data.lib.jsonUtility import getJsonFile, getKeyValue, dumpKeyValue
data = getJsonFile()
width = getKeyValue(data, "window_width")
height = getKeyValue(data, "window_height")
Config.set('graphics', 'width', width[0])
Config.set('graphics', 'height', height[0])

#kivy import
import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivymd.theming import ThemeManager

# lib import
from data.lib.paWidget import RootWidget
from data.lib.localStorage import LocalStorage




class MainApp(App):
    def build(self):
        ls = LocalStorage(debug=True)
        self.theme_cls = ThemeManager()
        # self.theme_cls.theme_style = 'Dark'
        self.title = "Vault Hub"
        self.icon = "res/icon/icon.ico"
        self.root = RootWidget(directory=ls.test_dir,
                               view_file="*_Views.py",
                               folder_name="/*Component")

        return self.root

    # TODO: Design the app start and close behaviour
    def on_start(self):
        # Read Json Data And pass it
        pass

    def on_stop(self):
        # Validate Json Data and pass it
        pass
