# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Core Screen Models"
"""
import time
from functools import partial

from kivy.app import App
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.resources import resource_find
from kivy.uix.actionbar import ActionToggleButton
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar



import utils
from utils.iconfonts import icon
from utils.jsonUtility import dump_json, get_json_file
from utils import appDirs
from bin import appSettings
from Core.KVFiles import *

from bin.libPackage.notification import Notification


class MainScreen(Screen):
    """
    Main Screen where everything will load ... attach to Launchpad
    """
    def __init__(self, login_name, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = "mainScreen"
        self.app_icon = "res\\logo.png"
        self.login_name = login_name
        self.json_default_dictionary = {}
        self.data = None
        self.app = App.get_running_app()
        self.user_dir = appDirs.user_config_dir(appname=appSettings.APP_NAME,
                                           appauthor=appSettings.APP_AUTHOR)
        self.component_conf_dir = self.user_dir+f"\\{appSettings.FOLDER_CONFIG}"
        appDirs.check_make_dir(self.component_conf_dir)
        self.se_component_dir = self.user_dir+f"\\{appSettings.FOLDER_SECONDARY_COMPONENT}"
        appDirs.check_make_dir(self.se_component_dir)

        self.src_mngr = ScreenManager(transition=SwapTransition())
        self._snackbar("simple", f"Logged in as {self.login_name}")
        self._make()

    @staticmethod
    def _snackbar(snack_type, msg):
        """
        Creating Snackbar type
        :param snack_type: str Type
        :param msg: str message
        :return:
        """
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def _make(self):
        """
        Default build function for Main Screen
        :return:
        """
        # get all component
        primary_component_entry = self.app.config.get("Component",
                                                 "PrimaryComponentEntry")
        secondary_component_entry = self.app.config.get("Component",
                                                 "SecondaryComponentEntry")

        for ch in ["(", ")", "'", " "]:
            if ch in primary_component_entry:
                primary_component_entry = primary_component_entry.replace(ch, "")
            if utils.is_empty(secondary_component_entry):
                pass
            else:
                if ch in secondary_component_entry:
                    secondary_component_entry = secondary_component_entry.replace(ch, "")

        primary_component_entry = primary_component_entry.split(",")
        if utils.is_empty(secondary_component_entry):
            pass
        else:
            secondary_component_entry = secondary_component_entry.split(",")
        # get json file
        if utils.is_empty(secondary_component_entry):
            for i in primary_component_entry:
                component_json = self._build_json_default(i)
                self.json_default_dictionary[f"{i}Component"] = component_json
        else:
            for i in [*primary_component_entry, *secondary_component_entry]:
                component_json = self._build_json_default(i)
                self.json_default_dictionary[f"{i}Component"] = component_json

        try:
            self.data = get_json_file(appSettings.FILE_CONFIG_COMPONENT,
                                      self.component_conf_dir)
        except FileNotFoundError:
            dump_json(self.json_default_dictionary,
                      appSettings.FILE_CONFIG_COMPONENT,
                      self.component_conf_dir)
        finally:
            self.data = get_json_file(appSettings.FILE_CONFIG_COMPONENT,
                                      self.component_conf_dir)

        component_dict = {}
        temp_dict_ordered = {}

        # Component class initialization
        for each_component_name, each_component_fields in self.data.items():
            if each_component_fields["status"]:
                instance = self._init_component(component_name=each_component_fields["component_name"],
                                               name=each_component_fields["id"],
                                               component_id=each_component_fields["id"],
                                               component_icon=each_component_fields["icon"],
                                               component_tab_info=each_component_fields["tab"],
                                               tab_group_name=each_component_fields["tab_group_name"])

                component_dict[each_component_fields["order"]] = instance

        for key in sorted(component_dict, reverse=True):  # Sorting
            temp_dict_ordered[key] = component_dict[key]

        def spinner_callback(instance):  # spinner button callback
            self.ids.act_spinner_id.text = instance.text
            self.src_mngr.current = instance.id

        for key in temp_dict_ordered:  # Spinner button
            if key != 0:
                ac_drpdwn_btn = ActionToggleButton(id=temp_dict_ordered[key].component_id,
                                                   markup=True,
                                                   text="%s" % (icon(temp_dict_ordered[key].component_icon, 20)) + "  " + temp_dict_ordered[key].component_id,
                                                   group="component_toggle")
                ac_drpdwn_btn.allow_no_selection = False
                ac_drpdwn_btn.bind(on_press=partial(spinner_callback))
                self.ids.act_spinner_id.add_widget(ac_drpdwn_btn)

        # default behaviour
        default = DefaultScreen()
        self.src_mngr.add_widget(default)
        for key in temp_dict_ordered:  # adding screen widget to screen manager (by order)
            self.src_mngr.add_widget(temp_dict_ordered[key])

        self.ids.src_mngr_level_2_id.add_widget(self.src_mngr)

    def _build_json_default(self, component_name):
        """
        Build json per component
        :param component_name: str (Component name)
        :return:
        """
        if component_name.endswith("_PR"):
            component_class = f"bin.Component.{component_name}Component.Component"
            module = utils.module_import_simple(component_class)
            return module.json_settings
        else:
            full_path = f"{self.se_component_dir}\\{component_name}Component\\"
            module = utils.module_import_from_abs(full_path, "*Component.py")
            return module.json_settings

    def _init_component(self, **kwargs):
        """
        docString
        :param kwargs: all parameter
        :return:
        """
        component_name = kwargs.get("component_name")
        if component_name.endswith("_PRComponent"):
            component_class = f"bin.Component.{component_name}.Component"
            module = utils.module_import_simple(component_class)
            return module.Component(component_name=kwargs.get("name"),
                                component_id=kwargs.get("component_id"),
                                component_icon=kwargs.get("component_icon"),
                                component_tab_info=kwargs.get("component_tab_info"),
                                tab_group_name=kwargs.get("tab_group_name"))
        else:
            full_path = f"{self.se_component_dir}\\{component_name}\\"
            module = utils.module_import_from_abs(full_path, "*Component.py")
            return module.Component(component_name=kwargs.get("name"),
                                component_id=kwargs.get("component_id"),
                                component_icon=kwargs.get("component_icon"),
                                component_tab_info=kwargs.get("component_tab_info"),
                                tab_group_name=kwargs.get("tab_group_name"))

class DefaultScreen(Screen):
    """
    Default screen to show blank
    """
    #TODO: need a good design to kv files
    pass


class ErrorScreen(Screen):
    """
    Error Screen ... attach to Launchpad
    """
    def __init__(self, err, **kwargs):
        super(ErrorScreen, self).__init__(**kwargs)
        self.name = "errorScreen"
        self.ids.error_msg_id.text = err

    def try_again(self):
        """
        Button callback
        :return:
        """
        login_screen = LoginScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(login_screen)
        self.manager.current = "loginScreen"


class RegistrationScreen(Screen):
    """
    Registration screen ... attach to Launchpad
    """
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
        self.name = "registrationScreen"

    def register_new(self):
        """
        Creates a new user for the app
        :return:
        """
        #TODO: implement registration system
        pass

    def back_to_login(self):
        """
        Cancel button callback
        :return:
        """
        login_screen = LoginScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(login_screen)
        self.manager.current = "loginScreen"


class LoginScreen(Screen):
    """
    Login Screen ... attach to Launchpad
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = "loginScreen"
        self.working = False

    @staticmethod
    def _snackbar(snack_type, msg):
        """
        Creating snack bar type
        :param snack_type: str type
        :param msg: str message
        :return:
        """
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def login(self):
        """
        login button callback
        :return:
        """
        username = self.ids.username.text
        password = self.ids.passwd.text
        if not username:
            self._snackbar("simple", "Username is empty")
        elif not password:
            self._snackbar("simple", "Password is empty")
        else:
            if self.ids.offline_chkbox_id.active:
                self._offline_login()
            else:
                self._online_login()

    def _online_login(self):
        """
        Try online login mechanism
        :return:
        """
        try:
            # all button disable while working
            # go to google sheet and try to match with username and pass
            utils.check_internet()
        except ConnectionError:
            self._snackbar("simple", "No internet")
        finally:
            # if match then self manager add widget main screen
            # if not then self manager add widget wrong password
            pass

    def _offline_login(self):
        """
        Try offline login mechanism
        :return:
        """
        app = App.get_running_app()
        if self.ids.username.text != app.config.get('User', 'Username'):
            self._switch_screen(error=True, error_message="Username is Incorrect")
        elif self.ids.passwd.text != app.config.get('User', 'Password'):
            self._switch_screen(error=True, error_message="Password is Incorrect")
        else:
            self._switch_screen(app=app)

    def _switch_screen(self, error=False, error_message=None, app=None):
        """
        Helper function for _offline_login
        :param error: bool if error occurs or not
        :param error_message: str message if error occurs
        :param app: app config if no error
        :return:
        """
        if error:
            error_screen = ErrorScreen(err=error_message)
            self.manager.clear_widgets()
            self.manager.add_widget(error_screen)
            self.manager.current = "errorScreen"
        else:
            main_screen = MainScreen(login_name=app.config.get('User', 'FirstName'))
            self.manager.clear_widgets()
            self.manager.add_widget(main_screen)
            self.manager.current = "mainScreen"

    def new_register(self):
        """
        New user button callback
        :return:
        """
        registration_screen = RegistrationScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(registration_screen)
        self.manager.current = "registrationScreen"

    def forget(self):
        """
        forget password button callback
        :return:
        """
        #TODO: implement the forget mechanism
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="We will email you the password",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Send",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.add_action_button("Cancel",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    # test notification
    def show_notification(self, *args):
        # open default notification
        Notification().open(title='Kivy Notification',
                            message='Hello from the other side?',
                            timeout=10,
                            icon=resource_find('data/logo/kivy-icon-128.png')
                            )


        # open notification with layout in kv
        Notification().open(title='Kivy Notification',
                            message="I'm a Button!",
                            kv="Button:\n    text: app.message"
                            )


class LoadingScreen(Screen):
    """
    Loading Screen ... Attach to Launchpad
    """
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.name = "loadingScreen"
        self.login = LoginScreen()
        self._check()

    @utils.threaded(thread_name="check Thread")
    def _check(self):
        """
        check for internet and builds the UI according to response
        :return:
        """
        time.sleep(0.5)
        self.manager.add_widget(self.login)
        self.manager.current = "loginScreen"

        # internet = utils.check_internet()

        # if internet:
            # self._check_updates()
            # self._auto_login()
            # self.manager.add_widget(self.login)
            # self.manager.current = "loginScreen"
        # else:
        #     self.manager.add_widget(self.login)
        #     self.manager.current = "loginScreen"

    def _auto_login(self):
        """
        Tries to login automatically from web
        :return:
        """
        # TODO: implement the auto login system
        pass

    def _check_updates(self):
        """
        Tries to check for updates
        :return:
        """
        # TODO: implement the upgrade check
        pass


class LaunchPad(ScreenManager):
    """
    First Screen to draw when main is running
    """
    def __init__(self, **kwargs):
        super(LaunchPad, self).__init__(**kwargs)
        self.build_kv()
        self._make()

    @staticmethod
    def build_kv():
        """
         build all the kv files imported from core and components
        :return:
        """
        # get the base kv files
        base_kv = (launchPad_kv,
                   loadingScreen_kv,
                   loginScreen_kv,
                   errorScreen_kv,
                   registration_kv,
                   seperator_kv,
                   mainScreen_kv,
                   componentBase_kv,
                   defaultScreen_kv,
                   tabBase_kv,
                   defaultTab_kv,
                   tabWithoutDrawer_kv,
                   tabWithDrawer_kv,
                   miningField_kv
                   )
        all_kv = """"""
        for i in base_kv:
            all_kv += i

        # get component's kv file
        app = App.get_running_app()
        primary_component_entry = app.config.get("Component", "PrimaryComponentEntry")
        secondary_component_entry = app.config.get("Component", "SecondaryComponentEntry")
        for ch in ["(", ")", "'", " "]:
            if ch in primary_component_entry:
                primary_component_entry = primary_component_entry.replace(ch, "")
            if utils.is_empty(secondary_component_entry):
                pass
            else:
                if ch in secondary_component_entry:
                    secondary_component_entry = secondary_component_entry.replace(ch, "")
        primary_component_entry = primary_component_entry.split(",")
        if utils.is_empty(secondary_component_entry):
            pass
        else:
            secondary_component_entry = secondary_component_entry.split(",")
        if utils.is_empty(secondary_component_entry):
            for component_name in primary_component_entry:
                if component_name.endswith("_PR"):
                    kv_class = f"bin.Component.{component_name}Component.KV"
                    module = utils.module_import_simple(kv_class)
                    all_kv += module.kv
        else:
            for component_name in [*primary_component_entry, *secondary_component_entry]:
                if component_name.endswith("_PR"):
                    kv_class = f"bin.Component.{component_name}Component.KV"
                    module = utils.module_import_simple(kv_class)
                    all_kv += module.kv
                else:
                    user_dir = appDirs.user_config_dir(appname=appSettings.APP_NAME,
                                                   appauthor=appSettings.APP_AUTHOR)
                    se_component_dir = user_dir + f"\\{appSettings.FOLDER_SECONDARY_COMPONENT}"
                    full_path = f"{se_component_dir}\\{component_name}Component\\"
                    module = utils.module_import_from_abs(full_path, "*KV.py")
                    all_kv += module.kv

        Builder.load_string(all_kv)

    @mainthread
    def _make(self):
        """
        Default build for Launching Pad
        :return:
        """
        loading = LoadingScreen()
        self.add_widget(loading)
        self.current = "loadingScreen"

    @staticmethod
    def resize_window(size):
        """
        Call back Functions from KV window resize
        :param size: int height and int width from kv
        :return:
        """
        app = App.get_running_app()
        app.config.set('WindowSettings', 'Width', size[0])
        app.config.set('WindowSettings', 'Height', size[1])
        app.config.write()
