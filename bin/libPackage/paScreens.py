# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import os
import importlib
import time
from functools import partial
import subprocess
from threading import Thread

from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.resources import resource_find
from kivy.uix.actionbar import ActionToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, SwapTransition
from kivymd.button import MDRaisedButton
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar
from kivymd.tabs import MDTabbedPanel, MDTab
from kivymd.textfields import MDTextField

from bin.libPackage.iconfonts import icon
from bin.libPackage.jsonUtility import dump_json, get_json_file
from bin.libPackage.notification import Notification
from bin.libPackage.cipherRSA import CipherRSA
from bin.libPackage.localStorage import LocalStorage
from bin.libPackage.googleSheet import GoogleSheet
from bin.libPackage.paUtility import PaUtility, _check_internet
from bin.libPackage.paUtility import threaded
from bin.libPackage.kvFiles import *
from data.testclass.MDToggleButton import MDToggleButton


class MainScreen(Screen):
    def __init__(self, login_name, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = "mainScreen"
        self.app_icon = "res\\logo.png"
        self.login_name = login_name
        self.local_storage = LocalStorage(debug=True)
        self.json_dictionary = {}
        self.data = None
        self.src_mngr = ScreenManager(transition=SwapTransition())
        self._snackbar("simple", f"Logged in as {self.login_name}")
        self._make()

    def _snackbar(self, snack_type, msg):
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def _make(self):
        # get all component
        app = App.get_running_app()
        primary_component_entry = app.config.get("Component", "PrimaryComponentEntry")

        for ch in ["(", ")", "'", " "]:
            if ch in primary_component_entry:
                primary_component_entry = primary_component_entry.replace(ch, "")

        primary_component_entry = primary_component_entry.split(",")
        # get the json file
        try:
            self.data = get_json_file(self.local_storage.storage)
        except FileNotFoundError:
            for i in primary_component_entry:
                component_json = self.build_json_default(i)
                self.json_dictionary[f"{i}_Component"] = component_json
            dump_json(self.json_dictionary, self.local_storage.storage)
        finally:
            self.data = get_json_file(self.local_storage.storage)

        component_dict = {}
        temp_dict_ordered = {}

        for each_component_name, each_component_fields in self.data.items():
            if each_component_fields["status"] == True:
                # initialize generic class
                instance = self.init_component(component_name=each_component_fields["component_name"],
                                               name=each_component_fields["id"],
                                               component_id=each_component_fields["id"],
                                               component_icon=each_component_fields["icon"],
                                               component_tab_info=each_component_fields["tab"],
                                               tab_group_name=each_component_fields["tab_group_name"])

                component_dict[each_component_fields["order"]] = instance

        for key in sorted(component_dict):  # Sorting
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


    def build_json_default(self, component_name):
        """
        docString
        :param component_name: str (Component name)
        :return:
        """
        COMPONENT_CLASS = f"bin.Component.{component_name}Component.Component"
        module = importlib.import_module(COMPONENT_CLASS, ".")
        return module.json_settings

    def init_component(self, **kwargs):
        """
        docString
        :param kwargs: all parameter
        :return:
        """
        component_name = kwargs.get("component_name")
        COMPONENT_CLASS = f"bin.Component.{component_name}.Component"
        module = importlib.import_module(COMPONENT_CLASS, ".")
        return module.Component(component_name=kwargs.get("name"),
                                component_id=kwargs.get("component_id"),
                                component_icon=kwargs.get("component_icon"),
                                component_tab_info=kwargs.get("component_tab_info"),
                                tab_group_name=kwargs.get("tab_group_name"))


class DefaultScreen(Screen):
    pass


class ErrorScreen(Screen):
    """
    DocString
    """
    def __init__(self, err, **kwargs):
        super(ErrorScreen, self).__init__(**kwargs)
        self.name = "errorScreen"
        self.ids.error_msg_id.text = err

    def try_again(self):
        login_screen = LoginScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(login_screen)
        self.manager.current = "loginScreen"


class RegistrationScreen(Screen):
    """
    DocString
    """
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
        self.name = "registrationScreen"

    #TODO: need fix
    def register_new(self):
        print("New User Created")

    def back_to_login(self):
        login_screen = LoginScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(login_screen)
        self.manager.current = "loginScreen"


class LoginScreen(Screen):
    """
    DocString
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = "loginScreen"
        self.working = False

    @staticmethod
    def _snackbar(snack_type, msg):
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def login(self):
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

    def new_register(self):
        registration_screen = RegistrationScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(registration_screen)
        self.manager.current = "registrationScreen"

    def _online_login(self):
        print("Trying Online")
        try:
            # go to google sheet and try to match with username and pass
            _check_internet()
        except ConnectionError:
            self._snackbar("simple", "No internet")
        finally:
            # if match then self manager add widget root widget
            # if not then self manager add widget wrong passowrd
            # self.ids.loginbtn.disabled = True
            pass

    def _offline_login(self):
        app = App.get_running_app()
        if self.ids.username.text != app.config.get('Client', 'Username'):
            error_screen = ErrorScreen(err="Username is Incorrect")
            self.manager.clear_widgets()
            self.manager.add_widget(error_screen)
            self.manager.current = "errorScreen"
        elif self.ids.passwd.text != app.config.get('Client', 'Password'):
            error_screen = ErrorScreen(err="Password is Incorrect")
            self.manager.clear_widgets()
            self.manager.add_widget(error_screen)
            self.manager.current = "errorScreen"
        else:
            main_screen = MainScreen(login_name=app.config.get('Client', 'Username'))
            self.manager.clear_widgets()
            self.manager.add_widget(main_screen)
            self.manager.current = "mainScreen"

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

    # TODO: need fix
    def forget(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          size_hint_y=None,
                          valign='top')
        # content = MDTextField(hint_text="Enter Your Email Address",size_hint_y=None)
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


class LoadingScreen(Screen):
    """
    DocString
    """
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.name = "loadingScreen"
        self.login = LoginScreen()
        self._check()

    @threaded(thread_name="check Thread")
    def _check(self):
        time.sleep(0.5)
        internet = _check_internet()

        if internet:
            self._auto_login()
            self.manager.add_widget(self.login)
            self.manager.current = "loginScreen"
        else:
            self.manager.add_widget(self.login)
            self.manager.current = "loginScreen"

    def _auto_login(self):
        # TODO: implement the auto login system
        pass


class LaunchPad(ScreenManager):
    """
    DocString
    """
    def __init__(self, **kwargs):
        super(LaunchPad, self).__init__(**kwargs)
        self.build_kv()
        self._make()

    def build_kv(self):
        """
         build all the kv files
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
                   tabWithDrawer_kv
        )
        all_kv_list = """"""
        # get base kv files
        for i in base_kv:
            all_kv_list += i

        # get component's kv file
        app = App.get_running_app()
        primary_component_entry = app.config.get("Component", "PrimaryComponentEntry")
        for ch in ["(", ")", "'", " "]:
            if ch in primary_component_entry:
                primary_component_entry = primary_component_entry.replace(ch, "")

        primary_component_entry = primary_component_entry.split(",")

        for i in primary_component_entry:
            component_name = i
            KV_CLASS = f"bin.Component.{component_name}Component.KV"
            module = importlib.import_module(KV_CLASS, ".")

            all_kv_list += module.kv

        Builder.load_string(all_kv_list)

    @mainthread
    def _make(self):
        loading = LoadingScreen()
        self.add_widget(loading)
        self.current = "loadingScreen"

    @staticmethod
    def resize_window(size):
        app = App.get_running_app()
        app.config.set('WindowSettings', 'Width', size[0])
        app.config.set('WindowSettings', 'Height', size[1])
        app.config.write()



