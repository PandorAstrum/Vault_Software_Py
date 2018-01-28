# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from os.path import expanduser

from kivy.clock import Clock, mainthread
from kivy.metrics import dp
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar

# notification
from bin.libPackage.xpop import XConfirmation
from bin.libPackage.xpop import XError
from bin.libPackage.xpop import XFileOpen
from bin.libPackage.xpop import XLoading
from bin.libPackage.xpop import XMessage
from bin.libPackage.xpop import XProgress


class Notify:
    pass
# snackbar
class Snacks:
    def snackbar(self, type="simple", msg="YourMessage"):
        if type == 'simple':
            Snackbar(text=msg).show()
        elif type == 'button':
            Snackbar(text=msg, button_text="with a button!", button_callback=lambda *args: 2).show()
        elif type == 'verylong':
            Snackbar(text=msg).show()
# xpop

class PopUp:
    def _xpop(self, sid, msg=None, title=None,
              on_dismiss_callback=None, check_callback=None,
              text=None, max_value=None, buttons=None, complete_callback=None, cancel_callback=None):
        if sid == 'msgbox':
            XMessage(text=msg, title=title, on_dismiss=on_dismiss_callback)
        elif sid == 'error':
            XError(text=msg)
        elif sid == 'confirm':
            XConfirmation(text='Do you see a confirmation?',
                          on_dismiss=on_dismiss_callback)
        elif sid == "fileOpen":
            XFileOpen(on_dismiss=on_dismiss_callback, path=expanduser(u'~'),
                      multiselect=False)
        elif sid == 'progress':
            self._o_popup = XProgress(title=title,
                                      text=text, max=max_value)

            def _progress(on_complete_callback=complete_callback, on_cancel_callback=cancel_callback, pdt=None):
                if self._o_popup.is_canceled():
                    if on_cancel_callback is not None:
                        on_cancel_callback()
                    return

                # self._o_popup.inc()
                self._o_popup.text = 'Processing (%d / %d)' % \
                                     (self._o_popup.value, self._o_popup.max)
                if self._o_popup.value < self._o_popup.max:
                    Clock.schedule_once(_progress, .01)
                else:
                    self._o_popup.complete(func=on_complete_callback)
            # XProgress(title=title, text=text, max=max_value)
            Clock.schedule_once(_progress, .1)
            return self._o_popup

        elif sid == "loading":
            XLoading(buttons=buttons)

    def add_md_dialogue(self, size_hint_x=.9, size_hint_y=.9, height=200,
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
