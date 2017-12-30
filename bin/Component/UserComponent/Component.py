# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.uix.boxlayout import BoxLayout

from bin.libPackage.baseComponent import ComponentBase, TabBase


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
            "tab_class_name": "GeneralTab",
            "tab_name": "General",
            "tab_id": "general",
            "tab_icon": "fa-user",
            "tab_type": "basic",
            "tab_content": []
        },
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "AccountTab",
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
            "tab_class_name": "HelpTab",
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
        self.default_tab_name = "General"
        self.kv = """
<GeneralTab>:
    BoxLayout:
        canvas:
            color:
                rgb: C('#222222')

<AccountTab>:
    BoxLayout:
        canvas:
            color:
                rgb: C('#222222')

<HelpTab>:
    BoxLayout:
        canvas:
            color:
                rgb: C('#222222')
        """
        # tab class
        self.tab_class = (GeneralTab(), AccountTab(), HelpTab())
        self._populate(component_name=kwargs.get("component_name"),
                       component_id=kwargs.get("component_id"),
                       component_icon=kwargs.get("component_icon"),
                       component_tab_info=kwargs.get("component_tab_info"),
                       tab_group_name=kwargs.get("tab_group_name"),
                       kv=self.kv,
                       default_tab_name=self.default_tab_name,
                       tab_classes=self.tab_class)

        # tab create instructions


class GeneralTab(BoxLayout):
    def __init__(self, **kwargs):
        super(GeneralTab, self).__init__()
        self.name = "GeneralTab"

class AccountTab(BoxLayout):
    def __init__(self, **kwargs):
        super(AccountTab, self).__init__(**kwargs)
        self.name = "AccountTab"

class HelpTab(BoxLayout):
    def __init__(self, **kwargs):
        super(HelpTab, self).__init__(**kwargs)
        self.name = "HelpTab"