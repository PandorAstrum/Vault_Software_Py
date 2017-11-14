from kivy.clock import mainthread
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from data.lib import customBuilder as CustomBuilder
layout = """
<User_t_General_s_Ui_screen>
    FloatLayout:
        canvas:
            Color:
                rgb: C('#000000')
            Rectangle:
                pos: self.pos
                size: self.size


<User_t_General_s_Functions_screen>
    FloatLayout:
        canvas:
            Color:
                rgb: C('#FFFFFF')
            Rectangle:
                pos: self.pos
                size: self.size

<User_t_Help_s_Guides_screen>
    FloatLayout:
        canvas:
            Color:
                rgb: C('#E86198')
            Rectangle:
                pos: self.pos
                size: self.size

<User_t_Help_s_Test_screen>
    FloatLayout:
        canvas:
            Color:
                rgb: C('#8AD8B6')
            Rectangle:
                pos: self.pos
                size: self.size

<User_t_General_s_Main_screen>
    FloatLayout:
        canvas:
            Color:
                rgb: C('#846DD1')
            Rectangle:
                pos: self.pos
                size: self.size
"""
CustomBuilder.build_generic_ui(layout)

class User_t_General_s_Main_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_General_s_Main_screen, self).__init__(**kwargs)
        self.name = "main"
        self.class_id = "Main"
        self.class_icon = "fa-home"
        self.dir = dir

    @mainthread
    def on_create(self):
        # Build Screen
        self.section_screen_manager = ScreenManager(transition=SlideTransition())

class User_t_General_s_Ui_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_General_s_Ui_screen, self).__init__(**kwargs)
        self.name = "ui"
        self.class_id = "Ui"
        self.class_icon = "fa-home"
        self.dir = dir

    @mainthread
    def on_create(self):
        # Build Screen
        self.section_screen_manager = ScreenManager(transition=SlideTransition())
# class User_t_General_s_Functions_screen(Screen):
#     def __init__(self, dir, **kwargs):
#         super(User_t_General_s_Functions_screen, self).__init__(**kwargs)
#         self.name = "functions"
#         self.class_id = "Functions"
#         self.class_icon = "fa-home"
#         self.dir = dir
#
#     @mainthread
#     def on_create(self):
#         # Build Screen
#         self.section_screen_manager = ScreenManager(transition=SlideTransition())

class User_t_Help_s_Guides_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_Help_s_Guides_screen, self).__init__(**kwargs)
        self.name = "help"
        self.class_id = "Help"
        self.class_icon = "fa-question"
        self.dir = dir

    @mainthread
    def on_create(self):
        pass

class User_t_Help_s_Test_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_Help_s_Test_screen, self).__init__(**kwargs)
        self.name = "test"
        self.class_id = "Test"
        self.class_icon = "fa-camera"
        self.dir = dir

    @mainthread
    def on_create(self):
        pass









# Generate JSON about Tabs
