# -*- coding: utf-8 -*-

from bin import mainApp
from utils import iconfonts, appDirs

__author__      = "Ashiquzzaman Khan"
__copyright__   = "2018 GPL"
__desc__        = """Main Exe File to run"""

if __name__ == "__main__":

    DATA_PATH = appDirs.get_current_directory()
    # web-fonts icons
    iconfonts.register('font_awesome', DATA_PATH + '\\res\\font\\fontawesome-webfont.ttf',
                       DATA_PATH + '\\res\\font\\font-awesome.fontd')
    iconfonts.register('wb1', DATA_PATH + '\\res\\font\\wb1.ttf',
                       DATA_PATH + '\\res\\font\\wb1.fontd')
    mainApp.MainApp().run()
