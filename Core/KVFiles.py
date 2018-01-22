# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "kv design files for core"
"""
__all__ = [
    "seperator_kv",
    "launchPad_kv",
    "loadingScreen_kv",
    "loginScreen_kv",
    "registration_kv",
    "errorScreen_kv",
    "mainScreen_kv",
    "componentBase_kv",
    "defaultScreen_kv",
    "tabBase_kv",
    "defaultTab_kv",
    "tabWithoutDrawer_kv",
    "tabWithDrawer_kv",
    "miningField_kv"
]

testKV = """
<GeneralTab>:
    id: content_id
    orientation: "vertical"
    Button:
        text: "Okay"
"""


seperator_kv = """
<Gap>:
    size_hint: (None, None)
    height: self.minimum_height if self.height_dp == None else self.height_dp
    width: self.minimum_width if self.width_dp == None else self.width_dp
<Separator>:
    canvas:
        Color:
            rgba: app.theme_cls.divider_color
        Rectangle:
            pos: self.pos
            size: self.size

<VSeparator>:
    size_hint_x: None
    width: dp(2)

<HSeparator>:
    size_hint_y: None
    height: dp(2)
"""
miningField_kv = """
<MiningField>
    id: mining_field_id
    size_hint_y: None
    height: self.minimum_height
    padding: (dp(20), dp(5))

    MDCard:
        id: field_mdcard_id
        size_hint_y: None
        height: self.minimum_height
        padding: (dp(20), dp(5))
        spacing: dp(20)
        MDTextField:
            hint_text: "Field Name"
            color_mode: "accent"
        MDTextField:
            hint_text: "Xpath"
            color_mode: "accent"
        MDIconButton:
            icon: "delete"
"""

tabWithDrawer_kv = """
<TabWithDrawer>:
    NavigationLayout:
        id: nav_layout_id
        BoxLayout:
            # MDNavigationDrawer add here --------------------------------------
            id: nav_drawer
            orientation: "horizontal"

        BoxLayout:
            # Toolbar add here -------------------------------------------------
            orientation: "vertical"
            id: toolbar_id
            canvas:
                Color:
                    rgb: C('5BAD00')
                Rectangle:
                    pos: self.pos
                    size: self.size
            # Toolbar:
            #     # must have top bar
            #
                # size_hint_y: 0.1
                # right_action_items: [['dots-vertical', lambda x: self.parent.parent.parent.toggle_nav_drawer()]]
            # BoxLayout:
            #     id: content_id
            #     orientation: "vertical"
            #     Button:
            #         text: "OKAY"
"""
tabWithoutDrawer_kv = """
# <TabBase2>:
#     BoxLayout:
#         orientation: "vertical"
#         canvas:
#             Color:
#                 rgb: C('5BAD00')
#             Rectangle:
#                 pos: self.pos
#                 size: self.size
"""
defaultTab_kv = """
<DefaultTab>:
    BoxLayout:
        id: default_screen_id
        canvas:
            Color:
                rgb: C('5F5567')
            Rectangle:
                pos: self.pos
                size: self.size
"""
tabBase_kv = """
<_Tab>:
    NavigationLayout:
        id: nav_layout_id
        BoxLayout:
            # MDNavigationDrawer add here --------------------------------------
            id: nav_drawer
            orientation: "horizontal"

        BoxLayout:
            # Toolbar add here -------------------------------------------------
            orientation: "vertical"
            id: toolbar_id
            canvas:
                Color:
                    # rgba:app.theme_cls.bg_dark
                    rgb: C("#3B3A39")
                Rectangle:
                    pos: self.pos
                    size: self.size
"""
componentBase_kv = """
<ComponentBase>:
    BoxLayout:
        id: src_mngr_level_3_id
        pos_hint: {"right": 1, "y": 0}
        size_hint: 0.95, 1

    # tabs ---------------------------
    FloatLayout:
        id: tab_panel_id
        size_hint: 0.05, 1
        canvas:
            Color:
                rgb: C('#222222')
            Rectangle:
                pos: self.pos
                size: self.size
"""
defaultScreen_kv = """
<DefaultScreen>:
    BoxLayout:
        id: default_screen_id
        canvas:
            Color:
                rgb: C('#AAAAAA')
            Rectangle:
                pos: self.pos
                size: self.size
"""
mainScreen_kv = """
# Main Root
<MainScreen>:
    BoxLayout:
        orientation: "vertical"

        # Action Bar -------------------------------------
        ActionBar:
            pos_hint: {'top':1}
            # App Logo here ------------
            ActionView:
                orientation: 'horizontal'
                padding: '5dp'
                use_separator: True
                ActionPrevious:
                    title: ''
                    with_previous: False

                # contextual DropDown ---------------------
                ActionOverflow:
                    id: action_overflow_id

                # DropDown Selection ----------------------
                ActionGroup:
                    id: act_spinner_id
                    markup:True
                    text: f"{(icon('fa-chevron-circle-down', 20, font_name='font_awesome'))} Select"
                    mode: 'spinner'
                    size_hint_x: None

                ActionButton:
                    halign: "center"
                    markup: True
                    text:f"{(icon('fa-bell', 20, font_name='font_awesome'))}"
                ActionButton:
                    halign: "center"
                    markup: True
                    text:f"{(icon('fa-flag', 20, font_name='font_awesome'))}"
                ActionButton:
                    halign: "center"
                    markup: True
                    text:f"{(icon('fa-user', 20, font_name='font_awesome'))}"

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
# need fix on error_message_id (centralize)
errorScreen_kv = """
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
                    id: error_msg_id
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
                        on_release: root.try_again()
"""
#nedd fix button (at most bottom)
registration_kv = """
<RegistrationScreen>:
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
                        padding:"20dp"
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
                            on_release: root.back_to_login()
                        MDRaisedButton:
                            text: "Register"
                            size_hint:None, None
                            size:dp(48), dp(40)
                            pos_hint:{'center_x': 0.4, 'center_y': 0.5}
                            on_release: root.register_new()
"""
loginScreen_kv = """
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
                # login image ----------------------------------
                Image:
                    size_hint: 1, 0.6
                    source: "res\\lock.png"
                # login field ----------------------------------
                RelativeLayout:
                    MDTextField:
                        id: username
                        hint_text: "Username"
                        multiline: False
                        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
                        color_mode: "accent"
                    MDTextField:
                        id: passwd
                        hint_text: "Password"
                        multiline: False
                        password: True
                        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                        color_mode: "accent"
                    MDCheckbox:
                        id: offline_chkbox_id
                        size_hint:None, None
	    		        size:dp(48), dp(48)
		    	        pos_hint:{'center_x': 0.35, 'center_y': 0.15}
		    	        color: self.theme_cls.accent_color if offline_chkbox_id.active else self.theme_cls.secondary_text_color
                    MDLabel:
                        theme_text_color: 'Primary'
                        size_hint: None, None
                        size: dp(130), dp(48)
                        text: "Work Offline"
                        pos_hint:{'center_x': 0.6, 'center_y': 0.15}
                # Login buttons --------------------------------
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
                        on_release: root.new_register()
                    MDRaisedButton:
                        id: login_btn_id
                        text: "                                        Login                                        "
                        opposite_colors: True
                        size_hint:None, None
			            size:dp(48), dp(40)
                        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
                        on_release: root.login()
"""
loadingScreen_kv = """
<LoadingScreen>:
    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        active: True
        color: self.theme_cls.accent_color
"""
launchPad_kv = """
#:import icon utils.iconfonts.icon
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
#:import MDFlatButton kivymd.button
#:import MDIconButton kivymd.button
#:import MDRaisedButton kivymd.button
<LaunchPad>:
    id: mainRoot
    on_size: self.resize_window(self.size)
"""