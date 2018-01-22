# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
__all__ = [
    "kv"
]

mining_scrapy_tab_kv = """
<MiningScrapyTab>:
    BoxLayout:
        orientation: "vertical"
        size_hint_y:None
        height: self.minimum_height
        padding: "20dp"
        spacing: "5dp"
        Button:
            text: "Mining Scrapy Tab"
"""
mining_selenium_tab_kv = """
<MiningSeleniumTab>:
    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        padding: dp(20)
        spacing: dp(5)
        BoxLayout:
            size_hint_y: None
            height: sum(x.height for x in self.children)
            MDCard:
                orientation: "vertical"
                MDLabel: # Title
                    size_hint_y: None
                    height: dp(30)
                    text:"Select A Browser"
                    theme_text_color: "Primary"
                    font_style: "Body2"
                    halign: "center"
                BoxLayout: # separator
                    padding: (dp(40), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:
                BoxLayout: # checker box
                    size_hint: None, None
                    height: self.minimum_height
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    spacing: dp(40)
                    MDCheckbox:
                        id: google_chrome_id
                        group: 'browser_select'
                        size_hint: None, None
                        size: dp(48), dp(48)
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Google Chrome"
                        theme_text_color: "Primary" if google_chrome_id.active else "Secondary"
                    MDCheckbox:
                        id: mozilla_firefox_id
                        group: 'browser_select'
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Mozilla Firefox"
                        theme_text_color: "Primary" if mozilla_firefox_id.active else "Secondary"
                    MDCheckbox:
                        id: ie_id
                        group: 'browser_select'
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Internet Explorer"
                        theme_text_color: "Primary" if ie_id.active else "Secondary"

        BoxLayout: # Login box
            size_hint_y: None
            height: self.minimum_height
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: self.parent.width, self.minimum_height
                padding: (dp(40), 0)
                MDLabel: # Title
                    size_hint_y: None
                    height: dp(30)
                    text:"Login (Optional)"
                    theme_text_color: "Primary"
                    font_style: "Body2"
                    halign: "center"
                BoxLayout: # separator
                    padding: (dp(40), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:
                BoxLayout: # login enabler
                    size_hint: None, None
                    height: self.minimum_height
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDSwitch:
                        id: login_option_id
                        size_hint: None, None
                        size: dp(36), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        _active: False
                BoxLayout: # linkedin login
                    padding: (dp(60), dp(5))
                    size_hint_y: None
                    height: self.minimum_height
                    MDCheckbox:
                        id: linkedin_id
                        group: "login_group"
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        disabled: False if login_option_id.active else True
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "LinkedIn"
                        theme_text_color: "Primary" if linkedin_id.active else "Secondary"
                    BoxLayout:
                        orientation: "vertical"
                        size_hint_y:None
                        height: self.minimum_height
                        MDTextField:
                            id: linkedin_username_id
                            hint_text: "LinkedIn Email" if linkedin_id.active else "Disabled"
                            disabled: False if linkedin_id.active else True
                            color_mode: "accent"
                        MDTextField:
                            id: linkedin_password_id
                            hint_text: "LinkedIn Password" if linkedin_id.active else "Disabled"
                            disabled: False if linkedin_id.active else True
                            color_mode: "accent"
                            multiline: False
                            password: True
                BoxLayout: # separator
                    padding: (dp(40), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:
                BoxLayout: # custom login
                    padding: (dp(60), dp(5))
                    size_hint_y:None
                    height: self.minimum_height
                    MDCheckbox:
                        id: custom_login_id
                        group: "login_group"
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        disabled: False if login_option_id.active else True
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Custom"
                        theme_text_color: "Primary" if custom_login_id.active else "Secondary"
                    BoxLayout:
                        size_hint_y:None
                        height: self.minimum_height
                        MDTextField:
                            id: sign_in_url_id
                            hint_text: "Sign in URL" if custom_login_id.active else "Disabled"
                            disabled: False if custom_login_id.active else True
                            color_mode: "accent"
                BoxLayout: # username password xpath
                    padding: (dp(60), dp(5))
                    spacing: dp(40)
                    size_hint_y: None
                    height: self.minimum_height
                    BoxLayout:
                        size_hint_y:None
                        height: self.minimum_height
                        orientation: "vertical"
                        MDTextField:
                            id: custom_username_id
                            hint_text: "Username" if custom_login_id.active else "Disabled"
                            disabled: False if custom_login_id.active else True
                            color_mode: "accent"
                        MDTextField:
                            id: custom_password_id
                            hint_text: "Password" if custom_login_id.active else "Disabled"
                            disabled: False if custom_login_id.active else True
                            color_mode: "accent"
                            multiline: False
                            password: True
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: "vertical"
                        MDTextField:
                            id: custom_username_xpath_id
                            hint_text: "Username Xpath" if custom_login_id.active else "Disabled"
                            disabled: False if custom_login_id.active else True
                            color_mode: "accent"
                        MDTextField:
                            id: custom_password_xpath_id
                            hint_text: "Password XPath" if custom_login_id.active else "Disabled"
                            disabled: False if custom_login_id.active else True
                            color_mode: "accent"
                BoxLayout: # sign in button xpath
                    padding: (dp(150), dp(5))
                    size_hint_y: None
                    height: self.minimum_height
                    MDTextField:
                        id: sing_in_btn_xpath_id
                        hint_text: "SignIn or LogIn Button XPath" if custom_login_id.active else "Disabled"
                        disabled: False if custom_login_id.active else True
                        color_mode: "accent"

        BoxLayout: # link box
            size_hint_y: None
            height: self.minimum_height
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: self.parent.width, self.minimum_height
                padding: (dp(40), 0)
                MDLabel: # Title
                    size_hint_y: None
                    height: dp(30)
                    text:"Scrap Link"
                    theme_text_color: "Primary"
                    font_style: "Body2"
                    halign: "center"
                BoxLayout: # separator
                    padding: (dp(20), 0)
                    size_hint_y: None
                    height: self.minimum_height
                    HSeparator:

                BoxLayout:
                    size_hint: None, None
                    height: dp(60)
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDCheckbox:
                        id: single_link_id
                        group: "scrapy link"
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                    MDLabel:
                        text: "Single link"
                        size_hint: None, None
                        height: self.parent.height
                        width: self.width
                        theme_text_color: "Primary" if single_link_id.active else "Secondary"
                BoxLayout: # main Link
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), 0)
                    MDTextField:
                        id: link_to_scrap_id
                        hint_text: "Paste Link" if single_link_id.active else "Disabled"
                        color_mode: "accent"
                        disabled: False if single_link_id.active else True
                BoxLayout: # link parameter Multipage
                    size_hint_y:None
                    height: self.minimum_height
                    padding: (dp(20), dp(5))
                    MDCheckbox:
                        id: next_page_id
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        disabled: False if single_link_id.active else True
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Continuous (Next Page)"
                        theme_text_color: "Primary" if next_page_id.active else "Secondary"
                    MDTextField:
                        id: next_page_xpath_id
                        hint_text: "Next Button Xpath" if next_page_id.active else "Disabled"
                        color_mode: "accent"
                        disabled: False if next_page_id.active else True
                BoxLayout: # link parameter Continuous page
                    size_hint_y:None
                    height: self.minimum_height
                    padding: (dp(20), 0)
                    MDCheckbox:
                        id: continuous_id
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        disabled: False if single_link_id.active else True
                    MDLabel:
                        size_hint_x: None
                        width: self.width
                        text: "Continuous (Single Page)"
                        theme_text_color: "Primary" if continuous_id.active else "Secondary"
                    MDTextField:
                        id: anchor_tag_xpath_id
                        hint_text: "Anchor Tag Xpath" if continuous_id.active else "Disabled"
                        color_mode: "accent"
                        disabled: False if continuous_id.active else True

                HSeparator:
                BoxLayout:
                    size_hint: None, None
                    height: dp(60)
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDCheckbox:
                        id: multi_link_id
                        group: "scrapy link"
                        size_hint: None, None
                        size: dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                    MDLabel:
                        text: "Multiple link"
                        size_hint: None, None
                        height: self.parent.height
                        width: self.width
                        theme_text_color: "Primary" if multi_link_id.active else "Secondary"

                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(5))
                    spacing: dp(40)
                    MDRaisedButton:
                        size_hint: None, None
                        height: self.height
                        width: self.width
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        text: "Import CSV"
                        disabled: False if multi_link_id.active else True
                        on_release: root.drivers.import_csv()
                    MDLabel:
                        id: import_csv_file_path_id
                        text: "File Path"
                        theme_text_color: "Primary" if multi_link_id.active else "Secondary"
                BoxLayout: # gap
                    size_hint_y: None
                    height: dp(30)

        BoxLayout: # scrap Field box
            size_hint_y: None
            height: self.minimum_height
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: self.parent.width, self.minimum_height
                padding: (dp(40), 0)
                MDLabel: # Title
                    size_hint_y: None
                    height: dp(30)
                    text:"What to Scrap"
                    theme_text_color: "Primary"
                    font_style: "Body2"
                    halign: "center"
                BoxLayout: # separator
                    padding: (dp(20), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:
                BoxLayout: # scrap field helper buttons
                    size_hint: None, None
                    height: self.minimum_height
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDIconButton:
                        icon: "plus"
                        on_release: root.drivers.add_new_field()
                BoxLayout: # separator
                    padding: (dp(20), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:
                BoxLayout: # here to add all the added field
                    id: scrap_field_box_id
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: "vertical"
                    spacing: dp(5)

                BoxLayout: # gap
                    size_hint_y: None
                    height: dp(30)

        BoxLayout: # Parameter box
            size_hint_y: None
            height: self.minimum_height
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: self.parent.width, self.minimum_height
                padding: (dp(40), 0)
                MDLabel: # Title
                    size_hint_y: None
                    height: dp(30)
                    text:"Generic Parameter"
                    theme_text_color: "Primary"
                    font_style: "Body2"
                    halign: "center"
                BoxLayout: # separator
                    padding: (dp(20), 0)
                    size_hint_y:None
                    height: self.minimum_height
                    HSeparator:

                BoxLayout: # timer
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(10))
                    spacing: dp(40)
                    MDLabel:
                        size_hint: None, None
                        height: self.height
                        width: self.width
                        text: "Time to wait between action"
                        halign: "right"
                        theme_text_color: "Primary"
                    MDSlider:
                        id: time_id
                        size_hint_y: None
                        height: self.height
                        min:0.1
                        max:10
                        value: 2.0
                        show_off: False
                    MDLabel:
                        size_hint: None, None
                        height: self.height
                        width: self.width
                        text: str(round(time_id.value, 1)) +" Seconds"
                        theme_text_color: "Primary"

                HSeparator:
                BoxLayout: # email check
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(10))
                    orientation: "vertical"
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        MDLabel:
                            size_hint_y: None
                            height: self.height
                            text: "Email Checker if any scrapping field named Email"
                            halign: "left"
                            theme_text_color: "Primary" if email_cheker_id.active else "Secondary"
                        BoxLayout: # gap
                            size_hint_y: None
                            height: self.minimum_height
                        MDSwitch:
                            id: email_cheker_id
                            size_hint: None, None
                            size: dp(36), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            _active: False
                HSeparator:
                BoxLayout: # user agent
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(10))
                    orientation: "vertical"
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        MDLabel:
                            size_hint_y: None
                            height: self.height
                            text: "Use user agent"
                            halign: "left"
                            theme_text_color: "Primary" if user_agent_id.active else "Secondary"
                        BoxLayout: # gap
                            size_hint_y: None
                            height: self.minimum_height
                        MDSwitch:
                            id: user_agent_id
                            size_hint: None, None
                            size: dp(36), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            _active: False
                HSeparator:
                BoxLayout: # missing link
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(10))
                    orientation: "vertical"
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(40)
                        MDLabel:
                            size_hint: None, None
                            height: self.height
                            width: self.width
                            text: "Fill missing link in href"
                            halign: "left"
                            theme_text_color: "Primary" if missing_link_id.active else "Secondary"
                        MDTextField:
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                            hint_text: "Domain Name" if missing_link_id.active else "Disabled"
                            color_mode: "accent"
                            disabled: False if missing_link_id.active else True
                        BoxLayout: # gap
                            size_hint: None, None
                            height: self.minimum_height
                            width: dp(40)
                        MDSwitch:
                            id: missing_link_id
                            size_hint: None, None
                            size: dp(36), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            _active: False
                HSeparator:
                BoxLayout: # string fix
                    size_hint_y: None
                    height: self.minimum_height
                    padding: (dp(20), dp(10))
                    orientation: "vertical"
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        MDLabel:
                            size_hint_y: None
                            height: self.height
                            text: "Fix text gap"
                            halign: "left"
                            theme_text_color: "Primary" if fix_text_id.active else "Secondary"
                        BoxLayout: # gap
                            size_hint_y: None
                            height: self.minimum_height
                        MDSwitch:
                            id: fix_text_id
                            size_hint: None, None
                            size: dp(36), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            _active: False
                HSeparator:
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(20)
                    MDCheckbox:
                        id: single_email_check_id
                        size_hint: None, None
                        size: dp(48), dp(48)
                        color: self.theme_cls.accent_color if self.active else self.theme_cls.secondary_text_color
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        active: False
                    MDLabel:
                        size_hint: None, None
                        height: self.height
                        width: self.width
                        text: "Check email Now"
                        theme_text_color: "Primary" if single_email_check_id.active else "Secondary"
                    MDTextField:
                        id: single_email_text_id
                        size_hint_y:None
                        height: self.height
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        hint_text: "Email address to check" if single_email_check_id.active else "Disabled"
                        disabled: False if single_email_check_id.active else True
                        color_mode: "accent"
                    MDRaisedButton:
                        id: email_check_btn_id
                        text: "Check"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        disabled: False if single_email_check_id.active else True
                        on_release: root.drivers.check_email(single_email_text_id.text)

        BoxLayout: # Buttons
            size_hint: None, None
            height: self.minimum_height
            width: self.minimum_width
            spacing: dp(20)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDRaisedButton:
                id: start_scrapping_btn_id
                text: "Start Scrapping"
                on_release: root.drivers.start_scrapping()
"""
mining_help_tab = """
<MiningHelpTab>:
    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        padding: "20dp"
        spacing: "5dp"
        Button:
            text: "Mining Help Tab"
"""

scrap_field_kv = """
<_ScrapField>:
    # size_hint_y: None
    # height: self.minimum_height
    # padding: (dp(20), dp(5))

    # MDCard:
    #     size_hint_y: None
    #     height: self.minimum_height
    #     padding: (dp(20), dp(5))
    #     spacing: dp(20)
    #     BoxLayout:
    #         size_hint_y: None
    #         height: self.minimum_height
    #         orientation: "vertical"
    #
    #         BoxLayout: # buttons helper
    #             size_hint: None, None
    #             height: self.minimum_height
    #             width: self.minimum_width
    #             pos_hint: {"center_x": 0.95, "center_y": 0.5}
    #             MDIconButton:
    #                 icon: "arrow-down-bold-hexagon-outline"
    #             MDIconButton:
    #                 icon: "delete"
    #
    #         MDTextField:
    #             hint_text: "Field Name"
    #             color_mode: "accent"
    #
    #         BoxLayout: # holder
    #             id: root.holder_id
    #             size_hint_y: None
    #             height: self.minimum_height
    #             orientation: "vertical"

"""


kv = scrap_field_kv+ mining_scrapy_tab_kv + mining_selenium_tab_kv + mining_help_tab
