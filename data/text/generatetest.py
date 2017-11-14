import os
import textwrap

_filepath = os.getcwd()
_Component_name = "ScrappingComponent"
_id_name = '"scrapping"'
_Icon = '"fa-home"'
_Status = '"active"'
_Order = 1
_List_of_tabs = '{}'
_Tab_group_name = '"scrapping_tabs"'
_layout = '""'


temp_path = _filepath + "\\{component_name}\\".format(component_name=_Component_name)


_Component = temp_path + "{component_name}Base.py".format(component_name=_Component_name)
_Component_tabs = temp_path + "{component_name}Tabs.py".format(component_name = _Component_name)
_Component_section = temp_path + "{component_name}Sections.py".format(component_name = _Component_name)
# _Component_details = temp_path + "details.py"
# _Component_drivers = temp_path + "drivers.py"


def MakeComponent():
    with open(_Component, 'w') as f:
        f.write(textwrap.dedent('''\
            from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
            from data.lib import customBuilder as CustomBuilder

            layout = {layout}
            CustomBuilder.build_generic_ui(layout)

            class {component_name}(Screen):
                def __init__(self, dir, **kwargs):
                    super({component_name}, self).__init__(**kwargs)
                    self.name = {name}
                    self.class_id = {id}
                    self.class_icon = {icon}
                    self.status = {status}
                    self.component_screen_manager = ScreenManager(transition=SlideTransition(direction="left"))
                    self.order = {order}
                    self.dir = dir
                    self.list_of_tabs = {list_of_tabs}
                    self.tab_collections = []
                    self.tab_group_name = {tab_group_name}
                    CustomBuilder.on_create(create_for="tab",
                                            dir=self.dir,
                                            scene_manager=self.component_screen_manager,
                                            scene_manager_attach_to_id=self.ids.component_screen_manager_id,
                                            internal_list=self.list_of_tabs,
                                            tab_btn_attach_to_id=self.ids.tab_panel_id,
                                            class_id=self.class_id,
                                            tab_btn_collections=self.tab_collections,
                                            tab_group_name=self.tab_group_name)
                '''.format(layout =_layout,
                           component_name = _Component_name,
                           name = _id_name.lower(),
                           id = _id_name.capitalize(),
                           icon =_Icon,
                           status = _Status,
                           order = _Order,
                           list_of_tabs = _List_of_tabs,
                           tab_group_name = _Tab_group_name)))
    # print(file_name+' Execution completed.')

def MakeComponentTabs():

    with open(_Component_tabs, 'w') as f:
        f.write(textwrap.dedent('''\
                from kivy.uix.screenmanager import ScreenManager, SlideTransition, Screen
                    '''))

def MakeTabSections():
    with open(_Component_section, 'w') as f:
        f.write(textwrap.dedent('''\
                from kivy.clock import mainthread
                    '''))

def BuildComponent():
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    MakeComponent()
    # MakeComponentTabs()
    # MakeTabSections()

BuildComponent()