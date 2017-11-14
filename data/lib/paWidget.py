from functools import partial

from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.actionbar import ActionToggleButton
from kivy.uix.screenmanager import ScreenManager, SwapTransition, SlideTransition, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerToolbar

from data.lib.iconfonts import icon
from data.lib.jsonUtility import getJsonFile, dumpKeyValue

root_widget_layout = """
#: import icon data.lib.iconfonts.icon
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout

#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

# Main Root
<RootWidget>:
    orientation: "vertical"
    on_size: self.resize_window(self.size)

#   Action Bar ---------------------------------------------------------------
    ActionBar:
        pos_hint: {'top':1}
        # App Logo
        ActionView:
            orientation: 'horizontal'
            padding: '5dp'
            use_separator: True
            ActionPrevious:
                title: ''
                with_previous: False

            # contextual DropDown
            ActionOverflow: # Build Content From PY
                id: action_overflow_id

            # DropDown Selection
            ActionGroup: # Build Content From PY
                id: act_spinner_id
                markup:True
                text: ""
                mode: 'spinner'
                size_hint_x: None


            ActionButton:
                halign: "center"
                markup: True
                text:"%s"%(icon('fa-bell', 20))
            ActionButton:
                halign: "center"
                markup: True # Always turn markup on
                text:"%s"%(icon('fa-flag', 20))
            ActionButton:
                halign: "center"
                markup: True # Always turn markup on
                text:"%s"%(icon('fa-user', 20))

#Main screen Manager ---------------------------------------------------------

    BoxLayout:
        id: src_mngr_id
        canvas:
            Color:
                rgb: C('#AAAAAA')
            Rectangle:
                pos: self.pos
                size: self.size

# Bottom Bar
    BoxLayout:
        pos_hint: {'bottom':1}
        size_hint: 1, None
        height: "16px"
        canvas:
            Color:
                rgb: C('#1F1F1F')
            Rectangle:
                pos: self.pos
                size: self.size
"""
generic_component_widget_layout = """
<Generic_component_widget_screen>:
    BoxLayout:
        id: src_mngr_comp_id
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
generic_tab_widget_layout = """
<Generic_tab_widget_screen>:
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
"""
Builder.load_string(root_widget_layout + generic_component_widget_layout + generic_tab_widget_layout)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__()
        self.data = getJsonFile()
        self.dir = kwargs.get("directory") # change on dev build
        self.folder_name = kwargs.get("folder_name")
        self.view_file = kwargs.get("view_file")
        self.directory = self.dir + self.folder_name
        self.dict_of_component = {}
        self.src_mngr = ScreenManager(transition=SwapTransition())
        self.on_create()

    @mainthread
    def on_create(self):
        component_dict = {}
        temp_dict_ordered = {}

        for key, value in self.data.items():
            if (key == "component"):
                for all_component in value:
                    for each_component_name, each_component_fields in all_component.items():
                        if each_component_fields["status"] == True:
                            # initialize with generic class
                            instance = Generic_component_widget_screen(component_name=each_component_fields["id"],
                                                                       component_id=each_component_fields["id"],
                                                                       component_icon=each_component_fields["icon"],
                                                                       component_tab_info=each_component_fields["tab"],
                                                                       tab_group_name=each_component_fields[
                                                                           "tab_group_name"])
                            component_dict[each_component_fields["order"]] = instance

        for key in sorted(component_dict):  # Sorting
            temp_dict_ordered[key] = component_dict[key]

        for key in temp_dict_ordered:  # adding screen widget to screen manager (by order)
            self.src_mngr.add_widget(temp_dict_ordered[key])
        self.ids.src_mngr_id.add_widget(self.src_mngr)

        def callback(instance):  # spinner button callback
            self.ids.act_spinner_id.text = instance.text
            self.src_mngr.current = instance.id

        for key in temp_dict_ordered:  # Spinner button
            ac_drpdwn_btn = ActionToggleButton(id=temp_dict_ordered[key].component_id,
                                               markup=True,
                                               text="%s" % (icon(temp_dict_ordered[key].component_icon, 20)) + "  " +
                                                    temp_dict_ordered[key].component_id,
                                               group="component_toggle")
            ac_drpdwn_btn.allow_no_selection = False
            ac_drpdwn_btn.bind(on_press=partial(callback))
            self.ids.act_spinner_id.add_widget(ac_drpdwn_btn)

    def resize_window(self, size):
        """
        RootWidget size dump settings key in json
        :param size: self.size
        :return: none
        """
        dumpKeyValue(self.data, "window_width", size[0])
        dumpKeyValue(self.data, "window_height", size[1])

class Generic_component_widget_screen(Screen):
    def __init__(self, **kwargs):
        super(Generic_component_widget_screen, self).__init__()
        self.name = kwargs.get("component_name")
        self.component_id = kwargs.get("component_id")
        self.component_icon = kwargs.get("component_icon")
        self.component_tab_info = kwargs.get("component_tab_info")
        self.tab_group_name = kwargs.get("tab_group_name")
        self.src_mngr_comp = ScreenManager(transition=SlideTransition())
        self.tab_collection = []
        self.on_create()

    @mainthread
    def on_create(self):
        tab_dict = {}
        for each_tab_dict in self.component_tab_info:
            tab_dict[each_tab_dict["tab_name"]] = each_tab_dict["tab_icon"]
            # initialize tab class widget and add to sc manger
            instance = Generic_tab_widget_screen(tab_name=each_tab_dict["tab_name"],
                                                 tab_icon=each_tab_dict["tab_icon"],
                                                 tab_type=each_tab_dict["tab_type"])
            self.src_mngr_comp.add_widget(instance)
        self.ids.src_mngr_comp_id.add_widget(self.src_mngr_comp)

        def callback(instance): #tab button callback
            self.src_mngr_comp.current = instance.id
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

class Generic_tab_widget_screen(Screen):
    def __init__(self, **kwargs):
        super(Generic_tab_widget_screen, self).__init__()
        self.name = kwargs.get("tab_name")
        # self.tab_id = kwargs.get("tab_id")
        self.tab_icon = kwargs.get("tab_icon")
        self.tab_type = kwargs.get("tab_type")
        self.on_create()

    @mainthread
    def on_create(self):
        # create the navigation drawer according to type
        if (self.tab_type == "list"):
            instance = TypeListDrawer(drawer_name=self.name)
            self.ids.nav_drawer.add_widget(instance)
        elif (self.tab_type == "basic"):
            pass
        # add screen based on tab type and assign to ids

class TypeListDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(TypeListDrawer, self).__init__()
        self.toolbar = DrawerToolbar(drawer_name=kwargs.get("drawer_name"))
        #TODO: add list of screen
        self.add_widget(self.toolbar)

class DrawerToolbar(NavigationDrawerToolbar):
    def __init__(self, **kwargs):
        super(DrawerToolbar, self).__init__()
        self.title = kwargs.get("drawer_name")
        self.elevation = 1

class TypeBasicDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(TypeBasicDrawer, self).__init__()