from kivy.clock import mainthread
from kivy.uix.screenmanager import ScreenManager, SlideTransition, Screen
from kivy.uix.togglebutton import ToggleButton
from data.lib.iconfonts import icon
from data.text.builderHelper import ScreenBuilder


class UsersScreen(Screen):
    def __init__(self, **kwargs):
        super(UsersScreen, self).__init__(**kwargs)

    @mainthread
    def on_create(self, RootWidget):
        # BUILD Screen
        ScreenBuilder(RootWidget, tabs.List_OF_CLASSES)

        # Build Tab


    def callback(self, value):
        print('%s pressed.' % value.pos_hint["top"])

        # value.pos_hint= {"x":0.5, "top": value.pos_hint["top"]}


        # self.tab_screen_manager.current = value.id
        # self.tab_screen_manager.transition.direction = 'right'
        #
        # for i in self.tab_collection:
        #     if (i.id == value.id):
        #
        #         i.size_hint = (1.3, 0.09)
        #     else:
        #         i.size_hint = (1, 0.09)
    pass