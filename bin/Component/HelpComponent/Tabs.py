# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

__all__ = [
    "HelpGeneralTab",
    "HelpAccountTab",
    "HelpHelpTab"
]

class HelpGeneralTab(ScrollView):
    def __init__(self, **kwargs):
        super(HelpGeneralTab, self).__init__(**kwargs)
        self.__name__ = "HelpGeneralTab"

class HelpAccountTab(ScrollView):
    def __init__(self, **kwargs):
        super(HelpAccountTab, self).__init__(**kwargs)
        self.__name__ = "HelpAccountTab"

class HelpHelpTab(ScrollView):
    def __init__(self, **kwargs):
        super(HelpHelpTab, self).__init__(**kwargs)
        self.__name__ = "HelpHelpTab"