from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.togglebutton import ToggleButton


def ScreenBuilder(RootWidget, ClassList):
    tab_screen_manager = ScreenManager(transition=SlideTransition())
    for Klass in ClassList:
        temp_class = Klass()
        temp_class.on_create()
        tab_screen_manager.add_widget(temp_class)
    # adding to main kv panel by id
    RootWidget.ids.tab_screen_content_id.add_widget(tab_screen_manager)


def TabBuilder(RootWidget, TabDict):
    def callback(value):
        pass

    tab_collection = []
    position_y = 1
    for name, icon_name in TabDict.items():
        btn = ToggleButton(id=name,
                           markup=True,
                           state="normal",
                           # background_color=(0.133, 0.133, 0.133, 1.0),
                           font_size=10,
                           halign="center",
                           text="%s\n%s" % ((icon(icon_name, 18)), name),
                           size_hint=(1, 0.09),
                           pos_hint={"x": 0, "top": position_y},
                           group="tab",
                           on_press=callback)
        btn.allow_no_selection = False
        # add to kv language by id
        RootWidget.ids.plugins_sidebar_id.add_widget(btn)
        position_y -= 0.09
        tab_collection.append(btn)
