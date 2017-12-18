# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

import os

from bin import mainApp
from bin.libPackage import iconfonts

if __name__ == "__main__":
    DATA_PATH = os.getcwd()
    iconfonts.register('default_font', DATA_PATH + '\\res\\font\\fontawesome-webfont.ttf',
                       DATA_PATH + '\\res\\font\\font-awesome.fontd')
    mainApp.MainApp().run()
