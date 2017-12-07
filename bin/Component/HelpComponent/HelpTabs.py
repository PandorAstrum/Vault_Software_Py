from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from data.lib import customBuilder as CustomBuilder

layout = """
<Help_t_Basic_screen>:
    RelativeLayout:
        id: section_scene_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 1, 1
        canvas:
            Color:
                rgb: C('D0B265')
            Rectangle:
                pos: self.pos
                size: self.size
        # Button:
        #     text: "LLLLL"

    # FloatLayout:
    #     id: section_buttons_id
    #     pos_hint: {"x": -0.25, "y": 0}
    #     size_hint: 0.25, 1
    #     canvas:
    #         Color:
    #             rgb: C('5247CC')
    #         Rectangle:
    #             pos: self.pos
    #             size: self.size
    # FloatLayout:
    #     pos_hint: {"x": 0, "top": 1}
    #     size_hint: 0.05, 1
    #     canvas:
    #         Color:
    #             rgb: C('#000000')
    #         Rectangle:
    #             pos: self.pos
    #             size: self.size
#       Section
#     Button:
#         text: "Okay"
        # FloatLayout:
        #     id: plugins_section_panel_id
        #     pos_hint: {"left": 1, "top": 1}
        #     size_hint: 0.25, 1
        #     canvas:
        #         Color:
        #             rgb: C('5247CC')
        #         Rectangle:
        #             pos: self.pos
        #             size: self.size
#        Content
#         RelativeLayout:
#             id: plugins_manager_section_main_id
#             pos_hint: {"right": 1, "bottom": 1}
#             size_hint: 0.75, 1
#             canvas:
#                 Color:
#                     rgb: C('D15767')
#                 Rectangle:
#                     pos: self.pos
#                     size: self.size
#            Button:
#                text:"LL"


<Help_t_Custom_screen>:
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

<Help_t_Mechine_screen>:
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
CustomBuilder.build_generic_ui(layout)
# test



class Help_t_Basic_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(Help_t_Basic_screen, self).__init__(**kwargs)
        self.name = "basic"
        self.class_id = "Basic"
        self.class_icon = "fa-facebook"
        self.order = 1
        self.list_of_tabs = {}
        self.section_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
        self.tab_type = "list_of_buttons"
        self.status = "active"


class Help_t_Custom_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(Help_t_Custom_screen, self).__init__(**kwargs)
        self.name = "custom"
        self.class_id = "Custom"
        self.class_icon = "fa-twitter"
        self.order = 2
        self.list_of_sections = {}
        self.section_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
        self.tab_type = "basic"
        self.status = "active"

class Help_t_Mechine_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(Help_t_Mechine_screen, self).__init__(**kwargs)
        self.name = "mechine"
        self.class_id = "Mechine"
        self.class_icon = "fa-youtube"
        self.order = 3
        self.status = "active"










# Generate JSON about Tabs
