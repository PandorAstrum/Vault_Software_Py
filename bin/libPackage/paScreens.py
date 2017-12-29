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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.button import MDRaisedButton
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar
from kivymd.tabs import MDTabbedPanel, MDTab
from kivymd.textfields import MDTextField

from bin.libPackage.jsonUtility import dump_json
from bin.libPackage.notification import Notification
from bin.libPackage.cipherRSA import CipherRSA
from bin.libPackage.localStorage import LocalStorage
from bin.libPackage.googleSheet import GoogleSheet
from bin.libPackage.paUtility import PaUtility, _check_internet
from bin.libPackage.paUtility import threaded
from bin.libPackage.kvFiles import *
from data.testclass.MDToggleButton import MDToggleButton

Builder.load_string(launchPadKV + loginScreenKV + newRegistrationKV + errorScreenKV + seperatorKV  + mainScreenKV + loadingScreenKV + mainAppKV)



class ErrorScreen(Screen):

    def __init__(self, err, **kwargs):
        super(ErrorScreen, self).__init__(**kwargs)
        self.name = "errorScreen"
        self.ids.errorTextBox.text = err

    def tryAgain(self):
        login = LoginScreen(instance=None)
        self.manager.clear_widgets()
        self.manager.add_widget(login)
        self.manager.current = "loginScreen"

class MainScreen(Screen):
    def __init__(self, loginName, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = "mainScreen"
        self.app_icon = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\res\\logo.png"
        self.loginName = loginName
        self.localStorage = LocalStorage(debug=True)
        self._snackbar("simple", "Logged in as {}".format(self.loginName))
        self.make()

    def _snackbar(self, snack_type, msg):
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    @mainthread
    def make(self):
        # get all component
        app = App.get_running_app()
        comp = app.config.get("Component", "PrimaryComponentList")
        loc = app.config.get("Component", "Loc")
        component = comp.replace("(", "").replace(")", "").replace("'","").replace(" ", "").split(",")

        # position_y = 1
        for i in component:
            # print(i)
            # btn = MDTab(text=i)
        #     # btn = MDTabbedPanel(tab_orientation="top",tab_display_mode="text")
        #     # # btn.allow_no_selection = False
        #     # # btn.bind(on_press=partial(callback))
        #     self.ids.tab_panel.add_widget(btn)
        #     position_y -= 0.09
            self.initializeComponent(i, self.localStorage.storage)
        # print(type(ii))
        # print(ii)
        pass

    def initializeComponent(self, component_name, loc):
        COMPONENT_CLASS = f"bin.Component.{component_name}Component.Component"
        module = importlib.import_module(COMPONENT_CLASS, ".")
        comp = module.Component()
        return comp.json_settings

        # dumpJson(js,loc)
        # print(comp.json_settings)

class NewRegistrationScreen(Screen):

    def __init__(self, **kwargs):
        super(NewRegistrationScreen, self).__init__(**kwargs)
        self.name = "registration"

    def registerNew(self):
        print(self.ids.test)
        # generate RSA key
        # take all the details and make a row
        #encrypt data using RSA key
        # test = (self.ids.usrname.text, self.ids.fname.text, self.ids.mname.text, self.ids.lname.text, self.ids.passwrd.text, self.ids.email.text, self.ids.ph.text, self.ids.addLines.text, self.ids.city.text, self.ids.country.text)
        # connect on google sheet and put the row
        # download the encryption key and store it appdata
        # back to login page
        # print(test)

    def backToLogin(self):
        self.login = LoginScreen(instance=None)
        self.manager.clear_widgets()
        self.manager.add_widget(self.login)
        self.manager.current = "loginScreen"

class LoginScreen(Screen):
    """
    DocString
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = "loginScreen"
        self.working = False

    def _snackbar(self, snack_type, msg):
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
            if self.ids.chkbox.active:
                self._offlineLogin()
            else:
                self._onlineLogin()

    def newRegister(self):
        self.registration = NewRegistrationScreen()
        self.manager.clear_widgets()
        self.manager.add_widget(self.registration)
        self.manager.current = "registration"

    def _onlineLogin(self):
        print("Trying Online")
        try:
            # go to google sheet and try to match with username and pass
            PaUtility()._checkInternet()
        except ConnectionError:
            self._snackbar("simple", "No internet")
        finally:
            # if match then self manager add widget root widget
            # if not then self manager add widget wrong passowrd
            self.ids.loginbtn.disabled = True

    def _offlineLogin(self):
        app = App.get_running_app()
        if self.ids.username.text != app.config.get('Client', 'Username'):
            errScreen = ErrorScreen(err="Username is Incorrect")
            self.manager.clear_widgets()
            self.manager.add_widget(errScreen)
            self.manager.current = "errorScreen"
        elif self.ids.passwd.text != app.config.get('Client', 'Password'):
            errScreen = ErrorScreen(err="Password is Incorrect")
            self.manager.clear_widgets()
            self.manager.add_widget(errScreen)
            self.manager.current = "errorScreen"
        else:
            mainScreen = MainScreen(loginName=app.config.get('Client', 'Username'))
            self.manager.clear_widgets()
            self.manager.add_widget(mainScreen)
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
        self._make()

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
