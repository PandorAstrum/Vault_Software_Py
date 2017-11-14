import os

from data.bin import mainApp
from data.lib import iconfonts
if '__main__' == __name__:

    data_path = os.getcwd()
    iconfonts.register('default_font', data_path + '\\res\\font\\fontawesome-webfont.ttf',
                       data_path + '\\res\\font\\font-awesome.fontd')
    mainApp.MainApp().run()
