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

rootWidgetKV = """
#: import icon bin.libPackage.iconfonts.icon
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
ComponentsWidgetKV = """
<ComponentsWidget>:
    BoxLayout:
        id: src_mngr_comp_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 0.95, 1

    # tabs ---------------------------------------------
    FloatLayout:
        id: tab_panel_id
        size_hint: 0.05, 1
        canvas:
            Color:
                rgb: C('#222222')
            Rectangle:
                pos: self.pos
                size: self.size

"""
TabWithDrawerKV = """
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
TabWithoutDrawerKV = """
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
Builder.load_string(rootWidgetKV + ComponentsWidgetKV + TabWithDrawerKV + TabWithoutDrawerKV + CustomToolbarKV + custom_block)

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
        self.ls = kwargs.get("ls")
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
                            instance = ComponentsWidget(component_name=each_component_fields["id"],
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

class ComponentsWidget(Screen):
    def __init__(self, **kwargs):
        super(ComponentsWidget, self).__init__()
        self.name = kwargs.get("component_name")
        self.component_id = kwargs.get("component_id")
        self.component_icon = kwargs.get("component_icon")
        self.component_tab_info = kwargs.get("component_tab_info")
        self.tab_group_name = kwargs.get("tab_group_name")
        self.src_mngr_comp = ScreenManager(transition=SlideTransition(direction="down"))
        self.tab_collection = []
        self.on_create()

    @mainthread
    def on_create(self):
        tab_dict = {}
        for each_tab_dict in self.component_tab_info:
            tab_dict[each_tab_dict["tab_name"]] = each_tab_dict["tab_icon"]

            if (each_tab_dict["tab_type"] == "list" or each_tab_dict["tab_type"] == "basic"):
                # TODO: Tab Withdrawer Initialize but different list view
                instance = TabWithDrawer(tab_name=each_tab_dict["tab_name"],
                                         tab_type=each_tab_dict["tab_type"],
                                         tab_content=each_tab_dict["tab_content"],
                                         toolbar=each_tab_dict["toolbar"])
                self.src_mngr_comp.add_widget(instance)

            elif each_tab_dict["tab_type"] == "null":
                # TODO: Tab Without drawer initialize
                pass
                # initialize the tab widget without drawer

                # instance = TabWithDrawer(tab_name=each_tab_dict["tab_name"],
                #                                      tab_icon=each_tab_dict["tab_icon"],
                #                                      tab_type=each_tab_dict["tab_type"],
                #                                      tab_content=each_tab_dict["tab_content"])
                # self.src_mngr_comp.add_widget(instance)
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