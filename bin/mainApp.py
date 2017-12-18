# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "main app module"
"""
# pylint: disable=C0103

import os
# os.environ["KIVY_NO_CONSOLELOG"] = "0"
os.environ["KIVY_NO_FILELOG"] = ""
# change the kivy home folder
# os.environ['KIVY_HOME'] = <folder>

# set the window size
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

# Config.set('kivy', 'window_icon', 'res/logo.png')
# Config.set('graphics', 'minimum_width', '1000')
# Config.set('graphics', 'minimum_height', '500')
import kivy
from kivy.uix.textinput import TextInput



kivy.require("1.10.0")
# from data.lib.jsonUtility import getJsonFile,\
#                                  getKeyValue,\
#                                  dumpKeyValue,\
#                                  dumpJson
# data = getJsonFile()
# WIDTH = getKeyValue(data, "window_width")
# HEIGHT = getKeyValue(data, "window_height")
# Config.set('graphics', 'width', WIDTH[0])
#
# Config.set('graphics', 'height', HEIGHT[0])

from kivymd.theming import ThemeManager
from kivy.app import App


# lib import
from data.lib.paWidget import RootWidget
from data.lib.localStorage import LocalStorage


from bin.libPackage.paScreens import RootScreenMngr
from bin.libPackage.kvFiles import *

# json test
USER_SETTINGS_JSON = {
    "component": [
        {
            "User_component": {
                "id": "Users",
                "icon": "fa-home",
                "status": True,
                "order": 1,
                "tab_group_name": "user_tab_group",
                "tab": [
                    {
                        "tab_name": "General",
                        "tab_id": "general",
                        "tab_icon": "fa-user",
                        "tab_type": "basic",
                        "tab_content": []
                    },
                    {
                        "tab_name": "Accounts",
                        "tab_id": "accounts",
                        "tab_icon": "fa-key",
                        "tab_type": "list",
                        "tab_content": [
                            {
                                "tab_item_name": "1 First"
                            },
                            {
                                "tab_item_name": "2 Second"
                            },
                            {
                                "tab_item_name": "3 Second"
                            }
                        ]
                    },
                    {
                        "tab_name": "Help",
                        "tab_id": "help",
                        "tab_icon": "fa-question",
                        "tab_type": "basic",
                        "tab_content": []
                    }
                ]
            }
        },
        {
            "Help_component": {
                "id": "Help",
                "icon": "fa-question",
                "status": True,
                "order": 2,
                "tab_group_name": "help_tab_group",
                "tab": [
                    {
                        "tab_name": "General",
                        "tab_id": "general",
                        "tab_icon": "fa-user",
                        "tab_type": "basic",
                        "tab_content": []
                    },
                    {
                        "tab_name": "Guides",
                        "tab_id": "guides",
                        "tab_icon": "fa-key",
                        "tab_type": "list",
                        "tab_content": []
                    }
                ]
            }
        },
        {
            "Test_component": {
                "id": "Test",
                "icon": "fa-question",
                "status": False,
                "order": 3,
                "tab": []
            }
        }
    ],
    "settings": [
        {
            "window_size": {
                "window_width": 1000,
                "window_height": 500
            }
        }
    ]
}
# dumpJson(USER_SETTINGS_JSON)






class MainApp(App):
    """
    Main Entry point for the app loop
    """
    # def build_config(self, config):
    #     # window settings
    #     config.setdefaults("WindowSettings", {
    #         "Height": "500",
    #         "Width": "1000"
    #     })
    #     # build the configuration file here for the ui
    #
    # def build_settings(self, settings):
    #     print(Config.get_configparser("kivy"))
    #     Config.set('kivy', 'window_icon', 'res/logo.png')
    #     Config.set('graphics', 'minimum_width', '1000')
    #     Config.set('graphics', 'minimum_height', '500')
    #     # Config.set("graphics", "width", "1000")
    #     Config.setdefaults("section", "value", "")

    def on_config_change(self, config, section, key, value):
        pass

    def build(self):
        self.theme_cls = ThemeManager()
        self.title = "Vault Hub"
        self.theme_cls.theme_style = 'Dark'
        self.icon = "res/icon/icon.ico"
        self.root = RootScreenMngr()
        return self.root

        # feed the ui with config file
        # config = self.config
        # width = config.getint('WindowSettings', 'width')

        # return Label(text='Height is %d and Width is %d' % (
        #     config.getint('WindowSettings', 'height'),
        #     config.getint('WindowSettings', 'width')))

        # ls = LocalStorage(debug=True)
        # self.root = RootWidget(directory=ls.test_dir,
        #                        view_file="*_Views.py",
        #                        folder_name="/*Component",
        #                        ls=ls)
        #
        # return self.root

    # TODO: Design the app start and close behaviour
    def on_start(self):
        # Read Json Data And pass it
        pass

    def on_pause(self):
        pass

    def on_resume(self):
        pass

    def on_stop(self):
        # Validate Json Data and pass it
        pass
