# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from functools import partial

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, FadeTransition, FallOutTransition, RiseInTransition
from kivy.uix.togglebutton import ToggleButton
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerToolbar, NavigationDrawerIconButton
from kivymd.toolbar import Toolbar

from bin.libPackage.iconfonts import icon
from bin.libPackage.paUtility import colorScale


class ComponentBase(Screen):
    """
    docString
    """
    def __init__(self, **kwargs):
        super(ComponentBase, self).__init__(**kwargs)
        self.src_mngr = ScreenManager(transition=RiseInTransition())
        self.tab_collection = []


    def _populate(self, **kwargs):
        self.name = kwargs.get("component_name")
        self.component_id = kwargs.get("component_id")
        self.component_icon = kwargs.get("component_icon")
        self.component_tab_info = kwargs.get("component_tab_info")
        self.tab_group_name = kwargs.get("tab_group_name")
        self.kv = kwargs.get("kv")
        self.build_ui(self.kv)
        self.tab_classes = kwargs.get("tab_classes")
        self._make(kwargs.get("default_tab_name"))

    def _make(self, default_tab_name):
        tab_dict = {}

        for each_tab in self.component_tab_info:
            tab_dict[each_tab["tab_name"]] = each_tab["tab_icon"]

            for each_tab_class in self.tab_classes:
                if each_tab_class.name == each_tab["tab_class_name"]:
                    instance = TabBase(tab_type=each_tab["tab_type"],
                                       tab_name=each_tab["tab_name"],
                                       tab_content=each_tab["tab_content"],
                                       toolbar=each_tab["toolbar"],
                                       tab_class_instance=each_tab_class)
                    self.src_mngr.add_widget(instance)

        self.ids.src_mngr_level_3_id.add_widget(self.src_mngr)

        # tabs
        def callback(instance):  # tab button callback
            self.src_mngr.current = instance.id
            for i in self.tab_collection:
                if (i.id == instance.id):
                    i.size_hint = (1.3, 0.09)
                else:
                    i.size_hint = (1, 0.09)

        position_y = 1
        for key, value in tab_dict.items():
            btn = ToggleButton(id=key,
                               markup=True,
                               state="normal",
                               font_size=10,
                               halign="center",
                               text="%s\n%s" % ((icon(value, 18)), key),
                               size_hint=(1, 0.09),
                               pos_hint={"x": 0, "top": position_y},
                               group=self.tab_group_name)
            btn.allow_no_selection = False
            btn.bind(on_press=partial(callback))
            self.ids.tab_panel_id.add_widget(btn)
            position_y -= 0.09
            self.tab_collection.append(btn)

        # default behaviour
        for i in self.tab_collection:
            if i.id == default_tab_name:
                i.state = "down"
                self.src_mngr.current = i.id
                i.size_hint = (1.3, 0.09)



    @classmethod
    def build_ui(cls, *args, **kwargs):
        Builder.load_string(*args)


class TabBase(Screen):
    def __init__(self, **kwargs):
        super(TabBase, self).__init__()
        self.name = kwargs.get("tab_name")
        self.tab_content = kwargs.get("tab_content")
        self.toolbar_dict = kwargs.get("toolbar")
        self.tab_type = kwargs.get("tab_type")
        self.tab_class_instance = kwargs.get("tab_class_instance")
        self._make(self.tab_type)

    def _make(self, tab_type):
        if tab_type == "list":
            #drawer (list type)
            drawer = TypeListDrawer(drawer_name=self.name, drawer_item_list=self.tab_content)
            self.ids.nav_drawer.add_widget(drawer)
            #toolbar
            if self.toolbar_dict["have_toolbar"] == True:
                tlbar = CustomToolbar(toolbar_color=self.toolbar_dict["toolbar_color"])
                self.ids.toolbar_id.add_widget(tlbar)
            #block
            # block = self.tab_class_instance()
            # block = CustomBlock()
            self.ids.toolbar_id.add_widget(self.tab_class_instance)
        # elif tab_type == "info":
        #     #drawer (info type)
        #     drawer = TypeListDrawer(drawer_name=self.name, drawer_item_list=self.tab_content)
        #     self.ids.nav_drawer.add_widget(drawer)
        #     #toolbar
        #     tlbar = CustomToolbar(toolbar_color=self.toolbar_dict["color"])
        #     self.ids.toolbar_id.add_widget(tlbar)
        #     #block change
        #     block = CustomBlock()
        #     self.ids.toolbar_id.add_widget(block)
        #     pass
        # elif tab_type == "custom":
        #     pass
        # elif tab_type == "null":
        #     self.remove_widget(self.ids['nav_layout_id'])
        #     box = BoxLayout(id="toolbar_id")
        #     self.add_widget(box)
        #     #block simple
        #     block = CustomBlock()
        #     self.ids.toolbar_id.add_widget(block)


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

class DrawerToolbar(NavigationDrawerToolbar):
    def __init__(self, **kwargs):
        super(DrawerToolbar, self).__init__()
        self.title = kwargs.get("drawer_name")
        self.elevation = 1

class DrawerIconBtn(NavigationDrawerIconButton):
    def __init__(self, **kwargs):
        super(DrawerIconBtn, self).__init__()
        self.icon = "checkbox-blank-circle"
        self.text = kwargs.get("drawer_item_name")
        # self.on_release = print("working")
        # self.on_release: app.root.ids.scr_mngr.current = 'accordion'

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

class DefaultTab(Screen):
    def __init__(self, **kwargs):
        super(DefaultTab, self).__init__(**kwargs)