# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import sys

sys.path.append('/path/to/application/app/folder')
# from bin.libPackage.baseComponent import ComponentBase
from .Tabs import *

json_settings = {
    "id": "Planner",
    "component_name": "Planner_SEComponent",
    "icon": "fa-home",
    "status": False,
    "order": 500,
    "tab_group_name": "planner_tab_group",
    "tab": [
        {
            "toolbar" : {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "PlannerGeneralTab",
            "tab_name": "General",
            "tab_id": "general",
            "tab_icon": "fa-key",
            "tab_type": "list",
            "tab_content": []
        }
    ]
}


class Component():
    """
    docString
    """
    def __init__(self, **kwargs):
        super(Component, self).__init__()
        # self.name = kwargs.get("component_name")
        # self.component_id = kwargs.get("component_id")
        # self.component_icon = kwargs.get("component_icon")
        # self.component_tab_info = kwargs.get("component_tab_info")
        # self.tab_group_name = kwargs.get("tab_group_name")
        # self.default_tab_name = "General"

        # self.tab_class_collection = [UserAccountTab(),
        #                              UserComponentTab(),
        #                              UserPreferenceTab(),
        #                              UserHelpTab()]
        # self._populate()
