# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
theme_text_color must be ['Primary', 'Secondary', 'Hint', 'Error', 'Custom', 'ContrastParentBackground']
"""
from os.path import expanduser

from kivy.clock import mainthread
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivymd.button import MDIconButton
from kivymd.card import MDCard
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.selectioncontrols import MDCheckbox
from kivymd.textfields import MDTextField
from kivymd.theming import ThemableBehavior
from Core import xpop
from Core.table import Table


class Spawn(ThemableBehavior):
    """
    Spawn class
    ===========
    The :class:`Spawn` is the extension for the :class:`~kivy.theming.ThemableBehavior`
    class. To enable all MD Class for usage on other class.. Any class inherited from
    Spawn class will be able to call any MD class as a function

    Usage
    =====
    class MyClass(Spawn):
        self.add_md_label()

    """
    def __init__(self, **kwargs):
        super(Spawn, self).__init__(**kwargs)

    def add_grid_layout(self):
        grd_lt = GridLayout()
        return grd_lt
    # md modal

    def add_modal_dialog(self, dialog_title="test", title_align="left", title_colors=False,
                         size_hint_x=.9, size_hint_y=.9, height=200, auto_dismiss=False,
                         content=None, content_table=False,
                         button_anchor_x="right",
                         buttons="default",
                         default_callback=None):
        def _on_dismiss(dismiss_callback):
            if dismiss_callback is not None:
                self.d.dismiss(dismiss_callback())
            else:
                self.d.dismiss()

        if content is not None:
            # content.bind(texture_size=content.setter("size"))
            # _content = content
            # _content.bind(texture_size=_content.setter('size'))
            self.d = MDDialog(title=dialog_title, title_align=title_align, title_colors=title_colors,
                          size_hint=(size_hint_x, size_hint_y),
                          height=dp(height) if size_hint_y is None else dp(height),
                          auto_dismiss=auto_dismiss,
                          content=content, content_table=content_table,
                          button_anchor_x=button_anchor_x)

        if not auto_dismiss:
            if buttons == "default":
                self.d.add_action_button("Okay", action=lambda *x: _on_dismiss(default_callback))
            # else:
            #     for btn in buttons.keys():
            #         self.d.add_action_button(btn, action=lambda *x: self.d.dismiss(buttons[btn]()))
        return self.d

    def add_table(self, table_content=None, fixed_width_header=True, cell_align="center", blank_cell_message=""):
        if table_content is not None:
            t = Table(table_content=table_content,
                      fixed_width_header=fixed_width_header,
                      cell_align=cell_align,
                      blank_cell_message=blank_cell_message)
            return t

    def show_pop_modal(self, size_hint_x=.9,
                       size_hint_y=.9, height=200,
                       auto_dismiss=False, dialog_title="Title here",
                       title_align="left", title_colors=False,
                       buttons="default",
                       button_anchor_x="right", content=None,
                       dismiss_callback=None):
        """

        :param size_hint_x:
        :param size_hint_y:
        :param height:
        :param auto_dismiss:
        :param dialog_title:
        :param title_align:
        :param title_colors:
        :param buttons:
        :param final_button:
        :param button_anchor_x:
        :param content:
        :param custom_callback:
        :return:
        """
        def _on_dismiss(dismiss_callback):
            if dismiss_callback is not None:
                self.dialog.dismiss(dismiss_callback())
            else:
                self.dialog.dismiss()

        if content is not None:
            _content = content
            _content.bind(texture_size=_content.setter('size'))
        self.dialog = MDDialog(title=dialog_title,
                               title_align=title_align,
                               content=_content,
                               title_colors=title_colors,
                               size_hint=(size_hint_x, size_hint_y),
                               height=dp(height) if size_hint_y is None else dp(height),
                               button_anchor_x=button_anchor_x,
                               auto_dismiss=auto_dismiss)

        if not auto_dismiss:
            if buttons == "default":
                self.dialog.add_action_button("Okay",
                                              action=lambda *x: _on_dismiss(dismiss_callback))
            else:
                for btn in buttons.keys():
                    # print
                    func = buttons[btn]
                    # func()
                    self.dialog.add_action_button(btn,
                                                  action=lambda *x: self.dialog.dismiss(func()))


        self.dialog.open()

    # add xpop up
    def add_pop_notification(self):
        pass
    def add_pop_message(self):
        pass
    def add_pop_error(self):
        pass
    def add_pop_confirmation(self):
        pass
    def add_pop_progress(self):
        pass
    def add_pop_loading(self):
        pass
    def add_pop_slider(self):
        pass
    def add_text_input(self):
        pass
    def add_notes(self):
        pass
    def add_pop_authorization(self):
        pass
    def add_pop_filesave(self):
        pass

    def show_pop_fileopen(self, on_dismiss_callback=None,
                          path=expanduser(u'~'),
                          multiselect=False):
        """
        show the pop up for file open and calls callback on dismiss
        :param on_dismiss_callback: default callback when the pop up dismissed
        :param path: path to open by default
        :param multiselect: boolean if multi select enabled or not
        :return:
        """
        xpop.XFileOpen(on_dismiss=on_dismiss_callback,
                       path=path,
                       multiselect=multiselect)

    def add_md_label(self, font_style="Body1",
                     theme_text_color="Secondary",
                     text="msg here", size_hint_y=None,
                     halign="left", valign="center", auto_size=False):
        lbl = MDLabel(font_style=font_style,
                      theme_text_color=theme_text_color,
                      text=text, size_hint_y=size_hint_y,
                      halign=halign, valign=valign)
        if auto_size:
            lbl.bind(texture_size=lbl.setter("size"))
        return lbl

    def add_MDCard(self):
        return MDCard()

    def add_BoxLayout(self, orientation= "horizontal"):
        box = BoxLayout()
        box.orientation = orientation
        return box

    def dp_double(self, first_value, second_value):
        return (dp(first_value), dp(second_value))

    def dp_single(self, value):
        return dp(value)

    def add_MDCheckbox(self, lbl_association=None, group=None):
        def _change(instance):
            if chk.active:
                chk.color = self.theme_cls.accent_color
                if lbl_association != None:
                    lbl_association.theme_text_color = "Primary"
            else:
                chk.color = self.theme_cls.secondary_text_color
                if lbl_association != None:
                    lbl_association.theme_text_color = "Secondary"

        chk = MDCheckbox()
        chk.size_hint = (None, None)
        chk.size = (dp(48), dp(48))
        chk.pos_hint= {'center_x': 0.5, 'center_y': 0.5}
        chk.bind(on_release=_change)
        chk.color =  self.theme_cls.secondary_text_color
        if lbl_association != None:
            lbl_association.theme_text_color = "Secondary"
        if group !=None:
            chk.group = group
        return chk

    def add_MDLabel(self, text, width=None):
        lbl = MDLabel()
        lbl.size_hint_x= None
        lbl.bind(width=lbl.setter("width"))
        lbl.text= text
        lbl.theme_text_color = "Primary"
        if width is not None:
            lbl.width = dp(width)
        return lbl

    def add_MDIconButton(self, icon_name):
        md_icon_btn = MDIconButton()
        md_icon_btn.icon = icon_name
        return md_icon_btn

    def add_MDTextField(self, hint_text, color_mode):
        md_text_field = MDTextField()
        md_text_field.hint_text = hint_text
        md_text_field.color_mode = color_mode
        return md_text_field

    def add_HSeparator(self):
        return HSeparator()

    def add_VSeparator(self):
        return VSeparator()

    def add_gap(self, height_dp, width_dp):
        return Gap(height_dp= height_dp, width_dp= width_dp)


class Separator(Widget):
    pass

class HSeparator(Separator):
    pass

class VSeparator(Separator):
    pass

class Gap(BoxLayout):
    height_dp = ObjectProperty(None, allownone=True)
    width_dp = ObjectProperty(None, allownone=True)
    def __init__(self, **kwargs):
        super(Gap, self).__init__(**kwargs)