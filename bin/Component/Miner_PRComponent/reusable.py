# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
__map__ =
   -MDCard (card)
       -BoxLayout (card_inner_box)
           -BoxLayout (button_box)
               -MDCheckbox
               -MDLabel
               -MDIConButton
           -MDTextField (Field Name)

           -BoxLayout (tag_selector_box_holder)
               -BoxLayout (tag_selector_buttons_box)
                   -MDIconButton
                   -MDIconButton
               -BoxLayout (Separator)
                   -VSeparator
               -BoxLayout (tag_selector_box)
                   -BoxLayout (tag_box)
                       -MDTextField
                       -MDCheckbox
                       -MDLabel
                       -MDCheckbox
                       -MDLabel
                       -MDCheckbox
                       -MDLabel
                   -BoxLayout (selector_box)
                       -MDTextField
                       -MDCheckbox
                       -MDLabel
                       -MDCheckbox
                       -MDLabel
                       -MDCheckbox
                       -MDLabel
           -HSeparator
           -BoxLayout
               -MDLabel
               -MDCheckbox
               -MDLabel
               -MDCheckbox
               -MDLabel
               -MDCheckbox
               -MDLabel
"""
import utils

from Core.baseInterface import CustomLayout


class _TagSelectorField(CustomLayout):
    def __init__(self, scrap_field_instance, _group, **kwargs):
        super(_TagSelectorField, self).__init__(**kwargs)
        self.scrap_field_instance = scrap_field_instance
        self.tag_selector_holder = scrap_field_instance.tag_selector_box_holder
        self.parent_group = _group + "_parent_group"
        self.class_group = _group + "_class_group"
        self.tag_selector_box = self.add_BoxLayout("vertical")
        self.tag_selector_buttons_box = self.add_BoxLayout("vertical")
        self.add_new_tag_selector_field_btn = self.add_MDIconButton("arrow-down-bold-hexagon-outline")
        self.delete_tag_selector_field_btn = self.add_MDIconButton("delete")
        self.separator_box = self.add_BoxLayout()
        self.tag_box = self.add_BoxLayout()
        self.selector_box = self.add_BoxLayout()

        # tag_box.children
        self.tag_field = self.add_MDTextField("HTML tag", "accent")
        self.parent_lbl = self.add_MDLabel("Parent")
        self.parent_chk = self.add_MDCheckbox(self.parent_lbl, group=self.parent_group)
        self.sibling_lbl = self.add_MDLabel("Children")
        self.sibling_chk = self.add_MDCheckbox(self.sibling_lbl, group=self.parent_group)
        self.find_lbl = self.add_MDLabel("Find All")
        self.find_chk = self.add_MDCheckbox(self.find_lbl)

        # selector_box.children
        self.selector_field = self.add_MDTextField("selector", "accent")
        self.cls_lbl = self.add_MDLabel("class")
        self.cls_selector_chk = self.add_MDCheckbox(self.cls_lbl, self.class_group)
        self.id_selector_lbl = self.add_MDLabel("id")
        self.id_selector_chk = self.add_MDCheckbox(self.id_selector_lbl, self.class_group)
        self.str_selector_lbl = self.add_MDLabel("string")
        self.str_selector_chk = self.add_MDCheckbox(self.str_selector_lbl, self.class_group)

        self._make()
        self.scrap_field_instance.tag_selector_list.append(self)

    def _make(self):
        # button callback
        @utils.clocked()
        def add_tag_selector_field(instance):
            num = self.scrap_field_instance.getter_group + str(len(self.tag_selector_holder.children) + 1)
            self.tag_selector_holder.add_widget(_TagSelectorField(self.scrap_field_instance, num))
            self.add_new_tag_selector_field_btn.disabled = True

        @utils.clocked()
        def delete_tag_selector_field(instance):
            if len(self.tag_selector_holder.children) < 2:
                self.snackbar("simple", "Need atleast one field")
            else:
                self.tag_selector_holder.remove_widget(self)
                self.scrap_field_instance.tag_selector_list.remove(self)

        self.tag_selector_box.size_hint_y = None
        self.tag_selector_box.bind(minimum_height=self.tag_selector_box.setter("height"))

        self.tag_selector_buttons_box.size_hint = (None, None)
        self.tag_selector_buttons_box.bind(minimum_height=self.tag_selector_box.setter("height"),
                                           minimum_width=self.tag_selector_buttons_box.setter("width"))
        self.tag_selector_buttons_box.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.add_new_tag_selector_field_btn.bind(on_release=add_tag_selector_field)
        self.delete_tag_selector_field_btn.bind(on_release=delete_tag_selector_field)

        self.tag_selector_buttons_box.add_widget(self.add_new_tag_selector_field_btn)
        self.tag_selector_buttons_box.add_widget(self.delete_tag_selector_field_btn)

        self.separator_box.size_hint = (None, None)
        self.separator_box.bind(minimum_height=self.tag_selector_box.setter("height"),
                                minimum_width=self.separator_box.setter("width"))

        gap = self.add_gap(height_dp=None, width_dp=self.dp_single(20))

        v_separator = self.add_VSeparator()
        self.separator_box.add_widget(v_separator)

        self.tag_box.size_hint_y = None
        self.tag_box.bind(minimum_height=self.tag_box.setter("height"))

        self.tag_box.add_widget(self.tag_field)
        self.tag_box.add_widget(self.parent_chk)
        self.tag_box.add_widget(self.parent_lbl)
        self.tag_box.add_widget(self.sibling_chk)
        self.tag_box.add_widget(self.sibling_lbl)
        self.tag_box.add_widget(self.find_chk)
        self.tag_box.add_widget(self.find_lbl)

        self.selector_box.size_hint_y = None
        self.selector_box.bind(minimum_height=self.selector_box.setter("height"))

        self.selector_box.add_widget(self.selector_field)
        self.selector_box.add_widget(self.cls_selector_chk)
        self.selector_box.add_widget(self.cls_lbl)
        self.selector_box.add_widget(self.id_selector_chk)
        self.selector_box.add_widget(self.id_selector_lbl)
        self.selector_box.add_widget(self.str_selector_chk)
        self.selector_box.add_widget(self.str_selector_lbl)

        self.tag_selector_box.add_widget(self.tag_box)
        self.tag_selector_box.add_widget(self.selector_box)

        self.add_widget(self.tag_selector_buttons_box)
        self.add_widget(self.separator_box)
        self.add_widget(gap)
        self.add_widget(self.tag_selector_box)


class ScrapField(CustomLayout):
    def __init__(self, main_instance, getter_group, **kwargs):
        super(ScrapField, self).__init__(**kwargs)
        self.main_instance = main_instance
        self.scrap_field_holder_id = main_instance.scrap_field_box
        self.getter_group = getter_group + "_getter_group"
        self.top_group = getter_group + "_top_group"
        self.card = self.add_MDCard()
        self.card_inner_box = self.add_BoxLayout(orientation="vertical")
        self.card_inner_btn_box = self.add_BoxLayout()
        self.field_name = self.add_MDTextField("Custom Name", "accent")
        self.tag_selector_box_holder = self.add_BoxLayout("vertical")
        self.HSeparator = self.add_HSeparator()
        self.get_value_box = self.add_BoxLayout()

        self.mark_text_lbl = self.add_MDLabel("String")
        self.mark_text_chk = self.add_MDCheckbox(self.mark_text_lbl, self.top_group)
        self.mark_link_lbl = self.add_MDLabel("Link")
        self.mark_link_chk = self.add_MDCheckbox(self.mark_link_lbl, self.top_group)
        self.mark_email_lbl = self.add_MDLabel("Email")
        self.mark_email_chk = self.add_MDCheckbox(self.mark_email_lbl, self.top_group)
        self.delete_field_btn = self.add_MDIconButton("delete")

        self.get_lbl = self.add_MDLabel("Get")
        self.get_value_lbl = self.add_MDLabel("Value")
        self.get_value_chk = self.add_MDCheckbox(self.get_value_lbl, self.getter_group)
        self.get_href_lbl = self.add_MDLabel("href")
        self.get_href_chk = self.add_MDCheckbox(self.get_href_lbl, self.getter_group)
        self.get_str_lbl = self.add_MDLabel("text")
        self.get_str_chk = self.add_MDCheckbox(self.get_str_lbl, self.getter_group)
        self.get_title_lbl = self.add_MDLabel("title")
        self.get_title_chk = self.add_MDCheckbox(self.get_title_lbl, self.getter_group)
        self.get_src_lbl = self.add_MDLabel("src")
        self.get_src_chk = self.add_MDCheckbox(self.get_src_lbl, self.getter_group)
        self.tag_selector_list = []

        self._make()
        self.main_instance.field_instance.append(self)

    def _make(self):
        # Buttons callback
        @utils.clocked()
        def delete_button_callback(instance):
            if len(self.scrap_field_holder_id.children) < 2:
                self.snackbar("simple", "Need atleast one field")
            else:
                self.scrap_field_holder_id.remove_widget(self)
                self.main_instance.field_instance.remove(self)

        self.delete_field_btn.bind(on_release=delete_button_callback)

        self.card.size_hint_y = None
        self.card.bind(minimum_height=self.card.setter('height'))
        self.card.padding = self.dp_double(20, 5)
        self.card.spacing = self.dp_single(20)

        self.card_inner_box.size_hint_y = None
        self.card_inner_box.bind(minimum_height=self.card_inner_box.setter("height"))

        self.card_inner_btn_box.size_hint = (None, None)
        self.card_inner_btn_box.bind(minimum_height=self.card_inner_btn_box.setter("height"),
                                     minimum_width=self.card_inner_btn_box.setter("width"))
        self.card_inner_btn_box.pos_hint = {"right": 1, "center_y": 0.5}

        self.tag_selector_box_holder.size_hint_y = None
        self.tag_selector_box_holder.bind(minimum_height=self.tag_selector_box_holder.setter("height"))

        if len(self.tag_selector_box_holder.children) < 1:
            num = self.getter_group + "0"
            self.tag_selector_box_holder.add_widget(_TagSelectorField(self, num))

        self.get_value_box.size_hint_y = None
        self.get_value_box.bind(minimum_height=self.get_value_box.setter("height"))
        self.get_value_box.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.card_inner_btn_box.add_widget(self.mark_link_chk)
        self.card_inner_btn_box.add_widget(self.mark_link_lbl)
        self.card_inner_btn_box.add_widget(self.mark_text_chk)
        self.card_inner_btn_box.add_widget(self.mark_text_lbl)
        self.card_inner_btn_box.add_widget(self.mark_email_chk)
        self.card_inner_btn_box.add_widget(self.mark_email_lbl)
        self.card_inner_btn_box.add_widget(self.delete_field_btn)

        self.get_value_box.add_widget(self.get_lbl)
        self.get_value_box.add_widget(self.get_value_chk)
        self.get_value_box.add_widget(self.get_value_lbl)
        self.get_value_box.add_widget(self.get_href_chk)
        self.get_value_box.add_widget(self.get_href_lbl)
        self.get_value_box.add_widget(self.get_str_chk)
        self.get_value_box.add_widget(self.get_str_lbl)
        self.get_value_box.add_widget(self.get_title_chk)
        self.get_value_box.add_widget(self.get_title_lbl)
        self.get_value_box.add_widget(self.get_src_chk)
        self.get_value_box.add_widget(self.get_src_lbl)

        self.card_inner_box.add_widget(self.card_inner_btn_box)
        self.card_inner_box.add_widget(self.field_name)
        self.card_inner_box.add_widget(self.tag_selector_box_holder)
        self.card_inner_box.add_widget(self.HSeparator)
        self.card_inner_box.add_widget(self.get_value_box)
        self.card.add_widget(self.card_inner_box)
        self.add_widget(self.card)
