# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from Core.baseInterface import ComponentBase, TabBase
from bin.Component.Mining_PRComponent.miningDrivers import MiningSeleniumTabDrivers

__all__ = [
    "Component",
    "json_settings"
]

json_settings = {
    "id": "Mining",
    "component_name": "Mining_PRComponent",
    "icon": "fa-gg",
    "status": True,
    "order": 3,
    "tab_group_name": "mining_tab_group",
    "tab": [
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MiningScrapyTab",
            "tab_name": "Scrapy",
            "tab_id": "Scrapy",
            "tab_icon": "fa-globe",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MiningSeleniumTab",
            "tab_name": "Selenium",
            "tab_id": "selenium",
            "tab_icon": "fa-chrome",
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
            "tab_class_name": "MiningHelpTab",
            "tab_name": "Help",
            "tab_id": "help",
            "tab_icon": "fa-question",
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
        }
    ]
}

# main Component ----------------------------------------
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
        self.default_tab_name = "Scrapy"

        self.tab_class_collection = [MiningScrapyTab(),
                                     MiningSeleniumTab(),
                                     MiningHelpTab()
                                     ]
        self._populate()

# Tabs --------------------------------------------------
class MiningScrapyTab(TabBase):
    def __init__(self, **kwargs):
        super(MiningScrapyTab, self).__init__(**kwargs)
        self.__name__ = "MiningScrapyTab"

class MiningSeleniumTab(TabBase):
    def __init__(self, **kwargs):
        super(MiningSeleniumTab, self).__init__(**kwargs)
        self.__name__ = "MiningSeleniumTab"
        self.drivers = MiningSeleniumTabDrivers(instances=self)

class MiningHelpTab(TabBase):
    def __init__(self, **kwargs):
        super(MiningHelpTab, self).__init__(**kwargs)
        self.__name__ = "MiningHelpTab"
