# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

__all__ = [
    "UserGeneralTab",
    "UserAccountTab",
    "UserHelpTab"
]

class UserGeneralTab(ScrollView):
    def __init__(self, **kwargs):
        super(UserGeneralTab, self).__init__(**kwargs)
        self.__name__ = "UserGeneralTab"

class UserAccountTab(ScrollView):
    def __init__(self, **kwargs):
        super(UserAccountTab, self).__init__(**kwargs)
        self.__name__ = "UserAccountTab"

class UserHelpTab(ScrollView):
    def __init__(self, **kwargs):
        super(UserHelpTab, self).__init__(**kwargs)
        self.__name__ = "UserHelpTab"