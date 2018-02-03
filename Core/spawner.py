# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
theme_text_color must be ['Primary', 'Secondary', 'Hint', 'Error', 'Custom', 'ContrastParentBackground']
"""
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.button import MDIconButton
from kivymd.card import MDCard
from kivymd.label import MDLabel
from kivymd.selectioncontrols import MDCheckbox
from kivymd.textfields import MDTextField
from kivymd.theming import ThemableBehavior


class Spawn(ThemableBehavior):
    # def __init__(self, **kwargs):
    #     super(Spawn, self).__init__(**kwargs)
    def add_md_label(self, font_style="Body1", theme_text_color="Secondary",
                     text="msg here", size_hint_y=None,
                     halign="left", valign="top"):
        lbl = MDLabel(font_style=font_style, theme_text_color=theme_text_color,
                      text=text, size_hint_y=size_hint_y, halign=halign, valign=valign)
        return lbl

    def add_MDCard(self):
        return MDCard()

    def add_BoxLayout(self, orientation= "horizontal"):
        box = BoxLayout()
        box.orientation = orientation
        return box

    def dp_double(self, first_value, second_value):
        return (dp(first_value), dp(second_value))

    def dp_single(self, value):
        return dp(value)

    def add_MDCheckbox(self, lbl_association=None, group=None):
        def _change(instance):
            if chk.active:
                chk.color = self.theme_cls.accent_color
                if lbl_association != None:
                    lbl_association.theme_text_color = "Primary"
            else:
                chk.color = self.theme_cls.secondary_text_color
                if lbl_association != None:
                    lbl_association.theme_text_color = "Secondary"

        chk = MDCheckbox()
        chk.size_hint = (None, None)
        chk.size = (dp(48), dp(48))
        chk.pos_hint= {'center_x': 0.5, 'center_y': 0.5}
        chk.bind(on_release=_change)
        chk.color =  self.theme_cls.secondary_text_color
        if lbl_association != None:
            lbl_association.theme_text_color = "Secondary"
        if group !=None:
            chk.group = group
        return chk

    def add_MDLabel(self, text):
        lbl = MDLabel()
        lbl.size_hint_x= None
        lbl.bind(width=lbl.setter("width"))
        lbl.text= text
        lbl.theme_text_color = "Primary"
        return lbl

    def add_MDIconButton(self, icon_name):
        md_icon_btn = MDIconButton()
        md_icon_btn.icon = icon_name
        return md_icon_btn

    def add_MDTextField(self, hint_text, color_mode):
        md_text_field = MDTextField()
        md_text_field.hint_text = hint_text
        md_text_field.color_mode = color_mode
        return md_text_field

    def add_HSeparator(self):
        return HSeparator()

    def add_VSeparator(self):
        return VSeparator()

    def add_gap(self, height_dp, width_dp):
        return Gap(height_dp= height_dp, width_dp= width_dp)


class Separator(Widget):
    pass

class HSeparator(Separator):
    pass

class VSeparator(Separator):
    pass

class Gap(BoxLayout):
    height_dp = ObjectProperty(None, allownone=True)
    width_dp = ObjectProperty(None, allownone=True)
    def __init__(self, **kwargs):
        super(Gap, self).__init__(**kwargs)