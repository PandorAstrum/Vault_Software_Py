# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from bin import mainApp
from utils import iconfonts, appDirs

if __name__ == "__main__":
    DATA_PATH = appDirs.get_current_directory()
    # web-fonts icons
    iconfonts.register('font_awesome', DATA_PATH + '\\res\\font\\fontawesome-webfont.ttf',
                       DATA_PATH + '\\res\\font\\font-awesome.fontd')
    mainApp.MainApp().run()
