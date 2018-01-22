# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

kv = """
<UserAccountTab>:
    BoxLayout:
        orientation: "vertical"
        size_hint_y:None
        height: self.minimum_height
        padding: "20dp"
        spacing: "5dp"
        MDCard:
            size_hint_y:None
            height: sum(x.height for x in self.children)
            padding: "10dp"
            BoxLayout:  # Image box
                orientation: "vertical"
                size_hint: None, None
                size: dp(200), self.parent.height - dp(20)
                Image:
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    source:"res\\me.png"
                MDLabel:
                    markup:True
                    text:f"{(icon('fa-key', 15, font_name='font_awesome'))} Logged in as"
                    theme_text_color: "Primary"
                    halign:"center"
                MDLabel:
                    text: f"{app.config.get('User','FirstName')} {app.config.get('User','LastName')}"
                    font_style: "Subhead"
                    theme_text_color: "Primary"
                    halign:"center"

            BoxLayout:
                orientation: "vertical"
                BoxLayout: # Title
                    size_hint: None, None
                    size: self.parent.width, dp(30)
                    canvas:
                        Color:
                            rgb: C("#db8625")
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    MDLabel:
                        text: "User Info"
                        halign: "center"
                        font_style: "Title"
                        theme_text_color: "Primary"

                BoxLayout: # middle block
                    padding: (dp(20), 0)
                    BoxLayout: # middle first half
                        size_hint: 0.6, 1
                        orientation:"vertical"
                        HSeparator:
                        BoxLayout:
                            MDLabel:
                                text: "Username: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: f"{app.config.get('User','Username')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "First Name: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: f"{app.config.get('User','FirstName')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "Last Name: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: f"{app.config.get('User','LastName')}"
                                theme_text_color: "Primary"
                        HSeparator:
                    BoxLayout: # middle second half
                        orientation: "vertical"
                        HSeparator:
                        BoxLayout:
                            MDLabel:
                                text: "Email: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: f"{app.config.get('User','Email')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "Password: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: "******"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "Role: "
                                theme_text_color: "Primary"
                                halign: "center"
                            MDLabel:
                                text: f"{app.config.get('User','Role')}"
                                theme_text_color: "Primary"
                        HSeparator:

                BoxLayout:  #Buttons
                    size_hint:None,None
                    size: self.parent.width, dp(40)
                    padding: (self.width/3, 0)
                    MDFlatButton:
                        text: "Update info"
                    MDFlatButton:
                        text: "Sign Out"
                        on_release: root.drivers.sign_out()
        # App Info
        MDCard:
            padding: "10dp"
            size_hint_y:None
            height: sum(x.height for x in self.children)
            FloatLayout: #Image Box
                size_hint: None, None
                size: dp(200), self.parent.height - dp(20)
                Image:
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    source: "res\\icon\\icon.png"
            BoxLayout: #details box
                orientation: "vertical"
                BoxLayout: # title
                    size_hint_y: None
                    height: dp(30)
                    canvas:
                        Color:
                            rgb: C("#db8625")
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    MDLabel:
                        text: "App Info"
                        halign: "center"
                        font_style: "Title"
                        theme_text_color: "Primary"
                BoxLayout: # middle
                    orientation: "vertical"
                    padding: (dp(20), 0)
                    HSeparator:
                    BoxLayout:
                        MDLabel:
                            text: "App Name: "
                            theme_text_color: "Primary"
                            halign: "center"
                        MDLabel:
                            text: f"{app.config.get('App','Name')}"
                            theme_text_color: "Primary"
                    BoxLayout:
                        MDLabel:
                            text: "Current Version: "
                            theme_text_color: "Primary"
                            halign: "center"
                        MDLabel:
                            text: f"{app.config.get('App','Version')}"
                            theme_text_color: "Primary"
                    BoxLayout:
                        MDLabel:
                            text: "Author: "
                            theme_text_color: "Primary"
                            halign: "center"
                        MDLabel:
                            text: f"{app.config.get('App','Author')}"
                            theme_text_color: "Primary"
                    HSeparator:

                BoxLayout: # buttons
                    size_hint:None,None
                    size: self.parent.width, dp(40)
                    padding: (self.width/3, 0)
                    MDFlatButton:
                        text: "Check Updates"
                    MDFlatButton:
                        text: "Whats New"

        # Device Info
        MDCard:
            padding: "10dp"
            size_hint_y:None
            height: sum(x.height for x in self.children)

            FloatLayout: #Image Box
                size_hint: None, None
                size: dp(200), self.parent.height - dp(20)
                Image:
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    source: "res\\device.png"
            BoxLayout: #details box
                orientation: "vertical"
                BoxLayout: # title
                    size_hint_y: None
                    height: dp(30)
                    canvas:
                        Color:
                            rgb: C("#db8625")
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    MDLabel:
                        text: "Device Info"
                        halign: "center"
                        font_style: "Title"
                        theme_text_color: "Primary"
                BoxLayout: # middle block
                    padding: (dp(20), 0)
                    BoxLayout: # middle first half
                        orientation: "vertical"
                        HSeparator:
                        BoxLayout:
                            MDLabel:
                                text: "Computer Name: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','DEVICE_NAME')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "OS Name: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','OS_NAME')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "OS Version: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','OS_VER')}"
                                theme_text_color: "Primary"
                        HSeparator:
                    BoxLayout: # middle second half
                        orientation: "vertical"
                        HSeparator:
                        BoxLayout:
                            MDLabel:
                                text: "CPU: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','CPU')}"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "Ram: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','RAM')} GB"
                                theme_text_color: "Primary"
                        BoxLayout:
                            MDLabel:
                                text: "Onboard GPU: "
                                theme_text_color: "Primary"
                                halign: "center"
                                size_hint_x: 0.45
                            MDLabel:
                                text: f"{app.config.get('Device','GPU')}"
                                theme_text_color: "Primary"
                        HSeparator

        # statistics
        MDCard:
            orientation: "vertical"
            padding: "10dp"
            size_hint_y:None
            height: sum(x.height for x in self.children)
            BoxLayout:
                size_hint_y: None
                height: dp(30)
                canvas:
                    Color:
                        rgb: C("#db8625")
                    Rectangle:
                        size: self.size
                        pos: self.pos
                MDLabel:
                    text: "Stats"
                    halign: "center"
                    font_style: "Title"
                    theme_text_color: "Primary"
            HSeparator:
            MDLabel:
                text: "Nothing to show"
                halign: "center"
                theme_text_color: "Primary"
            HSeparator:


<UserComponentTab>:
    BoxLayout:

        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        padding: "20dp"
        spacing: "5dp"
        BoxLayout: # Title primary
            size_hint_y: None
            height: dp(30)
            canvas:
                Color:
                    rgb: C("#db8625")
                Rectangle:
                    size: self.size
                    pos: self.pos
            MDLabel:
                text: "Core Component"
                halign: "center"
                font_style: "Title"
                theme_text_color: "Primary"

        BoxLayout: # Component box primary
            id: component_box_id
            orientation: "vertical"
            size_hint_y:None
            height: self.minimum_height
            spacing: "10dp"

            MDCard: # individual component
                size_hint_y:None
                height: sum(x.height for x in self.children)
                padding: "10dp"
                BoxLayout:
                    padding: (dp(20), 0)
                    MDLabel: # component icon
                        markup: True
                        text: f"{(icon('fa-plug', 30, font_name='font_awesome'))}"
                        theme_text_color: "Primary"
                        size_hint_x: None
                        width: dp(70)
                    BoxLayout:
                        orientation: "vertical"
                        size_hint_x: None
                        width: sum(x.width for x in self.children)
                        MDLabel:
                            text: "User Component"
                            theme_text_color: "Primary"
                            font_style: "Subhead"
                        MDLabel:
                            text: "Version: 1.0"
                            theme_text_color: "Primary"
                            font_style: "Caption"
                    MDLabel:
                        text: "A brief description About the Component. It is the core component of the software pandor astrum vault"
                        theme_text_color: "Primary"
                    BoxLayout: # Blank space
                        size_hint_x: None
                        width: dp(20)
                    MDSwitch:
                        size_hint: None, None
                        size: dp(36), dp(48)
                        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                        active: True

            MDCard: # individual component
                size_hint_y:None
                height: sum(x.height for x in self.children)
                padding: "10dp"
                BoxLayout:
                    padding: (dp(20), 0)
                    MDLabel: # component icon
                        markup: True
                        text: f"{(icon('fa-plug', 30, font_name='font_awesome'))}"
                        theme_text_color: "Primary"
                        size_hint_x: None
                        width: dp(70)
                    BoxLayout:
                        orientation: "vertical"
                        size_hint_x: None
                        width: sum(x.width for x in self.children)
                        MDLabel:
                            text: "Help Component"
                            theme_text_color: "Primary"
                            font_style: "Subhead"
                        MDLabel:
                            text: "Version: 1.0"
                            theme_text_color: "Primary"
                            font_style: "Caption"
                    MDLabel:
                        text: "A brief description About the Component. It is the core component of the software pandor astrum vault"
                        theme_text_color: "Primary"
                    BoxLayout: # Blank space
                        size_hint_x: None
                        width: dp(20)
                    MDSwitch:
                        size_hint: None, None
                        size: dp(36), dp(48)
                        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                        active: True
                        on_active: print("I am Active")

        BoxLayout: # Title secondary
            size_hint_y: None
            height: dp(30)
            canvas:
                Color:
                    rgb: C("#db8625")
                Rectangle:
                    size: self.size
                    pos: self.pos
            MDLabel: # Title
                text: "Secondary Component"
                halign: "center"
                font_style: "Title"
                theme_text_color: "Primary"

        BoxLayout: # Component box secondary
            orientation: "vertical"
            size_hint_y:None
            height: self.minimum_height
            spacing: "10dp"
            MDCard: # individual component
                size_hint_y:None
                height: sum(x.height for x in self.children)
                padding: "10dp"
                BoxLayout:
                    padding: (dp(20), 0)
                    MDLabel: # component icon
                        markup: True
                        text: f"{(icon('fa-plug', 30, font_name='font_awesome'))}"
                        theme_text_color: "Primary"
                        size_hint_x: None
                        width: dp(70)
                    BoxLayout:
                        orientation: "vertical"
                        size_hint_x: None
                        width: sum(x.width for x in self.children)
                        MDLabel:
                            text: "User Component"
                            theme_text_color: "Primary"
                            font_style: "Subhead"
                        MDLabel:
                            text: "Version: 1.0"
                            theme_text_color: "Primary"
                            font_style: "Caption"
                    MDLabel:
                        text: "A brief description About the Component. It is the core component of the software pandor astrum vault"
                        theme_text_color: "Primary"
                    BoxLayout: # Blank space
                        size_hint_x: None
                        width: dp(20)
                    MDSwitch:
                        size_hint: None, None
                        size: dp(36), dp(48)
                        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                        active: True

        BoxLayout: # Buttons
            orientation: "vertical"
            size_hint_y:None
            height: self.minimum_height
            padding: "10dp"
            spacing: "10dp"
            BoxLayout: # Blank space
            AnchorLayout:
                MDRaisedButton:
                    pos_hint: {"center_x": 0.5, "center_y": 1}
                    text: "Save Component Settings"



<UserPreferenceTab>:
    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        padding: "20dp"
        spacing: "5dp"
        BoxLayout: # Title Theme
            size_hint_y: None
            height: dp(30)
            canvas:
                Color:
                    rgb: C("#db8625")
                Rectangle:
                    size: self.size
                    pos: self.pos
            MDLabel:
                text: "Theme & Colors"
                halign: "center"
                font_style: "Title"
                theme_text_color: "Primary"
        BoxLayout: # Theme Card
            size_hint_y: None
            height: sum(x.height for x in self.children)
            MDCard:
                padding: "10dp"
                BoxLayout:
                    size_hint_x: None
                    width: self.minimum_width
                    padding: (dp(5), 0)
                    MDLabel: # icon
                        markup: True
                        text: f"{(icon('fa-paint-brush', 30, font_name='font_awesome'))}"
                        theme_text_color: "Primary"
                        size_hint_x: None
                        width: dp(70)
                        halign: "center"
                BoxLayout: # Settings details
                    BoxLayout: # theme style box
                        orientation: "vertical"
                        MDLabel:
                            text: "Theme Style"
                            halign: "center"
                            theme_text_color: "Primary"
                            font_size: "16"
                        HSeparator:
                        MDLabel:
                            text: f"{app.config.get('Theme','ThemeStyle')}"
                            halign: "center"
                            theme_text_color: "Primary"
                    VSeparator:
                    BoxLayout: # primary color box
                        orientation: "vertical"
                        MDLabel:
                            text: "Primary Color"
                            halign: "center"
                            theme_text_color: "Primary"
                            font_size: "16"
                        HSeparator:
                        MDLabel:
                            text: f"{app.config.get('Theme','PrimaryColor')}"
                            halign: "center"
                            theme_text_color: "Primary"
                    VSeparator:
                    BoxLayout: # accent color box
                        orientation: "vertical"
                        MDLabel:
                            text: "Accent Color"
                            halign: "center"
                            theme_text_color: "Primary"
                            font_size: "16"
                        HSeparator:
                        MDLabel:
                            text: f"{app.config.get('Theme','AccentColor')}"
                            halign: "center"
                            theme_text_color: "Primary"

                BoxLayout: # Buttons
                    size_hint_x: None
                    width: self.minimum_width
                    padding: (dp(20), 0)
                    MDRaisedButton:
                        text: 'Change theme'
                        on_release: MDThemePicker().open()
                        opposite_colors: True
                        pos_hint: {"center_y": 0.5}


<UserHelpTab>:
    BoxLayout:
        Button:
            text: "Coming Soon Help Tab"
"""