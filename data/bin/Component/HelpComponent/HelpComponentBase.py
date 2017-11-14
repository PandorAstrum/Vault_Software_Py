from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from data.lib import customBuilder as CustomBuilder
layout = """
<HelpComponentBase>:
    RelativeLayout:
        id: component_screen_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 0.95, 1

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

CustomBuilder.build_generic_ui(layout)
class HelpComponentBase(Screen):
    def __init__(self, dir, **kwargs):
        super(HelpComponentBase, self).__init__(**kwargs)
        self.name = "Help"
        self.class_id = "Help"
        self.class_icon = "fa-question"
        self.status = "active"
        self.component_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
        self.order = 2
        self.dir = dir
        self.list_of_tabs = {}
        self.tab_collections = []
        self.tab_group_name = "help_tab"
        CustomBuilder.on_create( create_for="tab",
                                 dir=self.dir,
                                 scene_manager=self.component_screen_manager,
                                 scene_manager_attach_to_id=self.ids.component_screen_manager_id,
                                 internal_list=self.list_of_tabs,
                                 tab_btn_attach_to_id=self.ids.tab_panel_id,
                                 class_id=self.class_id,
                                 tab_btn_collections=self.tab_collections,
                                 tab_group_name=self.tab_group_name)
