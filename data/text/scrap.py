
class PluginsScreen(Screen):
    @mainthread
    def on_create(self):

        self.tab_collection = []
        position_y = 1
        for i, j in NUMBER_OF_TABS.items():
            self.pushbtn = ToggleButton(id=i.lower(),
                                        markup=True,
                                        state="normal",
                                        # background_color=(0.133, 0.133, 0.133, 1.0),
                                        font_size=10,
                                        halign="center",
                                        text="%s\n%s" % ((icon(j, 18)),i),
                                        size_hint=(1, 0.09),
                                        pos_hint={"x": 0, "top": position_y},
                                        group="tabs",
                                        on_press=self.callback
                                        )
            self.pushbtn.allow_no_selection = False
            self.ids.screen_sidebar_id.add_widget(self.pushbtn)
            position_y -= 0.09
            self.tab_collection.append(self.pushbtn)

        # Create another screen manager and add 2nd
        # self.tab_screen_manager = ScreenManager(transition=SlideTransition())
        # #
        # #
        # self.plugins_t_manager = Plugin_tab_Screen(name='manager')
        # #
        # self.tab_screen_manager.add_widget(self.plugins_t_manager)
        # #
        # self.ids.screen_sidebar_id.add_widget(self.tab_screen_manager)


    def callback(self, value):
        for i in self.tab_collection:
            if (i.id == value.id):

                i.size_hint = (1.3, 0.09)
            else:
                i.size_hint = (1, 0.09)


# <editor-fold desc=" <Component>Plugin <Tab>Section Class "> --------
# class Plugin_t_Manager_s_General_screen(Screen):
#     pass
#
# class Plugin_t_Manager_s_Ui_screen(Screen):
#     pass
#
# class Plugin_t_Manager_s_Function_screen(Screen):
#     pass
# </editor-fold> ------------------------------------------------------

# <editor-fold desc=" <Component>Plugin Tab Class "> ------------------
# class PluginTABManagerScreen(Screen):
#
#     @mainthread
#     def on_create(self):
#
#
#         # <editor-fold desc=" Section Build "> ------------------------
#         self.section_collection = []
#         position_y = 1
#         for i, j in NUMBER_OF_SECTION.items():
#             self.pushbtn = ToggleButton(id=i.lower(),
#                                         markup=True,
#                                         state="normal",
#                                         # background_color=(0.133, 0.133, 0.133, 1.0),
#                                         font_size=10,
#                                         halign="center",
#                                         text="%s" % (icon(j, 18)) + "  " + i,
#                                         size_hint= (1, 0.09),
#                                         pos_hint= {"x": 0, "top": position_y},
#                                         group="section",
#                                         on_press=self.callback
#                                         )
#             self.pushbtn.allow_no_selection = False
#             self.ids.plugins_manager_section_panel_id.add_widget(self.pushbtn, index=2)
#             position_y -= 0.09
#             self.section_collection.append(self.pushbtn)
#
#         # </editor-fold> ----------------------------------------------
#
#
#
#
#         self.expander = ToggleButton(id="expander",
#                                          markup=True,
#                                          state="normal",
#                                          halign="center",
#                                          text="%s" % (icon("fa-chevron-right", 22)),
#                                          size_hint=(0.25, 0.07),
#                                          pos_hint={"x": 0.99, "top": 1},
#                                          on_press=self.expander_pressed
#                                          )
#         self.ids.plugins_manager_section_panel_id.add_widget(self.expander, index=1)
#         # <editor-fold desc=" Screen build <Section> "> ---------------
#         self.section_screen_manager = ScreenManager(transition=SlideTransition())
#         self.section_general = Plugin_t_Manager_s_General_screen(name='general')
#         self.section_screen_manager.add_widget(self.section_general)
#
#         self.section_screen_manager.add_widget(Plugin_t_Manager_s_Ui_screen(name='ui'))
#         self.section_screen_manager.add_widget(Plugin_t_Manager_s_Function_screen(name='function'))
#         self.ids.plugins_manager_section_main_id.add_widget(self.section_screen_manager)
#         # </editor-fold> ----------------------------------------------
#     def expander_pressed(self, value):
#         print(value.id)
#         # check if the state is down or normal
#         # change the text icon
#         if (value.state == "normal"):
#             value.text = "%s" % (icon("fa-chevron-right", 25))
#
#             self.ids.plugins_manager_section_panel_id.pos_hint = {"x": -0.25, "top": 1}
#         elif (value.state == "down"):
#             value.text = "%s" % (icon("fa-chevron-left", 25))
#             self.ids.plugins_manager_section_panel_id.pos_hint = {"x": 0, "top": 1}
#             # get the section panel and offset it
#
#     def callback(self, value):
#         self.section_screen_manager.current = value.id
#         self.section_screen_manager.transition.direction = 'left'