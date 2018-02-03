# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from Core.baseInterface import ComponentBase, TabBase

__all__ = [
    "Component",
    "json_settings"
]

json_settings = {
    "id": "Help",
    "component_name": "Help_PRComponent",
    "icon": "fa-book",
    "icon_class": "",
    "status": True,
    "order": 1,
    "version": "0.0",
    "tab_group_name": "help_tab_group",
    "tab": [
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "HelpGeneralTab",
            "tab_name": "General",
            "tab_id": "general",
            "tab_icon": "wb1-screwdriver",
            "tab_icon_class": "wb1",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "HelpAccountTab",
            "tab_name": "Accounts",
            "tab_id": "accounts",
            "tab_icon": "wb1-screwdriver",
            "tab_icon_class": "wb1",
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
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "HelpHelpTab",
            "tab_name": "Help",
            "tab_id": "help",
            "tab_icon": "wb1-screwdriver",
            "tab_icon_class": "wb1",
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

class HelpGeneralTab(TabBase):
    def __init__(self, **kwargs):
        super(HelpGeneralTab, self).__init__(**kwargs)
        self.__name__ = "HelpGeneralTab"

class HelpAccountTab(TabBase):
    def __init__(self, **kwargs):
        super(HelpAccountTab, self).__init__(**kwargs)
        self.__name__ = "HelpAccountTab"

class HelpHelpTab(TabBase):
    def __init__(self, **kwargs):
        super(HelpHelpTab, self).__init__(**kwargs)
        self.__name__ = "HelpHelpTab"