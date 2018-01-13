# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.uix.scrollview import ScrollView

__all__ = [
    "PlannerGeneralTab"
]


class PlannerGeneralTab(ScrollView):
    def __init__(self, **kwargs):
        super(PlannerGeneralTab, self).__init__(**kwargs)
        self.__name__ = "PlannerGeneralTab"

