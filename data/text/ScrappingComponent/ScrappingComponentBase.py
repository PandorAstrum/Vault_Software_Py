from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from data.lib import customBuilder as CustomBuilder

layout = ""
CustomBuilder.build_generic_ui(layout)

class ScrappingComponent(Screen):
    def __init__(self, dir, **kwargs):
        super(ScrappingComponent, self).__init__(**kwargs)
        self.name = "scrapping"
        self.class_id = "scrapping"
        self.class_icon = "fa-home"
        self.status = "active"
        self.component_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
        self.order = 1
        self.dir = dir
        self.list_of_tabs = {}
        self.tab_collections = []
        self.tab_group_name = "scrapping_tabs"
        CustomBuilder.on_create(create_for="tab",
                                dir=self.dir,
                                scene_manager=self.component_screen_manager,
                                scene_manager_attach_to_id=self.ids.component_screen_manager_id,
                                internal_list=self.list_of_tabs,
                                tab_btn_attach_to_id=self.ids.tab_panel_id,
                                class_id=self.class_id,
                                tab_btn_collections=self.tab_collections,
                                tab_group_name=self.tab_group_name)
