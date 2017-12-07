from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, FadeTransition, WipeTransition
from kivymd.toolbar import Toolbar

from data.lib.essWidget import DrawerLayout, ViewDrawer
from data.lib import customBuilder as CustomBuilder
from data.bin.Component.UserComponent.drivers  import Drivers

from data.text.slidingtest import SlidingPanel
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase, NavigationLayout
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker



layout_base = """
<UserComponentBase>:
    BoxLayout:
        id: component_src_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 0.95, 1
        canvas:
            Color:
                rgb: C('#FFFFFF')
            Rectangle:
                pos: self.pos
                size: self.size

    # tabs
    FloatLayout:
        id: tab_panel_id
        # pos_hint: {"left": 1, "y": 0}
        size_hint: 0.05, 1
        canvas:
            Color:
                rgb: C('#222222')
            Rectangle:
                pos: self.pos
                size: self.size
"""
layout_tabs_screens = """
<User_t_General_screen>:
    NavigationLayout:
        id: nav_layout_id
        BoxLayout:
            id: nav_drawer
            orientation: "horizontal"
            # add the MDNavigationDrawer class here

        BoxLayout:
            orientation: "vertical"
            # pos_hint: {"x":0, "bottom":1}
            # size_hint_y: 1
            canvas:
                Color:
                    rgb: C('5BADEE')
                Rectangle:
                    pos: self.pos
                    size: self.size
            Toolbar:
                id: toolbar_id
                size_hint_y: 0.1
                right_action_items: [['dots-vertical', lambda x: self.parent.parent.parent.toggle_nav_drawer()]]
            Button:
                text: "OKAY"


                # md_bg_color: app.theme_cls.primary_color
                # background_palette: 'Primary'
                # background_hue: '500'


                # pos_hint: {"right": 1, "y": 0}
        # canvas:
        #     Color:
        #         rgb: C('#222d32')
        #     Rectangle:
        #         pos: self.pos
        #         size: self.size



<User_t_Accounts_screen>:
    RelativeLayout:
        id: section_scene_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 1, 1
        canvas:
            Color:
                rgb: C('A2DF9F')
            Rectangle:
                pos: self.pos
                size: self.size

<User_t_Settings_screen>:
    RelativeLayout:
        id: section_scene_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 1, 1
        canvas:
            Color:
                rgb: C('5BADEE')
            Rectangle:
                pos: self.pos
                size: self.size


"""
layer_default = """
<User_t_Default_Screen>:
    canvas:
        Color:
            rgb: C('#AAAAAA')
        Rectangle:
            pos: self.pos
            size: self.size
"""
layout_sections = """
"""
CustomBuilder.build_generic_ui(layout_base+layout_tabs_screens+layer_default+layout_sections)

# Component Screens -----------------------------------------------------
class UserComponentBase(Screen):
    def __init__(self, **kwargs):
        super(UserComponentBase, self).__init__()
        self.dir = kwargs.get("directory")
        self.name = "User"              # name for the screen when initialized
        self.class_id = "User"
        self.class_icon = "fa-home"
        self.view_file = kwargs.get("view_file")  # the file containing views
        self.status = True              # if the plugin is active or not
        self.order = 1                  # order of the component
        self.src_mngr = ScreenManager(transition=SlideTransition())
        self.dict_of_tabs = {}
        self.tab_collection = []
        self.group_name = "user_tab"    # name of the toggle button group
        CustomBuilder.On_create_component(directory=self.dir,
                                          view_file=self.view_file,
                                          component_name=self.name,
                                          dict_of_tab=self.dict_of_tabs,
                                          src_mngr=self.src_mngr,
                                          src_mngr_id=self.ids.component_src_id,
                                          tab_collection=self.tab_collection,
                                          group_name=self.group_name,
                                          tab_panel_id=self.ids.tab_panel_id)


# Tab Screens ------------------------------------------------------------
class User_t_Default_Screen(Screen):
    def __init__(self, **kwargs):
        super(User_t_Default_Screen, self).__init__()
        self.name = "default"
        self.class_id = "Default"
        self.class_icon = "fa-user"
        self.status = True  # if the plugin is active or not
        self.order = 0

class User_t_General_Screen(Screen):
    def __init__(self,**kwargs):
        super(User_t_General_Screen, self).__init__()
        self.name = "general"
        self.class_id = "General"
        self.class_icon = "fa-user"
        self.status = True              # if the plugin is active or not
        self.order = 1
        # self.list_of_tabs = {}


        self.drawer = ViewDrawer(drawer_name="User Component")


        self.section_screen_manager = ScreenManager(transition=FadeTransition())
        self.ids.nav_drawer.add_widget(self.drawer)

        # self.has_drawer = True
        # self.drawer_type = "list_btn"

    def printMe(self):
        print("action")

class User_t_Accounts_Screen(Screen):
    def __init__(self, **kwargs):
        super(User_t_Accounts_Screen, self).__init__()
        self.name = "accounts"
        self.class_id = "Accounts"
        self.class_icon = "fa-key"
        self.order = 2
        self.list_of_sections = {}
        self.section_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))

        self.status = True
        self.has_drawer = False
        self.drawer_type = "list_btn"

class User_t_Settings_Screen(Screen):
    def __init__(self, **kwargs):
        super(User_t_Settings_Screen, self).__init__()
        self.name = "settings"
        self.class_id = "Settings"
        self.class_icon = "fa-gear"
        self.order = 3
        self.status = True


class TitleToolbar(Toolbar):

    pass