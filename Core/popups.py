# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from os.path import expanduser

from kivy.clock import mainthread, Clock
from kivy.metrics import dp
from kivymd.dialog import MDDialog
from Core.xpop import XProgress, XFileOpen
import queue

class Popups:
    def __init__(self):
        self._q = queue.Queue()

    def pop_progress(self, title=None, text=None, max_value=None, cancel_callback=None,
                     complete_callback=None):
        progress_name = XProgress(title=title,text=text, max=max_value)
        progress_name.bind(on_dismiss=cancel_callback)
        return progress_name

    def test(self, progress_name, progress_text, pn_delta):
        self._q.put(self)
        while not self._q.empty():
            self._q.get()
            self.update_progress(progress_name, progress_text, pn_delta)
            # Clock.schedule_once(lambda dt: self.update_progress(progress_name, progress_text, pn_delta), .01)
            # when update call()
            # que it for execution
            # then pass it to mainthread to execute when one finished

    @mainthread
    def update_progress(self, progress_name, progress_text, pn_delta):

        if progress_name is not None:
            current_value = progress_name.value
            updated_value = current_value + pn_delta
            if progress_name.is_canceled():
                return
            # percentage = "{0: .0f} % ".format(1/self.total_progress_count * self.progress_bar.max)
            if progress_name.value < progress_name.max:
                if progress_name.value < updated_value:
                    progress_name.text = f"{progress_text} {int(current_value) + 1} %"
                    progress_name.inc()
                    increment = (updated_value-current_value)-1
                    # self.update_progress(progress_name, progress_text, increment)
                    Clock.schedule_once(lambda dt: self.update_progress(progress_name, progress_text, increment), .01)
                    print(progress_text)
                else:
                    return
            else:
                progress_name.complete()


    def pop_modal(self, size_hint_x=.9, size_hint_y=.9, height=200,
                  auto_dismiss=False, dialog_title="Title here",
                  title_align="left", title_colors=False,
                  buttons=None, final_button="Cancel", button_anchor_x="right",
                  content=None, custom_callback=None):
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
        if content is not None:
            _content = content
            _content.bind(texture_size=_content.setter('size'))
        self.dialog = MDDialog(title=dialog_title,
                               title_align=title_align,
                               content=content,
                               title_colors=title_colors,
                               size_hint=(size_hint_x, size_hint_y),
                               height=dp(height) if size_hint_y is None else dp(height),
                               button_anchor_x=button_anchor_x,
                               auto_dismiss=auto_dismiss)
        if buttons is not None:
            for btn, callbacks in buttons.items():
                self.dialog.add_action_button(str(btn),
                                              action=lambda *x: callbacks())
        if not auto_dismiss:
            self.dialog.add_action_button(final_button,
                                          action=lambda *x: dismissal(custom_callback))

        self.dialog.open()

        def dismissal(callback):
            if callback is not None:
                self.dialog.dismiss(callback())
            else:
                self.dialog.dismiss()

    def pop_open_file(self, import_callback):
        XFileOpen(on_dismiss=import_callback, path=expanduser(u'~'),
                      multiselect=False)
