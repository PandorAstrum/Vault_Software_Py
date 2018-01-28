# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
theme_text_color must be ['Primary', 'Secondary', 'Hint', 'Error', 'Custom', 'ContrastParentBackground']
"""
from kivymd.label import MDLabel


class Spawn():
    def add_md_label(self, font_style="Body1", theme_text_color="Secondary",
                     text="msg here", size_hint_y=None,
                     halign="left", valign="top"):
        lbl = MDLabel(font_style=font_style, theme_text_color=theme_text_color,
                      text=text, size_hint_y=size_hint_y, halign=halign, valign=valign)
        return lbl
