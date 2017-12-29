# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "kv design files for all"
"""
launchPadKV = """
#:import icon bin.libPackage.iconfonts.icon
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout

#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
<LaunchPad>:
    id: mainRoot
    on_size: self.resize_window(self.size)
"""
seperatorKV = """
<Separator@Widget>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<VSeparator@Separator>:
    size_hint_x: None
    width: dp(2)

<HSeparator@Separator>:
    size_hint_y: None
    height: dp(2)
"""
loginScreenKV = """
<LoginScreen>:
    AnchorLayout:
        MDCard:
            size_hint: None, None
            size: dp(400), dp(400)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            BoxLayout:
                size_hint: None, None
			    size: dp(400), dp(400)
                orientation: "vertical"
                padding: "20dp"
                # login image -------------------------------------------------------------
                Image:
                    size_hint: 1, 0.6
                    source: "res\\lock.png"
                # login field -------------------------------------------------------------
                RelativeLayout:
                    MDTextField:
                        id: username
                        hint_text: "Username"
                        multiline: False
                        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
                    MDTextField:
                        id: passwd
                        hint_text: "Password"
                        multiline: False
                        password: True
                        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                    MDCheckbox:
                        id: chkbox
                        size_hint:None, None
	    		        size:dp(48), dp(48)
		    	        pos_hint:{'center_x': 0.35, 'center_y': 0.15}
                    MDLabel:
                        theme_text_color: 'Primary'
                        size_hint: None, None
                        size: dp(130), dp(48)
                        text: "Work Offline"
                        pos_hint:{'center_x': 0.6, 'center_y': 0.15}
                # Login buttons -----------------------------------------------------------
                RelativeLayout:
                    size_hint:None, None
			        size:dp(360), dp(100)
                    MDRaisedButton:
                        text: "Forget password?"
                        size_hint: None, None
				        size: dp(48), dp(40)
                        pos_hint:{'center_x': 0.3, 'center_y': 0.25}
                        on_release: root.forget()
                    MDRaisedButton:
                        text: "    New User?    "
                        size_hint: None, None
				        size: 4*dp(48), dp(40)
                        pos_hint:{'center_x':0.75,'center_y':0.25}
                        on_release: root.newRegister()
                    MDRaisedButton:
                        id: loginbtn
                        text: "                                        Login                                        "
                        size_hint:None, None
			            size:dp(48), dp(40)
                        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
                        on_release: root.login()
"""
newRegistrationKV = """
<NewRegistrationScreen>:
    AnchorLayout:
        MDCard:
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            BoxLayout:
                orientation: "vertical"
                padding: "20dp"
                Image:
                    size_hint: 0.2, 0.2
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    source: "res\\edit_u.png"
                ScrollView:
			        do_scroll_x: False
			        MDList:
                        padding: "20dp"
                        id: test
                        MDTextField:
                            id: usrname
                            hint_text: "Username"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: fname
                            hint_text: "First Name"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: mname
                            hint_text: "Middle Name"
                            helper_text: "If Available (Optional)"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            id: lname
                            hint_text: "Last Name"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: passwrd
                            hint_text: "Password"
                            multiline: False
                            password: True
                            required: True
                            helper_text: "Atleast 8 charecters"
                            helper_text_mode: "on_focus"
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: email
                            hint_text: "Email"
                            helper_text: "Please enter a valid email address"
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: ph
                            hint_text: "Phone"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: addLines
                            hint_text: "Address Line"
                            helper_text: "(Optional)"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            id: city
                            hint_text: "City"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            id: country
                            hint_text: "Country"
                        MDTextField:
                            id: company
                            hint_text: "Company"
                            color_mode: "accent"
                HSeparator:
                BoxLayout:
                    size_hint: 1, 0.1
                    canvas:
                        Color:
                            rgba: 0.2, 0.2, 0.2, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    RelativeLayout:
                        size_hint: 0.8, 0.8
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDRaisedButton:
                            text: "Cancel"
                            size_hint:None, None
                            size:dp(48), dp(40)
                            pos_hint:{'center_x': 0.6, 'center_y': 0.5}
                            on_release: root.backToLogin()
                        MDRaisedButton:
                            text: "Register"
                            size_hint:None, None
                            size:dp(48), dp(40)
                            pos_hint:{'center_x': 0.4, 'center_y': 0.5}
                            on_release: root.registerNew()
    # AnchorLayout:
    #     canvas:
    #         Color:
    #             rgba: 0.1, 0.1, 0.1, 1
    #         Rectangle:
    #             pos: self.pos
    #             size: self.size
    #     ScrollView:
		# 	do_scroll_x: False
    #         BoxLayout:
    #             size_hint:None, None
		# 	    size:dp(400), dp(800)
    #             orientation: "vertical"
    #             padding: "20dp"
    #             canvas:
    #                 Color:
    #                     rgba: 0.9, 0.9, 0.9, 1
    #                 Rectangle:
    #                     pos: self.pos
    #                     size: self.size
		# 	    MDTextField:
    #                 id: username
    #                 hint_text: "Username"
    #                 required: True
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: fname
    #                 hint_text: "First Name"
    #                 required: True
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: mname
    #                 hint_text: "Middle Name"
    #                 helper_text: "If Available (Optional)"
    #                 helper_text_mode: "on_focus"
    #             MDTextField:
    #                 id: lname
    #                 hint_text: "Last Name"
    #                 required: True
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: pss
    #                 hint_text: "Password"
    #                 multiline: False
    #                 password: True
    #                 required: True
    #                 helper_text: "Atleast 8 charecters"
    #                 helper_text_mode: "on_focus"
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 hint_text: "Email"
    #                 helper_text: "Please enter a valid email address"
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: ph
    #                 hint_text: "Phone"
    #                 required: True
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: pss
    #                 hint_text: "Address Line"
    #                 helper_text: "(Optional)"
    #                 helper_text_mode: "on_focus"
    #             MDTextField:
    #                 id: pss
    #                 hint_text: "City"
    #                 required: True
    #                 helper_text_mode: "on_error"
    #             MDTextField:
    #                 id: pss
    #                 hint_text: "Country"
    #             MDTextField:
    #                 id: pss
    #                 hint_text: "Company"
"""
errorScreenKV = """
<ErrorScreen>:
    AnchorLayout:
        MDCard:
            size_hint: None, None
            size: dp(400), dp(300)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            BoxLayout:
                size_hint:None, None
			    size:dp(400), dp(300)
                orientation: "vertical"
                padding: "20dp"

                MDLabel:
                    id: errorTextBox
                    text: "Password or Username is Incorrect"
                    font_style: "Title"
                    theme_text_color: 'Primary'
                RelativeLayout:
                    size_hint:None, None
			        size:dp(360), dp(100)
                    MDRaisedButton:
                        text: "                                      Try Again                                      "
                        size_hint:None, None
			            size:dp(48), dp(40)
                        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
                        on_release: root.tryAgain()
"""

mainScreenKV = """
# Main Root
<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        # on_size: self.resize_window(self.size)

    #   Action Bar ---------------------------------------------------------------
        ActionBar:
            pos_hint: {'top':1}
            # App Logo
            ActionView:
                orientation: 'horizontal'
                padding: '5dp'
                use_separator: True
                ActionPrevious:
                    title: ''
                    with_previous: False

                # contextual DropDown
                ActionOverflow: # Build Content From PY
                    id: action_overflow_id

                # DropDown Selection
                ActionGroup: # Build Content From PY
                    id: act_spinner_id
                    markup:True
                    text: ""
                    mode: 'spinner'
                    size_hint_x: None


                ActionButton:
                    halign: "center"
                    markup: True
                    text:"%s"%(icon('fa-bell', 20))
                ActionButton:
                    halign: "center"
                    markup: True # Always turn markup on
                    text:"%s"%(icon('fa-flag', 20))
                ActionButton:
                    halign: "center"
                    markup: True # Always turn markup on
                    text:"%s"%(icon('fa-user', 20))

    #Main screen Manager ---------------------------------------------------------

        BoxLayout:
            id: src_mngr_level_2_id
            canvas:
                Color:
                    rgb: C('#AAAAAA')
                Rectangle:
                    pos: self.pos
                    size: self.size

    # Bottom Bar -----------------------------------------------------------------
        BoxLayout:
            pos_hint: {'bottom':1}
            size_hint: 1, None
            height: "16px"
            canvas:
                Color:
                    rgb: C('#1F1F1F')
                Rectangle:
                    pos: self.pos
                    size: self.size
"""


notificationKV = """
BoxLayout:
    canvas:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    orientation: 'vertical'

    GridLayout:
        cols: 2
        size_hint_y: 0.2
        canvas:
            Color:
                rgba: app.line_color

            Line:
                points:
                    [self.pos[0], self.pos[1] + dp(1),
                    self.pos[0] + self.width,
                    self.pos[1] + dp(1)]

        Label:
            color: app.color
            text_size:
                [self.width - dp(10),
                self.height]
            text: app.notif_title
            halign: 'left'
            markup: True
            shorten: True
            shorten_from: 'right'

        Button:
            background_normal:
                'atlas://data/images/defaulttheme/bubble_btn'
            color: app.color
            size_hint_x: None
            width: self.height
            text: 'X'
            on_release: stopTouchApp()

    GridLayout:
        id: container
        cols: 2
        size_hint_y: 0.8

        FloatLayout:
            size_hint_x: 0.3
            Image:
                source: app.notif_icon
                size_hint: (None, None)
                width: dp(64)
                height: dp(64)
                pos_hint: {'center': (0.5, 0.5)}

        ScrollView:
            Label:
                color: app.color
                text: app.message
                text_size:
                    [self.width,
                    self.height]
                size_hint_y: None
                padding: (5, 5)
                text_size: self.width, None
                height: self.texture_size[1]
                markup: True
"""

loadingScreenKV = """
<LoadingScreen>:
    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        active: True
"""

mainAppKV = """
<Root>:
    id: mainRoot
    Button:
        text: "Okay"
"""