# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

import sys
import os
import platform
import re

class LocalStorage(object):

    def __init__(self, debug=True):
        self.debug = debug
        if self.debug:
            self.current_dir = os.getcwd()
            self.one_up = os.path.normpath(os.getcwd() + os.sep + os.pardir)
            self.root = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault"
            self.dump = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\localDump"
        else:
            self.user_home = os.path.expanduser('~')
            self.desktop = self.user_home + "\\Desktop\\"
            self.cacheDir = os.getenv("LOCALAPPDATA") + "\\PandorAstrum\\"
            self.image_dir = self.cacheDir + "\\Images\\"
            self.database_dir = self.cacheDir

    def make_dir(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def get_current_dir(self, file=None):
        if not hasattr(self.get_current_dir, "dir"):
            if hasattr(sys, "frozen"):
                dir = os.path.dirname(sys.executable)
            elif "__file__" in globals():
                dir = os.path.dirname(os.path.realpath(__file__))
            else:
                dir = os.getcwd()
            self.get_current_dir().dir = dir
        # If file is None return current directory without trailing slash.
        if file is None:
            file = ""
        # Only when relative path.
        if not file.startswith("/") and not file.startswith("\\") and (
                not re.search(r"^[\w-]+:", file)):
            path = self.get_current_dir().dir + os.sep + file
            if platform.system() == "Windows":
                path = re.sub(r"[/\\]+", re.escape(os.sep), path)
            path = re.sub(r"[/\\]+$", "", path)
            return path
        return str(file)

