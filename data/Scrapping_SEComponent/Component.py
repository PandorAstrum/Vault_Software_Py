# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from bin.libPackage.baseComponent import ComponentBase
from .Tabs import *

json_settings = {
    "id": "Scrapping",
    "component_name": "Scrapping_SEComponent",
    "icon": "fa-book",
    "status": False,
    "order": 501,
    "tab_group_name": "Scrapping_tab_group",
    "tab": [
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "ScrappingLinkedInTab",
            "tab_name": "LinkedIn",
            "tab_id": "linkedin",
            "tab_icon": "fa-user",
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
        self.default_tab_name = "LinkedIn"
        self.tab_class_collection = [HelpGeneralTab(), HelpAccountTab(), HelpHelpTab()]
        self._populate()
