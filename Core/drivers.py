# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy._event import EventDispatcher

from Core.snacksbar import Snacks
from Core.spawner import Spawn

__all__         = [
    "DriverBase"
]
__author__      = "Ashiquzzaman Khan"
__copyright__   = "2018 GPL"
__desc__        = """ Base Interface for Drivers"""

class DriverBase(Snacks, Spawn, EventDispatcher):
    def __init__(self, **kwargs):
        super(DriverBase, self).__init__(**kwargs)