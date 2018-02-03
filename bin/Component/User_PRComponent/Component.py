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
    "id": "Users",
    "component_name": "User_PRComponent",
    "icon": "fa-home",
    "icon_class": "",
    "status": True,
    "order": 2,
    "version": "0.1",
    "tab_group_name": "user_tab_group",
    "tab": [
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "UserAccountTab",
            "tab_name": "Account",
            "tab_id": "account",
            "tab_icon": "fa-key",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "UserComponentTab",
            "tab_name": "Component",
            "tab_id": "component",
            "tab_icon": "fa-plug",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": [
                {
                    "tab_item_name": "Component List"
                },
                {
                    "tab_item_name": "Create Component"
                },
                {
                    "tab_item_name": "Edit Component"
                }
            ]
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "UserPreferenceTab",
            "tab_name": "Preference",
            "tab_id": "preference",
            "tab_icon": "fa-cog",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": [
                {
                    "tab_item_name": "Themes"
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
                "have_toolbar": True,
                "toolbar_color": [
                    219,
                    134,
                    37
                ]
            },
            "tab_class_name": "UserWikiTab",
            "tab_name": "Wiki",
            "tab_id": "wiki",
            "tab_icon": "fa-book",
            "tab_icon_class": "font_awesome",
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
        self.default_tab_name = "Account"

        self.tab_class_collection = [UserAccountTab(),
                                     UserComponentTab(),
                                     UserPreferenceTab(),
                                     UserHelpTab()]
        self._populate()


# Tabs --------------------------------------------------
class UserAccountTab(TabBase):
    def __init__(self, **kwargs):
        super(UserAccountTab, self).__init__(**kwargs)
        self.__name__ = "UserAccountTab"


class UserComponentTab(TabBase):
    def __init__(self, **kwargs):
        super(UserComponentTab, self).__init__(**kwargs)
        self.__name__ = "UserComponentTab"


class UserPreferenceTab(TabBase):
    def __init__(self, **kwargs):
        super(UserPreferenceTab, self).__init__(**kwargs)
        self.__name__ = "UserPreferenceTab"


class UserHelpTab(TabBase):
    def __init__(self, **kwargs):
        super(UserHelpTab, self).__init__(**kwargs)
        self.__name__ = "UserHelpTab"
