# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from functools import partial

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.resources import resource_find
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar
from kivymd.textfields import MDTextField

from bin.libPackage.notification import Notification

from bin.libPackage.kvFiles import *

Builder.load_string(loginScreenKV + newRegistrationKV + errorScreenKV + seperatorKV + RootScreenMngrKV + mainScreenKV)

class LoginScreen(Screen):

    def login(self):
        username = self.ids.username.text
        password = self.ids.passwd.text
        if not username:
            self._snackbar("simple", "Username is empty")
        elif not password:
            self._snackbar("simple", "Password is empty")
        else:
            if self.ids.chkbox.active:
                self.offlineLogin()
            else:
                self.onlineLogin()
            # mix username and password with UUID and create the encryption key pass to method


    def _snackbar(self, snack_type, msg):
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()


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

        # if username and password:
        #     print(username, password)
        # else:
        #     print("username is empty")
        # print("username {} and password {}".format(username, password))

        # if self.ids.chkbox.active:
        #     self.offlineLogin()
        # else:
        #     self.onlineLogin()

    def _onlineLogin(self):
        # take encryption key
        # connect on sheet and match the encryption key
        # if matched then change the manager to mainscreen
        # or change the manager to errorScreen
        if self.ids.username.text == "" or self.ids.passwd.text:
            # rasie empty error
            print("username empty")
        else:

            if self.ids.username.text == "root" and self.ids.passwd.text == "123":
                self.manager.current = "mainScreen"
            else:
                self.manager.current = "errScreen"
        print("trying online")

    def _offlineLogin(self):
        # take UUID and input text
        # make encryption key
        # search for encryption key on appdata and match
        print("trying offline")

    def persistentLogin(self):
        # search for encryption key on appdata
        print("persistent login successful")

    def newRegister(self):
        self.manager.current = "registration"

    def forgetPass(self):
        # open popup
        pass
    def show_example_dialog(self):
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

class NewRegistrationScreen(Screen):
    def __init__(self, **kwargs):
        # self.username = MDTextField(id="test", hint_text="test")
        # self.ids.test.add_widget(self.username)
        super(NewRegistrationScreen, self).__init__(**kwargs)
        # self.on_create()
        # print()
    # validate email
    def on_create(self):
        username = MDTextField(id="test", hint_text="test")
        print(self.ids['test'])
    # register email
    def registerNew(self):
        print(self.ids.test)
        # take all the details and make a row
        # test = (self.ids.usrname.text, self.ids.fname.text, self.ids.mname.text, self.ids.lname.text, self.ids.passwrd.text, self.ids.email.text, self.ids.ph.text, self.ids.addLines.text, self.ids.city.text, self.ids.country.text)
        # connect on google sheet and put the row
        # download the encryption key and store it appdata
        # back to login page
        # print(test)

    def backToLogin(self):
        # all text field deletes
        self.ids.usrname.text = ""
        self.ids.fname.text = ""
        self.ids.mname.text = ""
        self.ids.lname.text = ""
        self.ids.passwrd.text = ""
        self.ids.email.text = ""
        self.ids.ph.text = ""
        self.ids.addLines.text = ""
        self.ids.city.text = ""
        self.ids.country.text = ""
        self.ids.company.text = ""
        self.manager.current = "loginScreen"

class GirisOnayEkrani(Screen):
    pass

class ErrorScreen(Screen):
    def tryAgain(self):
        self.manager.current = "loginScreen"

class RootScreenMngr(ScreenManager):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app_icon = "C:\\Users\\Ana Ash\\Desktop\\Project Software\\KivyPy\\Vault\\res\\logo.png"

