from functools import partial

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerToolbar
from kivymd.toolbar import Toolbar

from kivy.uix.tabbedpanel import TabbedPanel

layout_base = """
NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Navigation Drawer"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Accordion"
            on_release: app.root.ids.scr_mngr.current = 'accordion'
    # BoxLayout:
    #     orientation: 'vertical'
    #     Toolbar:
    #         id: toolbar
    #         title: 'KivyMD Kitchen Sink'
    #         md_bg_color: app.theme_cls.primary_color
    #         background_palette: 'Primary'
    #         background_hue: '500'
    #         left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
    #         right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
    #     ScreenManager:
    #         id: scr_mngr
    #         Screen:
    #             name: 'bottomsheet'


    # #     #BoxLayout:
    # #     #     orientation: 'vertical'
    #     TitleToolbar:
    #         id: toolbar
    #         pos_hint: {"x": 0, "top": 1}
    #
    #         size_hint_y: 0.05
    #         # title: 'KivyMD Kitchen Sink'
    #         md_bg_color: app.theme_cls.primary_color
    #         background_palette: 'Primary'
    #         background_hue: '500'
    # #         left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
    #         right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
"""

test = """
<DrawerLayout>:
        # add items dynamically
    NavigationDrawerToolbar:
        title: "Navigation Drawer"
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Accordion"
        on_release: app.root.ids.scr_mngr.current = 'accordion'
    # BoxLayout:
    #     orientation: 'vertical'
    #     Toolbar:
    #         id: toolbar


<ViewDrawer>:
    NavigationDrawerToolbar:
        title: "Navigation Drawer 2"
        # color: C("#222222")

    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Accordion"
        on_release: app.root.ids.scr_mngr.current = 'accordion'
    # size_hint: 1, 1
    # NavigationDrawerToolbar:
    #     title: "Navigation Drawer"
    # GridLayout:
    #     pos_hint_y: "bottom"
    #     size_hint: 1, 1
    #     # pos_hint: {'center_x': .5, 'center_y': .5}
    #     rows:1
    # canvas.before:
    #     Color:
    #         rgba: 0, 1, 0, 1
    #     BorderImage: # BorderImage behaves like the CSS BorderImage
    #         border: 10, 10, 10, 10
    #         pos: self.pos
    #         size: self.size


    # Label:
    #     text: "I don't suffer from insanity, I enjoy every minute of it"
    #     text_size: self.width-20, self.height-20
    #     valign: "top"
    #     color: C("#222222")

    # Label:
    #     text: "When I was born I was so surprised; I didn't speak for a year, →and a half."
    #     text_size: self.width-20, self.height-20
    #     valign: 'middle'
    #     halign: 'center'
    # Label:
    #     text: "A consultant is someone who takes a subject you understand and, →makes it sound confusing"
    #     text_size: self.width-20, self.height-20
    #     valign: 'bottom'
    #     halign: 'justify'
    # BoxLayout:
    #     orientation: "vertical"
    #     # an icon label
    #     Button:
    #         text: "LL"
    #     # name of the component
    #     Button:
    #         text: "KK"
    #     # a little description
    #     Label:
    #         text: "I don't suffer from insanity, I enjoy every minute of it"
    #         text_size: self.width-20, self.height-20
    #         valign: 'top'
    #         text_color: [0,0,0,1]

"""

toolbar = """
<TitleToolbar>:
    pos_hint: {"x": 0, "top": 1}
    size_hint_y: 0.05
    title: 'KivyMD Kitchen Sink'
    md_bg_color: app.theme_cls.primary_color
    background_palette: 'Primary'
    background_hue: '500'
"""

component_widget_screen = """
#:import C kivy.utils.get_color_from_hex
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
tab_widget_screen = """
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
Builder.load_string(component_widget_screen + tab_widget_screen)

class TitleToolbar(Toolbar):
    pass

class DrawerLayout(MDNavigationDrawer):
    pass
    # def __init__(self, **kwargs):
    #     CustomBuilder.build_generic_ui(layout_base)
    #     super(DrawerLayout, self).__init__(**kwargs)

class ViewDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(ViewDrawer, self).__init__()
        self.toolbar = DrawerToolbar(drawer_name=kwargs.get("drawer_name"))
        self.add_widget(self.toolbar)
    pass

class DrawerToolbar(NavigationDrawerToolbar):
    def __init__(self, **kwargs):
        super(DrawerToolbar, self).__init__()
        self.title = kwargs.get("drawer_name")
        self.elevation = 1


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

    def build_component_ui(self):
        tab_dict = {}

        # initialize tab class widget and add to sc manger
        for each_tab_dict in self.component_tab_info:
            tab_dict[each_tab_dict["tab_name"]] = each_tab_dict["tab_icon"]

            instance = Generic_tab_widget_screen(tab_name=each_tab_dict["tab_name"],
                                                 tab_id=each_tab_dict["tab_id"],
                                                 tab_icon=each_tab_dict["tab_icon"],
                                                 tab_type=each_tab_dict["tab_type"])
            instance.build_tab_ui()
            self.src_mngr_comp.add_widget(instance)
        self.ids.src_mngr_comp_id.add_widget(self.src_mngr_comp)

        def callback(instance):
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
        self.tab_id = kwargs.get("tab_id")
        self.tab_icon = kwargs.get("tab_icon")
        self.tab_type = kwargs.get("tab_type")
    def build_tab_ui(self):
        # create the navigation drawer according to type
        if (self.tab_type == "basic"):
            instance = ViewDrawer(drawer_name=self.name)
            self.ids.nav_drawer.add_widget(instance)
        # add screen based on tab type and assign to ids
        pass