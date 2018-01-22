# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from kivymd.snackbar import Snackbar

# notification
class Notify:
    pass
# snackbar
class Snacks:
    def snackbar(self, type="simple", msg="YourMessage"):
        if type == 'simple':
            Snackbar(text=msg).show()
        elif type == 'button':
            Snackbar(text=msg, button_text="with a button!", button_callback=lambda *args: 2).show()
        elif type == 'verylong':
            Snackbar(text=msg).show()
# xpop

class PopUp:
    pass