from kivy.clock import mainthread

from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from data.lib import customBuilder as CustomBuilder

# drawer

layout = """
<User_t_General_screen>:
    RelativeLayout:
        id: main_section_id
        # pos_hint: {"right": 1, "y": 0}
        canvas:
            Color:
                rgb: C('#222d32')
            Rectangle:
                pos: self.pos
                size: self.size

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
<User_t_Default_screen>:
    RelativeLayout:
        id: section_scene_manager_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 1, 1
        canvas:
            Color:
                rgb: C('F0FFF1')
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Please Select A tab"
            text_color : C('000000')

"""
CustomBuilder.build_generic_ui(layout)
# test




class User_t_Default_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_Default_screen, self).__init__(**kwargs)
        self.name = "default"
        self.class_id = "Default"
        self.class_icon = "fa-user-o"
        self.order = 0
        self.list_of_sections = {}
        self.tab_type = "basic"
        self.status = "active"

class User_t_General_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_General_screen, self).__init__(**kwargs)
        self.name = "general"
        self.class_id = "General"
        self.class_icon = "fa-user"
        self.order = 1
        self.list_of_tabs = {}
        self.section_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))

        self.status = "active"
        self.has_drawer = True
        self.drawer_type = "list_btn"
        # CustomBuilder.on_create(create_for="section", has_drawer=self.has_drawer, section_attach_to_id=self.ids.main_section_id)



    # @mainthread
    # def on_create(self):
    #     # navigationdrawer = NavigationDrawer()
    #     CustomBuilder.create_section_screen(self.dir, self.list_of_sections, self.section_screen_manager, self.ids.section_scene_manager_id, self.class_id)
    #
    #     def callback(instance):
    #         print(instance.id)
    #         self.section_screen_manager.current = instance.id
    #     def expander_pressed(instance):
    #         if (instance.state == "normal"):
    #             instance.text = "%s" % (icon("fa-chevron-right", 25))
    #             self.ids.section_buttons_id.pos_hint = {"x": -0.25, "top": 1}
    #             self.ids.section_scene_manager_id.size_hint = (1, 1)
    #
    #         elif (instance.state == "down"):
    #             instance.text = "%s" % (icon("fa-chevron-left", 25))
    #             self.ids.section_buttons_id.pos_hint = {"x": 0, "top": 1}
    #             self.ids.section_scene_manager_id.size_hint = (0.75, 1)
    #     # Build Screen
    #     # section_buttons_id
    #     self.section_collection = []
    #     position_y = 1
    #     for i, j in self.list_of_sections.items():
    #         self.btn = ToggleButton(id=i.lower(),
    #                                 markup=True,
    #                                 state="normal",
    #                                 # background_color=(0.133, 0.133, 0.133, 1.0),
    #                                 font_size=10,
    #                                 halign="left",
    #                                 text="%s" % (icon(j, 18)) + "  " + i,
    #                                 size_hint= (1, 0.09),
    #                                 pos_hint= {"x": 0, "top": position_y},
    #                                 group="section")
    #         self.btn.allow_no_selection = False
    #         self.btn.halign = "left"
    #         self.btn.bind(on_press=partial(callback))
    #         self.ids.section_buttons_id.add_widget(self.btn)
    #         position_y -= 0.09
    #         self.section_collection.append(self.btn)
    #     self.expander = ToggleButton(id="expander",
    #                                  markup=True,
    #                                  state="normal",
    #                                  halign="center",
    #                                  text="%s" % (icon("fa-chevron-right", 22)),
    #                                  size_hint=(0.25, 0.07),
    #                                  pos_hint={"x": 0.99, "top": 1})
    #     self.expander.bind(on_press=partial(expander_pressed))
    #     self.ids.section_buttons_id.add_widget(self.expander)


class User_t_Accounts_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_Accounts_screen, self).__init__(**kwargs)
        self.name = "accounts"
        self.class_id = "Accounts"
        self.class_icon = "fa-key"
        self.order = 2
        self.list_of_sections = {}
        self.section_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))

        self.status = "active"
        self.has_drawer = False
        self.drawer_type = "list_btn"
        CustomBuilder.on_create(create_for="section", has_drawer=self.has_drawer)
    # @mainthread
    # def on_create(self):
    #     CustomBuilder.create_section_screen(self.dir, self.list_of_sections, self.section_screen_manager,
    #                                         self.ids.section_scene_manager_id, self.class_id)
    #
    #     def callback(instance):
    #         print(instance.id)
    #         self.section_screen_manager.current = instance.id
    #
    #     def expander_pressed(instance):
    #         if (instance.state == "normal"):
    #             instance.text = "%s" % (icon("fa-chevron-right", 25))
    #             self.ids.section_buttons_id.pos_hint = {"x": -0.25, "top": 1}
    #             self.ids.section_scene_manager_id.size_hint = (1, 1)
    #
    #         elif (instance.state == "down"):
    #             instance.text = "%s" % (icon("fa-chevron-left", 25))
    #             self.ids.section_buttons_id.pos_hint = {"x": 0, "top": 1}
    #             self.ids.section_scene_manager_id.size_hint = (0.75, 1)
    #
    #     # Build Screen
    #     # section_buttons_id
    #     self.section_collection = []
    #     position_y = 1
    #     for i, j in self.list_of_sections.items():
    #         self.btn = ToggleButton(id=i.lower(),
    #                                 markup=True,
    #                                 state="normal",
    #                                 # background_color=(0.133, 0.133, 0.133, 1.0),
    #                                 font_size=10,
    #                                 halign="left",
    #                                 text="%s" % (icon(j, 18)) + "  " + i,
    #                                 size_hint=(1, 0.09),
    #                                 pos_hint={"x": 0, "top": position_y},
    #                                 group="section")
    #         self.btn.allow_no_selection = False
    #         self.btn.halign = "left"
    #         self.btn.bind(on_press=partial(callback))
    #         self.ids.section_buttons_id.add_widget(self.btn)
    #         position_y -= 0.09
    #         self.section_collection.append(self.btn)
    #     self.expander = ToggleButton(id="expander",
    #                                  markup=True,
    #                                  state="normal",
    #                                  halign="center",
    #                                  text="%s" % (icon("fa-chevron-right", 22)),
    #                                  size_hint=(0.25, 0.07),
    #                                  pos_hint={"x": 0.99, "top": 1})
    #     self.expander.bind(on_press=partial(expander_pressed))
    #     self.ids.section_buttons_id.add_widget(self.expander)

class User_t_Settings_screen(Screen):
    def __init__(self, dir, **kwargs):
        super(User_t_Settings_screen, self).__init__(**kwargs)
        self.name = "settings"
        self.class_id = "Settings"
        self.class_icon = "fa-gear"
        self.order = 3
        self.status = "active"











# Generate JSON about Tabs
