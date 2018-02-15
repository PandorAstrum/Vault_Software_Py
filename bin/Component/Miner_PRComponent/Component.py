# -*- coding: utf-8 -*-

from Core.baseInterface import ComponentBase, TabBase
from bin.Component.Miner_PRComponent import MinerSeleniumTabDrivers
from bin.Component.Miner_PRComponent import MinerUtilityTabDrivers

__all__ = [
    "Component",
    "json_settings"
]
__author__      = "Ashiquzzaman Khan"
__copyright__   = "2018 GPL"
__desc__        = """Miner Component"""

json_settings = {
    "id": "Miner",
    "component_name": "Miner_PRComponent",
    "icon": "fa-gg",
    "icon_class": "",
    "status": True,
    "order": 3,
    "version": "0.2",
    "tab_group_name": "miner_tab_group",
    "tab": [
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MinerScrapyTab",
            "tab_name": "Scrapy",
            "tab_id": "Scrapy",
            "tab_icon": "fa-globe",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MinerSeleniumTab",
            "tab_name": "Selenium",
            "tab_id": "selenium",
            "tab_icon": "fa-chrome",
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
            "tab_class_name": "MinerGrabberTab",
            "tab_name": "Grabber",
            "tab_id": "Grabber",
            "tab_icon": "fa-hand-grab-o",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MinerUtilityTab",
            "tab_name": "Utility",
            "tab_id": "Utility",
            "tab_icon": "fa-user-secret",
            "tab_icon_class": "font_awesome",
            "tab_type": "list",
            "tab_content": []
        },
        {
            "toolbar": {
                "have_toolbar": False,
                "toolbar_color": []
            },
            "tab_class_name": "MinerWikiTab",
            "tab_name": "Wiki",
            "tab_id": "wiki",
            "tab_icon": "fa-book",
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

        self.tab_class_collection = [MinerScrapyTab(),
                                     MinerSeleniumTab(),
                                     MinerGrabberTab(),
                                     MinerUtilityTab(),
                                     MinerWikiTab()
                                     ]
        self._populate()

# Tabs --------------------------------------------------
class MinerScrapyTab(TabBase):
    def __init__(self, **kwargs):
        super(MinerScrapyTab, self).__init__(**kwargs)
        self.__name__ = "MinerScrapyTab"

class MinerSeleniumTab(TabBase):
    def __init__(self, **kwargs):
        super(MinerSeleniumTab, self).__init__(**kwargs)
        self.__name__ = "MinerSeleniumTab"
        self.drivers = MinerSeleniumTabDrivers(instances=self)

class MinerGrabberTab(TabBase):
    def __init__(self, **kwargs):
        super(MinerGrabberTab, self).__init__(**kwargs)
        self.__name__ = "MinerGrabberTab"

class MinerUtilityTab(TabBase):
    def __init__(self, **kwargs):
        super(MinerUtilityTab, self).__init__(**kwargs)
        self.__name__ = "MinerUtilityTab"
        self.drivers = MinerUtilityTabDrivers(instances=self)

class MinerWikiTab(TabBase):
    def __init__(self, **kwargs):
        super(MinerWikiTab, self).__init__(**kwargs)
        self.__name__ = "MinerWikiTab"
