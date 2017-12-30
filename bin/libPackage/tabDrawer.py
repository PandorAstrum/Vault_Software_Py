# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from functools import partial

from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.actionbar import ActionToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, SwapTransition, SlideTransition, Screen
from kivy.uix.togglebutton import ToggleButton
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerToolbar, NavigationDrawerIconButton
from kivymd.toolbar import Toolbar

from bin.libPackage.iconfonts import icon
from data.lib.generalUtility import colorScale
from data.lib.jsonUtility import getJsonFile, dumpKeyValue

tabWithDrawerKV = """
<TabWithDrawer>:
    NavigationLayout:
        id: nav_layout_id
        BoxLayout:
            # MDNavigationDrawer add here --------------------------------------
            id: nav_drawer
            orientation: "horizontal"

        BoxLayout:
            # Toolbar add here -------------------------------------------------
            orientation: "vertical"
            id: toolbar_id
            canvas:
                Color:
                    rgb: C('5BAD00')
                Rectangle:
                    pos: self.pos
                    size: self.size
            # Toolbar:
            #     # must have top bar
            #
                # size_hint_y: 0.1
                # right_action_items: [['dots-vertical', lambda x: self.parent.parent.parent.toggle_nav_drawer()]]
            # BoxLayout:
            #     id: content_id
            #     orientation: "vertical"
            #     Button:
            #         text: "OKAY"
"""
tabWithoutDrawerKV = """
<TabWithoutDrawer>:
    BoxLayout:
        orientation: "vertical"
        canvas:
            Color:
                rgb: C('5BAD00')
            Rectangle:
                pos: self.pos
                size: self.size
"""
CustomToolbarKV = """
# <CustomToolbar>:
#     size_hint_y: 0.1
"""
custom_block = """
<CustomBlock>:
    id: content_id
    orientation: "vertical"
    Button:
        text: "Okay"
        on_release: self.parent.testPress()
"""






class TabWithDrawer(Screen):

    def __init__(self, **kwargs):
        super(TabWithDrawer, self).__init__()
        self.name = kwargs.get("tab_name")
        self.tab_type = kwargs.get("tab_type")
        self.tab_content = kwargs.get("tab_content")
        self.toolbar_dict = kwargs.get("toolbar")
        self.on_create()

    @mainthread
    def on_create(self):
        # TODO: Create the appropriate drawer

        if self.tab_type == "list":
            #drawer
            customdrawer = TypeListDrawer(drawer_name=self.name, drawer_item_list=self.tab_content)
            self.ids.nav_drawer.add_widget(customdrawer)
            #toolbar
            tlbar = CustomToolbar(toolbar_color=self.toolbar_dict["color"])
            self.ids.toolbar_id.add_widget(tlbar)
            #block
            block = CustomBlock()
            self.ids.toolbar_id.add_widget(block)
        elif self.tab_type == "basic":
            pass
        # TODO: Create the appropriate toolbar
        # TODO: Create appropriate Screen Manager
        # create the navigation drawer according to type
        # if (self.tab_type == "list"):
        #     # add toolbar
        #     c = CustomListToolbar()
        #     self.ids.toolbar_id.add_widget(c)
        #     # add boxlayout
        #     b = CustomBlock()
        #     self.ids.toolbar_id.add_widget(b)
        #     # add drawer list
        #     instance = TypeListDrawer(drawer_name=self.name, drawer_item_list=self.tab_content)
        #     self.ids.nav_drawer.add_widget(instance)
        # elif (self.tab_type == "basic"):
        #     # no toolbar
        #     c = CustomBasicToolbar()
        #     self.ids.toolbar_id.add_widget(c)
        #     # add boxlayout
        #     b = CustomBlock()
        #     self.ids.toolbar_id.add_widget(b)
        #     instance = TypeBasicDrawer()
        #     self.ids.nav_drawer.add_widget(instance)
        #     pass
        # add screen based on tab type and assign to ids

class TabWithoutDrawer(Screen):
    def __init__(self, **kwargs):
        super(TabWithoutDrawer, self).__init__()

class CustomToolbar(Toolbar):
    def __init__(self, **kwargs):
        super(CustomToolbar, self).__init__()
        self.toolbar_color = kwargs.get("toolbar_color")
        temp_color_list = []
        for i in self.toolbar_color:
            result = colorScale(i)
            temp_color_list.append(result)
        temp_color_list.append(1)
        self.size_hint_y = 0.1
        self.right_action_items = [['dots-vertical', lambda x: self.parent.parent.parent.toggle_nav_drawer()]]
        self.md_bg_color = temp_color_list

class CustomBasicToolbar(Toolbar):
    def __init__(self, **kwargs):
        super(CustomBasicToolbar, self).__init__()

class CustomBlock(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomBlock, self).__init__()
        #TODO: import appropriate component class and implement build ui
        # attach the ui to appropriate ids

        print("Open webpage")


class TypeListDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(TypeListDrawer, self).__init__()
        self.drawer_item_list = kwargs.get("drawer_item_list")
        self.content_src_mngr = ScreenManager(transition=SlideTransition())

        # add screen to content

        # add a toolbar on the drawer
        self.toolbar = DrawerToolbar(drawer_name=kwargs.get("drawer_name"))
        self.add_widget(self.toolbar)
        # add list of buttons
        for i in self.drawer_item_list:
            ins = DrawerIconBtn(drawer_item_name=i["tab_item_name"], on_release=print("working"))
            self.add_widget(ins)

class DrawerIconBtn(NavigationDrawerIconButton):
    def __init__(self, **kwargs):
        super(DrawerIconBtn, self).__init__()
        self.icon = "checkbox-blank-circle"
        self.text = kwargs.get("drawer_item_name")
        # self.on_release = print("working")
        # self.on_release: app.root.ids.scr_mngr.current = 'accordion'

class DrawerToolbar(NavigationDrawerToolbar):
    def __init__(self, **kwargs):
        super(DrawerToolbar, self).__init__()
        self.title = kwargs.get("drawer_name")
        self.elevation = 1

class TypeBasicDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(TypeBasicDrawer, self).__init__()