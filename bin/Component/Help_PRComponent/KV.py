# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
__all__ = [
    "kv"
]

help_general_tab_kv = """
<HelpGeneralTab>:
    BoxLayout:
        Button:
            text: "General Tab"
"""
help_account_tab_kv = """
<HelpAccountTab>:
    BoxLayout:
        Button:
            text: "Account Tab"
"""
help_wiki_tab_kv = """
<HelpHelpTab>:
    BoxLayout:
        Button:
            text: "Help Tab"
"""

kv = help_account_tab_kv \
     + help_general_tab_kv \
     + help_wiki_tab_kv