from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from data.lib import customBuilder as CustomBuilder
from data.bin.Component.UserComponent.drivers  import Drivers
layout_base = """
<UserComponentBase>:
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"x": 0, "top": 1}
        Toolbar:
            id: toolbar
            title: 'Vault'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['dots-vertical', lambda x: root.driver.printME()]]
    RelativeLayout:
        id: component_screen_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 0.95, 1
        # canvas:
        #     Color:
        #         rgb: C('#736066')
        #     Rectangle:
        #         pos: self.pos
        #         size: self.size

    # tabs
    FloatLayout:
        id: tab_panel_id
        pos_hint: {"x": 0, "top": 1}
        size_hint: 0.05, 1
        canvas:
            Color:
                rgb: C('#222222')
            Rectangle:
                pos: self.pos
                size: self.size
"""
layout_tabs = """


"""
layout_sections = """
"""
CustomBuilder.build_generic_ui(layout_base+layout_tabs+layout_sections)
class UserComponentBase(Screen):
    def __init__(self, dir, **kwargs):
        super(UserComponentBase, self).__init__(**kwargs)
        self.name = "User"
        self.class_id = "User"
        self.class_icon = "fa-home"
        self.status = "active"
        self.component_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
        self.order = 1
        self.dir = dir
        self.list_of_tabs = {}
        self.tab_collections = []
        self.tab_group_name = "user_tab"
        # CustomBuilder.on_create( create_for="tab",
        #                          dir=self.dir,
        #                          scene_manager=self.component_screen_manager,
        #                          scene_manager_attach_to_id=self.ids.component_screen_manager_id,
        #                          internal_list=self.list_of_tabs,
        #                          tab_btn_attach_to_id=self.ids.tab_panel_id,
        #                          class_id=self.class_id,
        #                          tab_btn_collections=self.tab_collections,
        #                          tab_group_name=self.tab_group_name)
        self.driver = Drivers()
    def toggle_nav_drawer(self):
        print("Working")


class User_t_General_Screen(Screen):
    pass

class User_t_Accounts_Screen(Screen):
    pass

class User_t_Settings_Screen(Screen):
    pass