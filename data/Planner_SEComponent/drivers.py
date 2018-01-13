from kivy.uix.button import Button


class PreferenceTabDrivers:
    def __init__(self, **kwargs):
        super(PreferenceTabDrivers, self).__init__()
        self.instance = kwargs.get("instance")

    def add(self):
        self.instance.ids.preference_id.add_widget(Button(text="New one"))