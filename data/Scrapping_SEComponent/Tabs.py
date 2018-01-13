# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

__all__ = [
    "ScrappingLinkedInTab"
]

class ScrappingLinkedInTab(ScrollView):
    def __init__(self, **kwargs):
        super(ScrappingLinkedInTab, self).__init__(**kwargs)
        self.__name__ = "ScrappingLinkedInTab"
