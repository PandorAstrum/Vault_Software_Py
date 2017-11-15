import importlib.util, fnmatch, os, glob, inspect
from functools import partial

from kivy.clock import mainthread
from kivy.uix.actionbar import ActionToggleButton
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

from data.lib.iconfonts import icon
# from data.lib import navdrawer
from data.lib.essWidget import Generic_component_widget_screen
from data.lib.jsonUtility import dumpJson, getJsonFile, getKeyValue, dumpKeyValue


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

def module_importer(filename, delimiters):
    clsmembers = []
    if fnmatch.fnmatch(filename, delimiters):
        temp_file = str(filename).split("\\")[-1]
        spec = importlib.util.spec_from_file_location(temp_file, filename)
        component_file = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(component_file)

        clsmembers = inspect.getmembers(component_file, inspect.isclass)
        # print(clsmembers)
    return list(clsmembers)




# SECTIONS ==========================================================================
def create_section_screen(dir, add_to_list, section_scene_manager, ids, parents):
    for subDirectoryName in glob.iglob(dir, recursive=True):
        for file in list_files(subDirectoryName):
            section_classes = module_importer(file, '*Sections.py')
            for i in section_classes:
                if fnmatch.fnmatch(i[0], "*_t_"+parents+"_s_*"):
                    instance = i[1](dir)
                    instance.on_create()
                    add_to_list[instance.class_id] = instance.class_icon
                    section_scene_manager.add_widget(instance)

    ids.add_widget(section_scene_manager)



# MAIN SCREEN OR COMPONENT ==========================================================
def create_main(dir, suffix, look_for_file, only_class_match_with, internal_list, scene_manager, scene_manager_attach_to_id):
    final_dir = dir + suffix
    instance_list = {}
    temp_dict_ordered = {}
    for subDirectoryName in glob.iglob(final_dir, recursive=True):
        for file in list_files(subDirectoryName):
            imported_classes = module_importer(file, look_for_file)
            # pass (imported_class, only_class_match_with, send_dir, instance_list)
            class_initializer(imported_classes,only_class_match_with,final_dir, instance_list)

    for key in sorted(instance_list): #Sorting
        temp_dict_ordered[key] = instance_list[key]
        scene_manager.add_widget(instance_list[key])
        internal_list[instance_list[key].class_id] = instance_list[key].class_icon
    scene_manager_attach_to_id.add_widget(scene_manager)

# TABS ==============================================================================
def create_tab(dir, look_for_file, only_class_match_with, internal_list, scene_manager, scene_manager_attach_to_id):
    instance_list = {}
    temp_dict_ordered = {}
    for subDirectoryName in glob.iglob(dir, recursive=True):
        for file in list_files(subDirectoryName):
            tab_classes = module_importer(file, look_for_file)
            class_initializer(tab_classes,only_class_match_with,dir,instance_list)

    for key in sorted(instance_list):  # Sorting
        temp_dict_ordered[key] = instance_list[key]
        scene_manager.add_widget(instance_list[key])
        if instance_list[key].class_id != "Default":
            internal_list[instance_list[key].class_id] = instance_list[key].class_icon
    scene_manager_attach_to_id.add_widget(scene_manager)




def build_generic_ui(layout):
    Builder.load_string(layout)


def class_initializer(**kwargs):
    imported_class = kwargs.get("imported_class")
    only_class_match_with = kwargs.get("only_match_with")
    directory = kwargs.get("directory")
    view_file = kwargs.get("view_file")
    instance_list = kwargs.get("instance_list")
    for i in imported_class:
        if fnmatch.fnmatch(i[0], only_class_match_with):
            instance = i[1](directory=directory, view_file=view_file)
            if (instance.status):
                instance_list[instance.order] = instance

@mainthread
def On_create(**kwargs):
    dir = kwargs.get("dir")
    view_file = kwargs.get("view_file")
    src_mngr = kwargs.get("src_mngr")
    src_mngr_id = kwargs.get("src_mngr_id")
    dict_of_component = kwargs.get("dict_of_component")
    act_spinner_id = kwargs.get("spinner_id")

    instance_list = {}
    temp_dict_ordered = {}
    for subDirectoryName in glob.iglob(dir, recursive=True):
        for file in list_files(subDirectoryName):
            imported_files = module_importer(file, view_file)
            # only initialize the main view
            class_initializer(imported_class=imported_files,
                              only_match_with="*ComponentBase",
                              directory=dir,
                              view_file=view_file,
                              instance_list=instance_list)

    for key in sorted(instance_list):  # Sorting
        temp_dict_ordered[key] = instance_list[key]
        src_mngr.add_widget(instance_list[key])
        dict_of_component[instance_list[key].class_id] = instance_list[key].class_icon
    src_mngr_id.add_widget(src_mngr)

    # create action buttons
    def callback(instance):
        act_spinner_id.text = instance.text
        src_mngr.current = instance.id
        # TODO: mark this scene as current on JSON

    for key, value in dict_of_component.items():
        ac_drpdwn_btn = ActionToggleButton(id=key,
                                           markup=True,
                                           text="%s" % (icon(value, 20)) + "  " + key,
                                           group="component_toggle")
        ac_drpdwn_btn.allow_no_selection = False
        ac_drpdwn_btn.bind(on_press=partial(callback))
        act_spinner_id.add_widget(ac_drpdwn_btn)

@mainthread
def On_create_component(**kwargs):
    dir = kwargs.get("directory")
    view_file = kwargs.get("view_file")
    component_name = kwargs.get("component_name")
    src_mngr = kwargs.get("src_mngr")
    src_mngr_id = kwargs.get("src_mngr_id")
    dict_of_tab = kwargs.get("dict_of_tab")
    tab_collection = kwargs.get("tab_collection")
    group_name = kwargs.get("group_name")
    tab_panel_id = kwargs.get("tab_panel_id")
    instance_list = {}
    temp_dict_ordered = {}
    for subDirectoryName in glob.iglob(dir, recursive=True):
        for file in list_files(subDirectoryName):

            imported_files = module_importer(file, view_file)
    #         # only initialize the tab_screens
            class_initializer(imported_class=imported_files,
                              only_match_with=component_name+"_t_*",
                              directory_send=dir, instance_list=instance_list)
    #
    for key in sorted(instance_list):  # Sorting
        temp_dict_ordered[key] = instance_list[key]
        src_mngr.add_widget(temp_dict_ordered[key])
        if instance_list[key].class_id != "Default":
            dict_of_tab[instance_list[key].class_id] = instance_list[key].class_icon
    src_mngr_id.add_widget(src_mngr)
    #
    # # create tabs
    def callback(instance):
        src_mngr.current = instance.id
        for i in tab_collection:
            if (i.id == instance.id):
                i.size_hint = (1.3, 0.09)
            else:
                i.size_hint = (1, 0.09)

    position_y = 1
    for i, j in dict_of_tab.items():
        btn = ToggleButton(id=i.lower(),
                           markup=True,
                           state="normal",
                           font_size=10,
                           halign="center",
                           text="%s\n%s" % ((icon(j, 18)), i),
                           size_hint=(1, 0.09),
                           pos_hint={"x": 0, "top": position_y},
                           group=group_name)
        btn.allow_no_selection = False
        btn.bind(on_press=partial(callback))
        tab_panel_id.add_widget(btn)
        position_y -= 0.09
        tab_collection.append(btn)

# new-------------------------------------

@mainthread
def on_main_create(**kwargs):
    component_dict = {}
    temp_dict_ordered = {}
    src_mngr = kwargs.get("src_mngr")

    for key, value in USER_SETTINGS_JSON.items():
        if (key == "component"):
            for all_component in value:
                for each_component_name, each_component_fields in all_component.items():
                    if each_component_fields["status"] == True:
                        # initialize with generic class
                        instance = Generic_component_widget_screen(component_name=each_component_fields["id"],
                                                                   component_id=each_component_fields["id"],
                                                                   component_icon=each_component_fields["icon"],
                                                                   component_tab_info=each_component_fields["tab"],
                                                                   tab_group_name=each_component_fields["tab_group_name"])
                        instance.build_component_ui()
                        component_dict[each_component_fields["order"]] = instance

    for key in sorted(component_dict):  # Sorting
        temp_dict_ordered[key] = component_dict[key]

    for key in temp_dict_ordered: # adding screen widget to screen manager (by order)
        src_mngr.add_widget(temp_dict_ordered[key])
    kwargs.get("attach_id").add_widget(src_mngr)

    def callback(instance): # spinner button callback
        kwargs.get("act_spinner_id").text = instance.text
        src_mngr.current = instance.id

    for key in temp_dict_ordered: #Spinner button
        ac_drpdwn_btn = ActionToggleButton(id=temp_dict_ordered[key].component_id,
                                           markup=True,
                                           text="%s" % (icon(temp_dict_ordered[key].component_icon, 20)) + "  " + temp_dict_ordered[key].component_id,
                                           group="component_toggle")
        ac_drpdwn_btn.allow_no_selection = False
        ac_drpdwn_btn.bind(on_press=partial(callback))
        kwargs.get("act_spinner_id").add_widget(ac_drpdwn_btn)

def on_component_create(**kwargs):
    print(kwargs.get("tab_info"))


# test
from data.lib.localStorage import LocalStorage
ls = LocalStorage(debug=True)
# print(ls.dump_dir)
dumpJson(USER_SETTINGS_JSON)
# print(getJsonFile())
# data = getJsonFile()
# dumpKeyValue(data, "window_width", 1200)

# window = jsontest.getkey(data, "settings")
# # size = jsontest.getkey(window, "window_size")
# print(window)