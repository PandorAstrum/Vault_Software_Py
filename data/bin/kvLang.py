
default_layout = '''
#: import icon data.lib.iconfonts.icon
#:import C kivy.utils.get_color_from_hex
#:import Toolbar kivymd.toolbar.Toolbar

# Main Root
<RootWidget>:
    orientation: "vertical"
    on_size: print(self.size)

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
                id: action_group_id
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

#    Main screen Manager ---------------------------------------------------------------------------
    RelativeLayout:
        id: main_screen_manager_id
        canvas:
            Color:
                rgb: C('#AAAAAA')
            Rectangle:
                pos: self.pos
                size: self.size

#        pos_hint: {'bottom':1}
#        size_hint: 1, 0.9
'''