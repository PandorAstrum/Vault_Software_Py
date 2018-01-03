# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from bin.libPackage.baseComponent import ComponentBase
from .Tabs import *

json_settings = {
    "id": "Help",
    "component_name": "HelpComponent",
    "icon": "fa-book",
    "status": True,
    "order": 2,
    "tab_group_name": "help_tab_group",
    "tab": [
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "HelpGeneralTab",
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
            "tab_class_name": "HelpAccountTab",
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
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "HelpHelpTab",
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
        self.tab_class_collection = [HelpGeneralTab(), HelpAccountTab(), HelpHelpTab()]
        self._populate()
