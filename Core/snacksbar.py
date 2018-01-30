# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivymd.snackbar import Snackbar


class Snacks:
    def snacks(self, type, message):
        if type == 'simple':
            Snackbar(text=message).show()
        elif type == 'button':
            Snackbar(text=message, button_text="with a button!",
                     button_callback=lambda *args: 2).show()
        elif type == 'verylong':
            Snackbar(text=message).show()
