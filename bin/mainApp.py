# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "main core file that builds kivy app
            Available palettes: 'Pink',
                                'Blue',
                                'Indigo',
                                'BlueGrey',
                                'Brown',
                                'LightBlue'
                                'Purple',
                                'Grey',
                                'Yellow',
                                'LightGreen',
                                'DeepOrange',
                                'Green',
                                'Red',
                                'Teal',
                                'Orange',
                                'Cyan',
                                'Amber',
                                'DeepPurple',
                                'Lime'
"""

from kivy.config import Config

Config.set('kivy', 'window_icon', 'res/logo.png')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '500')

import kivy
kivy.require("1.10.0")
from kivy.core.window import Window
from kivy.app import App
from kivymd.theming import ThemeManager

import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
# os.environ['KIVY_HOME'] = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\localDump\\"
# os.environ["KIVY_DATA_DIR"]="C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\localDump\\"
# os.environ["KIVY_NO_CONSOLELOG"] = "0"

# lib import
import utils
from selenium import webdriver
from utils import appDirs
from bin import appSettings
from Core.basescreens import LaunchPad

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


class MainApp(App):
    def __init__(self):
        super(MainApp, self).__init__()
        self.theme_cls = ThemeManager()
        self.sys_info = utils.get_sys_info()

    def build(self):
        config = self.config
        width = config.getint("WindowSettings", "Width")
        height = config.getint("WindowSettings", "Height")
        Window.size = (width, height)

        self.use_kivy_settings = False

        theme_styles = config.get("Theme", "ThemeStyle")
        self.theme_cls.theme_style = theme_styles
        primary_color = config.get("Theme", "PrimaryColor")
        self.theme_cls.primary_palette = primary_color
        accent_color = config.get("Theme", "AccentColor")
        self.theme_cls.accent_palette = accent_color
        installed_dir = config.get("App", "Installed_Directory")
        if installed_dir == "":
            installed_dir = appDirs.get_current_directory()
            config.set("App", "Installed_Directory", installed_dir)
        self.icon = "res/icon/icon.ico"
        self.title = "Vault Hub"
        self.root = LaunchPad()

        return self.root

    def get_application_config(self):
        user_dir = appDirs.user_config_dir(appname=appSettings.APP_NAME,
                                                 appauthor=appSettings.APP_AUTHOR)
        conf_directory = user_dir+f"\\{appSettings.FOLDER_CONFIG}"
        appDirs.check_make_dir(conf_directory)

        return super(MainApp, self).get_application_config(
            f'{conf_directory}\\{appSettings.FILE_CONFIG_APP}'
        )

    def build_config(self, config):
        config.setdefaults("WindowSettings", {
            "Height": "500",
            "Width": "1000"
        })
        config.setdefaults("App", {
            "Version": appSettings.APP_VERSION,
            "Name": appSettings.APP_NAME,
            "Author": appSettings.APP_AUTHOR,
            "Installed_Directory": ""
        })
        config.setdefaults("Device", {
            "OS_NAME": self.sys_info["OS_NAME"],
            "OS_VER": self.sys_info["OS_VER"],
            "CPU": self.sys_info["CPU"],
            "GPU": self.sys_info["GPU"],
            "RAM": self.sys_info["RAM"],
            "DEVICE_NAME": self.sys_info["DEVICE_NAME"],
            "UUID": self.sys_info["UUID"]
        })
        config.setdefaults("Session", {
            "Current": "500"
        })
        config.setdefaults("User", {
            "Username": "a",
            "Password": "a",
            "Email": "dreadlordn@gmail.com",
            "FirstName": "Ashiquzzaman",
            "LastName": "Khan",
            "Role": "Programmer"
        })
        config.setdefaults("Component", {
            "PrimaryComponentEntry": ("Miner_PR","User_PR", "Help_PR"),
            "SecondaryComponentEntry": ()
        })
        config.setdefaults("Theme", {
            "PrimaryColor": "Blue",
            "AccentColor": "Lime",
            "ThemeStyle": "Dark"
        })

    def on_config_change(self, config, section, key, value):
        pass

    # TODO: Design the app start and close behaviour
    def on_start(self):
        def initial_load():
            webdriver.Chrome(executable_path=".\\dll\\chrome_drivers\\chromedriver.exe")
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
