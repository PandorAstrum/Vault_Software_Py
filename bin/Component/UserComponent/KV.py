# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

kv = """
<UserGeneralTab>:
    BoxLayout:
        Button:
            text: "General Tab"

<UserAccountTab>:
    canvas:
        Color:
            rgb: C('#000000')
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        # height: dp(200)
        center_y: self.parent.center_y
        MDRaisedButton:
            size_hint: None, None
            size: 3 * dp(48), dp(48)
            center_x: self.parent.center_x
            text: 'Change theme'
            on_release: MDThemePicker().open()
            opposite_colors: True
            pos_hint: {'center_x': 0.5}
        MDLabel:
            text: f"Current Theme-- Theme Style :{app.theme_cls.theme_style}, Theme Primary Palette :{app.theme_cls.primary_palette}, Theme Accent Palette :{app.theme_cls.accent_palette}"
            theme_text_color: 'Primary'
            pos_hint: {'center_x': 0.5}
            halign: 'center'

<UserHelpTab>:
    BoxLayout:
        Button:
            text: "Help Tab"
"""