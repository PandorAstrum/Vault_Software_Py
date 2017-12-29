# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.lang import Builder

class ComponentBase:
    def __init__(self, *args, **kwargs):
        self.json_settings = None
        self.kv = """
        """
        self.build_ui(self.kv)

    @classmethod
    def build_ui(cls, *args, **kwargs):
        Builder.load_string(*args)
        print(f"Building UI from {cls.__name__}")