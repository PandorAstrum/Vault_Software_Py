# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.Username = TextInput(multiline=False)
        self.add_widget(self.Username)
        self.add_widget(Label(text='Password'))
        self.Password = TextInput(password=True, multiline=False)
        self.add_widget(self.Password)

class LoginApp(App):
    def build(self):
        return LoginScreen()