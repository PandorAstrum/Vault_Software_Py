# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivymd.snackbar import Snackbar


class Snacks(object):
    def dismiss(self, instance, call_back):
        if call_back is not None:
            call_back()
        instance.die()

    def snacks(self, type="simple", message="msg", btn_text="Okay", btn_callback=None, duration=3):
        if type == 'simple':
            Snackbar(text=message, duration=duration).show()
        elif type == 'button':
            Snackbar(text=message, button_text=btn_text,
                     button_callback=lambda *args: self.dismiss(btn_callback), duration=duration).show()
        elif type == 'verylong':
            Snackbar(text=message, duration=duration).show()
