# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivy.properties import BooleanProperty

__all__         = [
    "Table"
]
__author__      = "Ashiquzzaman Khan"
__copyright__   = "2018 GPL"
__desc__        = """ Table Widget. import class Table where to add table widget
                simply use below function pass id where to add table and list of data
                def add_table(self, id, table_dict):
                    id.add_widget(Table(table_content=table_dict))
                Dict example: {'head1':['content1'],'head2':['content2']},
                Variation: Table(table_content=table_dict,
                                fixed_width_header=True,
                                thead_align="center",
                                cell_align="left",
                                blank_cell_message="empty_cell")
                """


Builder.load_string('''
#:import MDLabel kivymd.label.MDLabel
<Table>
    do_scroll_y: False
    do_scroll_x: True
    # size_hint: (1, None)
    # height: table_layout_id.height
    BoxLayout:
        id: table_layout_id
        orientation:'vertical'
        size_hint_x: 1 if root.fixed_width_header else None
        width: header_container_id.width

        GridLayout:
            id: header_container_id
            spacing: dp(2)
            padding: [dp(10),dp(10),dp(10),dp(10)]
            size_hint_y: None
            height:dp(48)
            size_hint_x: 1 if root.fixed_width_header else None
            width: self.minimum_width

        ScrollView:
            size_hint_y:1
            do_scroll_y: True
            do_scroll_x: False
            GridLayout:
                id: cell_container_id
                spacing: dp(2)
                padding: [dp(10), dp(10), dp(10), dp(10)]
                size_hint_y: None
                height:self.minimum_height
                size_hint_x: 1 if root.fixed_width_header else None
                width: header_container_id.minimum_width

            #spacing:dp(2)


    # GridLayout:
    #     id:footer
    #     height:dp(48)
    #     pos_hint:{'center_y':0.1}

<Header>
    padding: [dp(10), dp(10), dp(10), dp(10)]
    canvas.before:
        Color:
            rgba: app.theme_cls.accent_dark
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: dp(48)
    size_hint_x: 1 if root.fixed_width else None
    width: self.minimum_width
    MDLabel:
        id: header_text_id
        text: root.text
        halign: root.align
        size_hint_x: 1 if root.fixed_width else None
        text_size: None, self.height
        width: self.texture_size[0]

<Cell>
    padding: [dp(10), dp(10), dp(10), dp(10)]
    canvas.before:
        Color:
            rgba: app.theme_cls.accent_color
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: dp(48)
    size_hint_x: 1 if root.fixed_width else None
    width: self.minimum_width
    ScrollView:
        MDLabel:
            id: cell_text_id
            text: root.text
            halign: root.align
            size_hint_x: None
            text_size: None, self.height
            width: self.texture_size[0]
''')


class Header(BoxLayout):
    text = StringProperty()
    align = StringProperty()
    fixed_width = BooleanProperty()


class Cell(BoxLayout):
    text = StringProperty()
    align = StringProperty()
    fixed_width = BooleanProperty()
    header_text = StringProperty("")


class Table(ScrollView):
    cols = NumericProperty(1)
    table_content = DictProperty({"Header 1": "row 11", "Header 2": "row 21"})
    thead = ListProperty()
    tbody = ListProperty()
    color = [128, 0, 2, 0.8]
    fixed_width_header = BooleanProperty(False)
    thead_align = StringProperty("center")
    cell_align = StringProperty("left")
    blank_cell_message = StringProperty("")

    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)

        self.thead = []
        for i in self.table_content.keys():
            self.thead.append(i)

        # header
        self.ids['header_container_id'].cols = len(self.thead)
        for i in self.thead:
            head = Header(text=i.upper(),
                          align=self.thead_align,
                          fixed_width=self.fixed_width_header)
            self.ids['header_container_id'].add_widget(head)

        # Cell
        self.ids['cell_container_id'].cols = len(self.thead)
        # find out the longest value
        max_key, max_value = max(self.table_content.items(), key=lambda x: len(set(x[1])))

        i = 0
        while i < len(max_value):
            for key in self.table_content.keys():
                try:
                    row = self.table_content[key][i]
                except IndexError:
                    row = self.blank_cell_message
                finally:
                    body = Cell(text=row,
                                align=self.cell_align,
                                fixed_width=self.fixed_width_header,
                                header_text=key)
                    self.ids['cell_container_id'].add_widget(body)
            i += 1
