# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from bin.libPackage.baseComponent import ComponentBase
from .Tabs import *

json_settings = {
    "id": "Users",
    "component_name": "UserComponent",
    "icon": "fa-home",
    "status": True,
    "order": 1,
    "tab_group_name": "user_tab_group",
    "tab": [
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "UserGeneralTab",
            "tab_name": "General",
            "tab_id": "general",
            "tab_icon": "fa-user",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "UserAccountTab",
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
            "toolbar" : {
                "have_toolbar": True,
                "toolbar_color": [
                    219,
                    134,
                    37
                ]
            },
            "tab_class_name": "UserHelpTab",
            "tab_name": "Help",
            "tab_id": "help",
            "tab_icon": "fa-question",
            "tab_type": "list",
            "tab_content": []
        }
    ]
}


class Component(ComponentBase):
    """
    docString
    """
    def __init__(self, **kwargs):
        super(Component, self).__init__()
        self.name = kwargs.get("component_name")
        self.component_id = kwargs.get("component_id")
        self.component_icon = kwargs.get("component_icon")
        self.component_tab_info = kwargs.get("component_tab_info")
        self.tab_group_name = kwargs.get("tab_group_name")
        self.default_tab_name = "General"

        self.tab_class_collection = [UserGeneralTab(), UserAccountTab(), UserHelpTab()]
        self._populate()
