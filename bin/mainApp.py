# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "main app module"
"""

from kivy.config import Config
Config.set('kivy', 'window_icon', 'res/logo.png')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '500')

import kivy
from kivy.core.window import Window, WindowBase

kivy.require("1.10.0")

from kivy.app import App
from kivymd.theming import ThemeManager

import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
# os.environ['KIVY_HOME'] = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\localDump\\"
# os.environ["KIVY_DATA_DIR"]="C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\localDump\\"
# os.environ["KIVY_NO_CONSOLELOG"] = "0"

# lib import
from data.lib.localStorage import LocalStorage
from bin.libPackage.paScreens import LaunchPad
from bin.libPackage.paUtility import PaUtility
from bin.libPackage.localStorage import LocalStorage
from bin.libPackage.googleSheet import GoogleSheet
from bin.libPackage.cipherRSA import CipherRSA

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
# dumpJson(USER_SETTINGS_JSON, LocalStorage(debug=True).storage)


class MainApp(App):
    def __init__(self):
        super(MainApp, self).__init__()
        self.local_Store = LocalStorage(debug=True)
        self.instance = self
        self.theme_cls = ThemeManager()

    def build(self):
        config = self.config
        width = config.getint("WindowSettings", "Width")
        height = config.getint("WindowSettings", "Height")
        Window.size = (width, height)

        self.use_kivy_settings = False

        self.title = "Vault Hub"
        self.theme_cls.theme_style = 'Dark'
        self.icon = "res/icon/icon.ico"
        self.root = LaunchPad()

        return self.root

    def get_application_config(self):
        conf_directory = self.local_Store.storage

        if not os.path.exists(conf_directory):
            os.makedirs(conf_directory)

        return super(MainApp, self).get_application_config(
            f'{conf_directory}config.cfg'
        )

    def build_config(self, config):
        # window settings
        config.setdefaults("WindowSettings", {
            "Height": "500",
            "Width": "1000"
        })
        config.setdefaults("Session", {
            "Current": "500"
        })
        config.setdefaults("Client", {
            "Username": "dreadlordn",
            "Password": "starwars0"
        })
        config.setdefaults("Component", {
            "PrimaryComponentEntry": ("User", "Help"),
            "SecondaryComponentEntry": [self.local_Store.storage]
        })

    def on_config_change(self, config, section, key, value):
        pass

    # TODO: Design the app start and close behaviour
    def on_start(self):
        pass

    def on_pause(self):
        pass

    def on_resume(self):
        pass

    def on_stop(self):
        # The Kivy event loop is about to stop, set a stop signal;
        # otherwise the app window will close, but the Python process will
        # keep running until all secondary threads exit.
        # self.root.stop.set()
        # Validate Json Data and pass it
        pass
