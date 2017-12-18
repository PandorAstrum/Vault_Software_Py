# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "inner main file"
"""

from kivy.config import Config
import kivy
kivy.require("1.10.0")
Config.set('kivy', 'window_icon', 'res/logo.png')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '500')

from bin.libPackage.jsonUtility import getJsonFile, getKeyValue
# from data.lib.jsonUtility import getJsonFile,\
#                                  getKeyValue,\
#                                  dumpKeyValue,\
#                                  dumpJson
data = getJsonFile()
WIDTH = getKeyValue(data, "window_width")
HEIGHT = getKeyValue(data, "window_height")
Config.set('graphics', 'width', WIDTH[0])
Config.set('graphics', 'height', HEIGHT[0])

from kivymd.theming import ThemeManager
from kivy.app import App


# lib import
from data.lib.paWidget import RootWidget
from data.lib.localStorage import LocalStorage

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
    """Doc String"""
    def build(self):
        ls = LocalStorage(debug=True)
        self.theme_cls = ThemeManager()
        # self.theme_cls.theme_style = 'Dark'
        self.title = "Vault Hub"
        self.icon = "res/icon/icon.ico"
        self.root = RootWidget(directory=ls.test_dir,
                               view_file="*_Views.py",
                               folder_name="/*Component",
                               ls=ls)

        return self.root

    # TODO: Design the app start and close behaviour
    def on_start(self):
        # Read Json Data And pass it
        pass

    def on_stop(self):
        # Validate Json Data and pass it
        pass
