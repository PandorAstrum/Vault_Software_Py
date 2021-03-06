# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# File names
import os

__author__          = "Ashiquzzaman Khan"
__copyright__       = "2018 GPL"
__desc__            = """App Settings"""

FILE_CONFIG_APP     = "config.cfg"
FILE_CONFIG_COMPONENT = "component_config.json"
FILE_LOG            = "vault.log"
FILE_ERROR          = "vault_error.log"

# Folders
FOLDER_CONFIG       = "Config"
FOLDER_LOG          = "\\Log"
FOLDER_SECONDARY_COMPONENT = "SEComponents"
FOLDER_PRIMARY_COMPONENT = "bin\\Component"
FOLDER_DOWNLOAD_DATA = "\\DOWNLOADS"
FOLDER_TEMP         = "\\Temp"
FOLDER_MAIN         = "\\Vault"
FOLDER_CORE         = "\\Core"
FOLDER_BIN          = "\\bin"
FOLDER_DLL          = "\\dll"
FOLDER_RES          = "\\res"
FOLDER_UTILS        = "\\utils"

# Version
APP_VERSION         = '0.0.1'
APP_NAME            = "Vault"
APP_AUTHOR          = "PandorAstrum"

# Copyrights
APP_EMAIL           = "primeintegerslab@gmail.com"

# directory and files relative to root
SOFTWARE_ROOT = os.path.normpath(os.path.abspath(os.path.dirname(__file__)) + os.sep + os.pardir)
CORE_ROOT           = os.path.join(SOFTWARE_ROOT, "Core")
BIN_ROOT            = os.path.join(SOFTWARE_ROOT, "bin")
DLL_ROOT            = os.path.join(SOFTWARE_ROOT, "dll")
RESOURCE_ROOT       = os.path.join(SOFTWARE_ROOT, "res")
UTILS_ROOT          = os.path.join(SOFTWARE_ROOT, 'utils')

TEST_ROOT           = os.path.join(SOFTWARE_ROOT, 'localDump')

