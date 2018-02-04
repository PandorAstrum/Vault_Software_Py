from kivy import metrics, kivy_data_dir

from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.widget import Widget

from kivy.properties import BooleanProperty, ListProperty, StringProperty,\
    NumericProperty, OptionProperty, ObjectProperty, BoundedNumericProperty,\
    DictProperty
from kivy.clock import Clock

from os.path import join
from os import path, makedirs

from Core.translator import gettext_ as _

__all__ = [
    "XNotification",
    "XMessage",
    "XError",
    "XConfirmation",
    "XProgress",
    "XLoading",
    "XSlider",
    "XTextInput",
    "XNotes",
    "XAuthorization",
    "XFileSave",
    "XFileOpen",
    "XFolder"
]


class XPopup(Popup):
    """
    XPopup class
    ============
    The :class:`XPopup` is the extension for the :class:`~kivy.uix.popup.Popup`
    class. Implements methods for limiting minimum size of the popup and fit popup
    to the app's window.

    By default, the minimum size is not set. It can be changed via setting value
    of an appropriate properties (see documentation below).

    .. warning::
    * Normalization is applied once (when using the :meth:`XPopup.open`)

    * The first normalization is performed on the minimum size, and then - fit
      to app's window. In this case, if the specified minimum size is greater
      than the size of the app's window - it will be ignored.


    Examples
    --------
    This example creates a simple popup with specified minimum size::

    popup = XPopup(size_hint=(.4, .3), min_width=400, min_height=300)
    popup.open()

    If actual size of popup less than minimum size, :attr:`size_hint` will be
    normalized. For example: assume the size of app window is 500x500, in this case
    popup will had size 200x150. But we set a minimum size, so :attr:`size_hint`
    for this popup will be recalculated and set to (.8, .6)

    By default, if you set the popup size in pixels, which will exceed the size
    of the app window, the popup will go out of app's window bounds.
    If you don't want that, you can set :attr:`fit_to_window` to True (popup will
    be normalized to the size of the app window)::

    popup = XPopup(size=(1000, 1000), size_hint=(None, None),
                   fit_to_window=True)
    popup.open()
    """

    min_width = NumericProperty(None, allownone=True)
    '''Minimum width of the popup.

    :attr:`min_width` is a :class:`~kivy.properties.NumericProperty` and
    defaults to None.
    '''

    min_height = NumericProperty(None, allownone=True)
    '''Minimum height of the popup.

    :attr:`min_height` is a :class:`~kivy.properties.NumericProperty` and
    defaults to None.
    '''

    fit_to_window = BooleanProperty(False)
    '''This property determines if the pop-up larger than app window is
    automatically fit to app window.

    :attr:`fit_to_window` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to False.
    '''

    def _norm_value(self, pn_value, pn_hint, pn_min, pn_max):
        """Normalizes one value

        :param pn_value: original value (width or height)
        :param pn_hint: original `size hint` (x or y)
        :param pn_min: minimum limit for the value
        :param pn_max: maximum limit for the value
        :return: tuple of normalized parameters (value, `size hint`)
        """
        norm_hint = pn_hint
        norm_value = pn_value

        if pn_min is not None and norm_value < pn_min:
            norm_value = pn_min
            norm_hint = pn_min / float(pn_max)

        if self.fit_to_window:
            if norm_value > pn_max:
                norm_value = pn_max
            if norm_hint is not None and norm_hint > 1:
                norm_hint = 1.

        return norm_value, norm_hint

    def _norm_size(self):
        """Applies the specified parameters
        """
        win_size = self.get_root_window().size[:]
        popup_size = self.size[:]

        norm_x = self._norm_value(popup_size[0], self.size_hint_x,
                                  self.min_width, win_size[0])
        norm_y = self._norm_value(popup_size[1], self.size_hint_y,
                                  self.min_height, win_size[1])
        self.width = norm_x[0]
        self.height = norm_y[0]
        self.size_hint = (norm_x[1], norm_y[1])

        # DON`T REMOVE OR FOUND AND FIX THE ISSUE
        # if `size_hint` is not specified we need to recalculate position
        # of the popup
        if (norm_x[1], norm_y[1]) == (None, None) and self.size != popup_size:
            self.property('size').dispatch(self)

    def open(self, *largs):
        super(XPopup, self).open(*largs)
        self._norm_size()


class XBase(XPopup):
    """
    XBase class
    ============
    Subclass of :class:`xpopup.XPopup`.
    Base class for all popup extensions. Don't use this class directly.

    Examples
    --------
    How to create your own class based on :class:`XBase`? It's easy!

    The content of the popup should be implemented in the :meth:`XBase._get_body`::

    class MyPopup(XBase):
        def _get_body(self):
            return Label(text='Hello World!')
    popup = MyPopup()

    By default, popup will automatically opened when the instance was created.
    If you don't want that, you can set :attr:`auto_open` to False::

    popup = MyPopup(auto_open=False)

    If you want to add buttons to the popup, just use :attr:`buttons`::

    popup = MyPopup(buttons=[MyPopup.BUTTON_OK, MyPopup.BUTTON_CANCEL])

    Pressing the button will trigger the 'dismiss' event. The button that was
    pressed, can be obtained from the :attr:`button_pressed`. You can use it
    in your callback::

    def my_callback(instance):
        print('Button "', instance.button_pressed, '" was pressed.')
    popup = MyPopup(auto_open=False, buttons=['Ok', 'Cancel'])
    popup.bind(on_dismiss=my_callback)
    popup.open()

    If you include a XBase.BUTTON_CANCEL in your set of buttons, then you can
    use :meth:`XBase.is_canceled` to check if it was pressed::

    def my_callback(instance):
        if instance.is_canceled():
            print('Popup was canceled.')
        else:
            print('Button "', instance.button_pressed, '" was pressed.')
    """

    auto_open = BooleanProperty(True)
    '''This property determines if the pop-up is automatically
    opened when the instance was created. Otherwise use :meth:`XBase.open`

    :attr:`auto_open` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to True.
    '''

    buttons = ListProperty()
    '''List of button names. Can be used when using custom button sets.

    :attr:`buttons` is a :class:`~kivy.properties.ListProperty` and defaults to
    [].
    '''

    button_pressed = StringProperty('')
    '''Name of button which has been pressed.

    :attr:`button_pressed` is a :class:`~kivy.properties.StringProperty` and
    defaults to '', read-only.
    '''

    size_hint_x = NumericProperty(.6, allownone=True)
    size_hint_y = NumericProperty(.3, allownone=True)
    auto_dismiss = BooleanProperty(False)
    '''Overrides properties from :class:`~kivy.uix.popup.Popup`
    '''

    min_width = NumericProperty(metrics.dp(300), allownone=True)
    min_height = NumericProperty(metrics.dp(150), allownone=True)
    fit_to_window = BooleanProperty(True)
    '''Overrides properties from :class:`XPopup`
    '''

    BUTTON_OK = _('Ok')
    BUTTON_CANCEL = _('Cancel')
    BUTTON_YES = _('Yes')
    BUTTON_NO = _('No')
    BUTTON_CLOSE = _('Close')
    '''Basic button names
    '''

    def __init__(self, **kwargs):
        # preventing change content of the popup
        kwargs.pop('content', None)
        self._pnl_buttons = None
        super(XBase, self).__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self._get_body())
        self._pnl_buttons = BoxLayout(size_hint_y=None)
        layout.add_widget(self._pnl_buttons)
        self.add_widget(layout)

        # creating buttons panel
        self.property('buttons').dispatch(self)

        if self.auto_open:
            self.open()

    def _on_click(self, instance):
        self.button_pressed = instance.id
        self.dismiss()

    def _get_body(self):
        """Returns the content of the popup. You need to implement
        this in your subclass.
        """
        raise NotImplementedError

    def on_buttons(self, instance, buttons):
        if self._pnl_buttons is None:
            return

        self._pnl_buttons.clear_widgets()
        if len(buttons) == 0:
            self._pnl_buttons.height = 0
            return

        self._pnl_buttons.height = metrics.dp(30)
        for button in buttons:
            self._pnl_buttons.add_widget(
                Factory.XButton(
                    text=button, id=button, on_release=self._on_click))

    def is_canceled(self):
        """Check the `cancel` event

        :return: True, if the button 'Cancel' has been pressed
        """
        return self.button_pressed == self.BUTTON_CANCEL


class XNotifyBase(XBase):
    """
    XNotifyBase class
    =================
    Subclass of :class:`xpopup.XBase`.
    The base class for all notifications. Also you can use this class to create
    your own notifications::

    XNotifyBase(title='You have a new message!', text='What can i do for you?',
                buttons=['Open it', 'Mark as read', 'Remind me later'])

    Or that way::

    class MyNotification(XNotifyBase):
        buttons = ListProperty(['Open it', 'Mark as read', 'Remind me later'])
        title = StringProperty('You have a new message!')
        text = StringProperty('What can i do for you?')
    popup = MyNotification()

    .. note:: :class:`XMessage` and :class:`XError` classes were created in a
    similar manner. Actually, it is just a subclasses with predefined default
    values.

    Similarly for the :class:`XConfirmation` class. The difference - it has
    :meth:`XConfirmation.is_confirmed` which checks which button has been
    pressed::

    def my_callback(instance):
        if instance.is_confirmed():
            print('You are agree')
        else:
            print('You are disagree')
    popup = XConfirmation(text='Do you agree?', on_dismiss=my_callback)

    Inherited on Classes
    ====================
    * XNotifyBase: Base class for all notifications.
    * XMessage: Notification with predefined button set (['Ok'])
    * XError: XMessage with predefined title
    * XConfirmation: Notification with predefined button set (['Yes', 'No'])
    * XNotification: Notification without buttons. Can autoclose after few seconds.
    * XProgress: Notification with ProgressBar
    """

    text = StringProperty('')
    '''This property represents text on the popup.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to
    ''.
    '''

    dont_show_text = StringProperty(_('Do not show this message again'))
    '''Use this property if you want to use custom text instead of
    'Do not show this message'.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`.
    '''

    dont_show_value = BooleanProperty(None, allownone=True)
    '''This property represents a state of checkbox 'Do not show this message'.
    To enable checkbox, set this property to True or False.

    .. versionadded:: 0.2.1

    :attr:`dont_show_value` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to None.
    '''

    def __init__(self, **kwargs):
        self._message = Factory.XLabel(text=self.text)
        self.bind(text=self._message.setter('text'))
        super(XNotifyBase, self).__init__(**kwargs)

    def _get_body(self):
        if self.dont_show_value is None:
            return self._message
        else:
            pnl = BoxLayout(orientation='vertical')
            pnl.add_widget(self._message)

            pnl_cbx = BoxLayout(
                size_hint_y=None, height=metrics.dp(35), spacing=5)
            cbx = CheckBox(
                active=self.dont_show_value, size_hint_x=None,
                width=metrics.dp(50))
            cbx.bind(active=self.setter('dont_show_value'))
            pnl_cbx.add_widget(cbx)
            pnl_cbx.add_widget(
                Factory.XLabel(text=self.dont_show_text, halign='left'))

            pnl.add_widget(pnl_cbx)
            return pnl


class XNotification(XNotifyBase):
    """
    XNotification class
    ===================
    Subclass of :class:`xpopup.XNotifyBase`.
    This is an extension of :class:`XNotifBase`. It has no buttons and can
    be closed automatically::

    XNotification(text='This popup will disappear after 3 seconds',
                  show_time=3)

    If you don't want that, you can ommit :attr:`XNotification.show_time` and
    use :meth:`XNotification.dismiss`::

    popup = XNotification(text='To close it, use the Force, Luke!')
    def close_popup():
        popup.dismiss()
    """

    show_time = BoundedNumericProperty(0, min=0, max=100, errorvalue=0)
    '''This property determines if the pop-up is automatically closed
    after `show_time` seconds. Otherwise use :meth:`XNotification.dismiss`

    :attr:`show_time` is a :class:`~kivy.properties.NumericProperty` and
    defaults to 0.
    '''

    def open(self, *largs):
        super(XNotification, self).open(*largs)
        if self.show_time > 0:
            Clock.schedule_once(self.dismiss, self.show_time)


class XMessage(XNotifyBase):
    """XMessageBox class. See module documentation for more information.
    """

    buttons = ListProperty([XNotifyBase.BUTTON_OK])
    '''Default button set for class
    '''


class XError(XMessage):
    """XErrorBox class. See module documentation for more information.
    """

    title = StringProperty(_('Something went wrong...'))
    '''Default title for class
    '''


class XConfirmation(XNotifyBase):
    """XConfirmation class. See module documentation for more information.
    """

    buttons = ListProperty([XNotifyBase.BUTTON_YES, XNotifyBase.BUTTON_NO])
    '''Default button set for class
    '''

    title = StringProperty(_('Confirmation'))
    '''Default title for class
    '''

    def is_confirmed(self):
        """Check the `Yes` event

        :return: True, if the button 'Yes' has been pressed
        """
        return self.button_pressed == self.BUTTON_YES


class XProgress(XNotifyBase):
    """
    XProgress class
    ===============
    Subclass of :class:`xpopup.XNotifyBase`.
    Represents :class:`~kivy.uix.progressbar.ProgressBar` in a popup. Properties
    :attr:`XProgress.value` and :attr:`XProgress.max` is binded to an
    appropriate properties of the :class:`~kivy.uix.progressbar.ProgressBar`.

    How to use it? Following example will create a `XProgress` object which has
    a title, a text message, and it displays 50% of progress::

    popup = XProgress(value=50, text='Request is being processed',
                      title='Please wait')

    There are two ways to update the progress line.
    First way: simply assign a value to indicate the current progress::

    # update progress to 80%
    popup.value = 80

    Second way: use :meth:`XProgress.inc`. This method will increase current
    progress by specified number of units::

    # reset progress
    popup.value = 0
    # increase by 10 units
    popup.inc(10)
    # increase by 1 unit
    popup.inc()

    By the way, if the result value exceeds the maximum value, this method is
    "looping" the progress. For example::

    # init progress
    popup = XProgress(value=50)
    # increase by 60 units - will display 10% of the progress
    popup.inc(60)

    This feature is useful when it is not known the total number of iterations.
    Also in this case, a useful method is :meth:`XProgress.complete`. It sets the
    progress to 100%, hides the button(s) and automatically closes the popup
    after 2 seconds::

    # init progress
    popup = XProgress(value=50)
    # complete the progress
    popup.complete()

.. versionadded:: 0.2.1
    You can change the text and time-to-close using following parameters::

        popup.complete(text='', show_time=0)

    In that case, the popup will be closed immediately.

.. versionadded:: 0.2.1
    :meth:`XProgress.autoprogress` starts infinite progress increase in the
    separate thread i.e. you don't need to increase it manually. Will be
    stopped automatically when the :meth:`XProgress.complete` or
    :meth:`XProgress.dismiss` is called.

    """

    buttons = ListProperty([XNotifyBase.BUTTON_CANCEL])
    '''Default button set for class
    '''

    max = NumericProperty(100.)
    value = NumericProperty(0.)
    '''Properties that are binded to the same ProgressBar properties.
    '''

    def __init__(self, **kwargs):
        self._complete = False
        self._progress = ProgressBar(max=self.max, value=self.value)
        self.bind(max=self._progress.setter('max'))
        self.bind(value=self._progress.setter('value'))
        super(XProgress, self).__init__(**kwargs)

    def _get_body(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(super(XProgress, self)._get_body())
        layout.add_widget(self._progress)
        return layout

    def complete(self, text=_('Complete'), show_time=2, func=None):
        """
        Sets the progress to 100%, hides the button(s) and automatically
        closes the popup.

        .. versionchanged:: 0.2.1
        Added parameters 'text' and 'show_time'

        :param text: text instead of 'Complete', optional
        :param show_time: time-to-close (in seconds), optional
        """
        self._complete = True
        n = self.max
        self.value = n
        self.text = text
        self.buttons = []
        if func is not None:
            func()
        Clock.schedule_once(self.dismiss, show_time)

    def inc(self, pn_delta=1):
        """
        Increase current progress by specified number of units.
         If the result value exceeds the maximum value, this method is
         "looping" the progress

        :param pn_delta: number of units
        """
        self.value += pn_delta
        if self.value > self.max:
            # create "loop"
            self.value = self.value % self.max

    def autoprogress(self, pdt=None):
        """
        .. versionadded:: 0.2.1

        Starts infinite progress increase in the separate thread
        """
        if self._window and not self._complete:
            self.inc()
            Clock.schedule_once(self.autoprogress, .01)


class XLoading(XBase):
    """
    XLoading class
    ===============
    Subclass of :class:`xpopup.XBase`.
    Shows a 'loading.gif' in the popup.

    Following example will create a `XLoading` object using custom title and
    image::

    popup = XLoading(title='Your_title', gif='/your_path_to/loading.gif')
    """
    gif = StringProperty(join(kivy_data_dir, 'images', 'image-loading.gif'))
    '''Represents a path to an image.
    '''

    title = StringProperty(_('Loading...'))
    '''Default title for class
    '''

    size_hint_x = NumericProperty(None, allownone=True)
    size_hint_y = NumericProperty(None, allownone=True)
    width = NumericProperty(metrics.dp(350))
    height = NumericProperty(metrics.dp(200))
    '''Default size properties for the popup
    '''

    def _get_body(self):
        return Image(source=self.gif, anim_delay=.1)


class XForm(XBase):
    """
    XForm class
    ===========
    Subclass of :class:`xpopup.XBase`.
    The base class for all the GUI forms. Also you can use this class to create
    your own forms. To do this you need to implement :meth:`XForm._get_form` in
    your subclass::

    class MyForm(XForm):
        def _get_form(self):
            layout = BoxLayout()
            layout.add_widget(Label(text='Show must go'))
            layout.add_widget(Switch(id='main_switch'))
            return layout

    popup = MyForm(title='Party switch')

    IMPORTANT: widgets, the values of which must be received after the close of
    the form, must have an "id" attribute (see an example above). Current version
    supports obtaining values of following widgets: TextInput, Switch, CheckBox,
    Slider.

    To obtain this values you need just use :meth:`XForm.get_value`::

    def my_callback(instance):
        print('Switch value: ' + str(instance.get_value('main_switch')))

    popup = MyForm(title='Party switch', on_dismiss=my_callback)

    If you omit an argument for the :meth:`XForm.get_value`, method returns
    a first value from the values dictionary. It is useful if the layout has only
    one widget.

    Another way to obtain values is :attr:`XForm.values`::

    def my_callback(instance):
        print('Values: ' + str(instance.values))

    popup = MyForm(title='Party switch', on_dismiss=my_callback)

    NOTE: The values are available only when the event `on_dismiss` was triggered.

    You can set list of the required fields using following parameter::

        popup = XForm(required_fields={
            'login': 'Login', 'password': 'Password'})

    Required fields checked when you press any button other than the "Cancel".

    Inherited on Classes
    ====================
    * XForm: Base class for all the GUI forms.
    * XSlider: Represents :class:`~kivy.uix.slider.Slider` in popup.
    * XTextInput: Represents a single line TextInput in popup.
    * XNotes: Represents a multiline TextInput in popup.
    * XAuthorization: Represents simple authorization form.
    """

    buttons = ListProperty([XBase.BUTTON_OK, XBase.BUTTON_CANCEL])
    '''List of button names. Can be used when using custom button sets.

    :attr:`buttons` is a :class:`~kivy.properties.ListProperty` and defaults to
    [Base.BUTTON_OK, Base.BUTTON_CANCEL].
    '''

    values = DictProperty({})
    '''Dict of pairs <widget_id>: <widget_value>. Use it to get the data from
    form fields. Supported widget classes: TextInput, Switch, CheckBox, Slider.

    :attr:`values` is a :class:`~kivy.properties.DictProperty` and defaults to
    {}, read-only.
    '''

    required_fields = DictProperty({})
    '''Dict of pairs <widget_id>: <widget_title>. Use it to set required fields
    in the form. If found blank widget with <widget_id>, its <widget_title>
    appears in the error message. Supported widget classes: TextInput.

    .. versionadded:: 0.2.3

    :attr:`values` is a :class:`~kivy.properties.DictProperty` and defaults to
    {}.
    '''

    def __init__(self, **kwargs):
        self._ui_form_container = BoxLayout()
        super(XForm, self).__init__(**kwargs)
        self._ui_form_container.add_widget(self._get_form())

    def _get_body(self):
        return self._ui_form_container

    def _on_click(self, instance):
        """Pre-dismiss method.
        Gathers widget values. Checks the required fields.
        Ignores it all if the "Cancel" was pressed.
        """
        if instance.id != self.BUTTON_CANCEL:
            self.values = {}
            required_errors = []
            for widget in self._ui_form_container.walk(restrict=True):
                t_id = widget.id
                if t_id is not None:
                    if isinstance(widget, TextInput):
                        t_value = widget.text
                        if self.required_fields and\
                                t_id in self.required_fields.keys()\
                                and not t_value:
                            required_errors.append(self.required_fields[t_id])
                    elif isinstance(widget, Switch)\
                            or isinstance(widget, CheckBox):
                        t_value = widget.active
                    elif isinstance(widget, Slider):
                        t_value = widget.value
                    else:
                        t_value = 'Not supported: ' + widget.__class__.__name__

                    self.values[t_id] = t_value

            if required_errors:
                XError(text=_('Following fields are required:\n') +
                       ', '.join(required_errors))
                return

        super(XForm, self)._on_click(instance)

    def _get_form(self):
        raise NotImplementedError

    def get_value(self, ps_id=''):
        """Obtain values from the widgets on the form.

        :param ps_id: widget id (optional)
            If omit, method returns a first value from the values dictionary
        :return: value of widget with specified id
        """
        assert len(self.values) > 0
        if ps_id == '':
            return self.values.get(list(self.values.keys())[0])
        else:
            return self.values.get(ps_id)


class XSlider(XForm):
    """
    XSlider class
    =============
    Subclass of :class:`xpopup.XForm`.
    Represents :class:`~kivy.uix.slider.Slider` in a popup. Properties
    :attr:`XSlider.value`, :attr:`XSlider.min`, :attr:`XSlider.max` and
    :attr:`XSlider.orientation` is binded to an appropriate properties of
    the :class:`~kivy.uix.progressbar.Slider`.

    Also :class:`xpopup.XSlider` has the event 'on_change'. You can bind
    your callback to respond on the slider's position change.

    Following example will create a :class:`xpopup.XSlider` object::

    def my_callback(instance, value):
        print('Current volume level: %0.2f' % value)

    popup = XSlider(title='Volume', on_change=my_callback)

    Another example you can see in the demo app module.

    You can display the slider's value in the title using following parameter::

        popup = XSlider(title_template='Volume: %0.2f', on_change=my_callback)

    NOTE: Be careful and use the only one formatting operator.

    :Events:
        `on_change`:
            Fired when the :attr:`~kivy.uix.slider.Slider.value` is changed.
    """
    __events__ = ('on_change', )

    buttons = ListProperty([XForm.BUTTON_CLOSE])
    '''Default button set for the popup
    '''

    min = NumericProperty(0.)
    max = NumericProperty(1.)
    value = NumericProperty(.5)
    orientation = OptionProperty(
        'horizontal', options=('vertical', 'horizontal'))
    '''Properties that are binded to the same slider properties.
    '''

    title_template = StringProperty('')
    '''Template for the formatted title. Use it if you want display the
    slider's value in the title. See module documentation for more information.

    .. versionadded:: 0.2.3

    :attr:`title_template` is a :class:`~kivy.properties.StringProperty` and
    defaults to ''.
    '''

    def __init__(self, **kwargs):
        super(XSlider, self).__init__(**kwargs)
        self._update_title()

    def _update_title(self):
        if self.title_template:
            self.title = self.title_template % self.value

    def _get_form(self):
        slider = Slider(id='value', min=self.min, max=self.max,
                        value=self.value, orientation=self.orientation)
        slider.bind(value=self.setter('value'))
        bind = self.bind
        bind(min=slider.setter('min'))
        bind(max=slider.setter('max'))
        bind(value=slider.setter('value'))
        bind(orientation=slider.setter('orientation'))
        return slider

    def on_value(self, instance, value):
        self._update_title()
        self.dispatch('on_change', value)

    def on_change(self, value):
        pass


class XTextInput(XForm):
    """
    XTextInput and XNotes classes
    =============================
    Subclasses of :class:`xpopup.XForm`.
    Both classes are represents :class:`~kivy.uix.textinput.TextInput` in a popup.
    The difference is that the class :class:`xpopup.XTextInput` is used to enter
    one text line, and the class :class:`xpopup.XNotes` - for multiline text.

    Following example will create a :class:`~kivy.uix.textinput.TextInput` object
    with the specified default text::

    def my_callback(instance):
        print('Your answer: ' + str(instance.get_value()))

    popup = XTextInput(title='What`s your mood?',
                       text='I`m in the excellent mood!',
                       on_dismiss=my_callback)

    NOTE: Pressing "Enter" key will simulate pressing "OK" on the popup. Valid for
    the :class:`xpopup.XTextInput` ONLY.

    :class:`xpopup.XNotes` allows you to specify a list of strings as the
    default value::

        def my_callback(instance):
            print('Edited text: ' + str(instance.lines))

        popup = XNotes(lines=['1st row', '2nd row', '3rd row'],
                       on_dismiss=my_callback)
    """

    text = StringProperty('')
    '''This property represents default text for the TextInput.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to
    ''.
    '''

    def _get_form(self):
        layout = BoxLayout(orientation='vertical', spacing=5)
        text_input = TextInput(id='text', multiline=False, text=self.text,
                               on_text_validate=self._on_text_validate,
                               # DON`T UNCOMMENT OR FOUND AND FIX THE ISSUE
                               # if `focus` set to `True` - TextInput will be
                               # inactive to edit
                               # focus=True,
                               size_hint_y=None, height=metrics.dp(33))
        layout.add_widget(Widget())
        layout.add_widget(text_input)
        layout.add_widget(Widget())
        return layout

    def _on_text_validate(self, instance):
        self._on_click(Button(id=self.BUTTON_OK))


class XNotes(XForm):
    """
    XTextInput and XNotes classes
    =============================
    Subclasses of :class:`xpopup.XForm`.
    Both classes are represents :class:`~kivy.uix.textinput.TextInput` in a popup.
    The difference is that the class :class:`xpopup.XTextInput` is used to enter
    one text line, and the class :class:`xpopup.XNotes` - for multiline text.

    Following example will create a :class:`~kivy.uix.textinput.TextInput` object
    with the specified default text::

    def my_callback(instance):
        print('Your answer: ' + str(instance.get_value()))

    popup = XTextInput(title='What`s your mood?',
                       text='I`m in the excellent mood!',
                       on_dismiss=my_callback)

    NOTE: Pressing "Enter" key will simulate pressing "OK" on the popup. Valid for
    the :class:`xpopup.XTextInput` ONLY.

    :class:`xpopup.XNotes` allows you to specify a list of strings as the
    default value::

        def my_callback(instance):
            print('Edited text: ' + str(instance.lines))

        popup = XNotes(lines=['1st row', '2nd row', '3rd row'],
                       on_dismiss=my_callback)
    """

    size_hint_x = NumericProperty(.9, allownone=True)
    size_hint_y = NumericProperty(.9, allownone=True)
    '''Default size properties for the popup
    '''

    text = StringProperty('')
    '''This property represents default text for the TextInput.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to
    ''.
    '''

    lines = ListProperty()
    '''This property represents default text for the TextInput as list of
    strings.

    .. versionadded:: 0.2.3

    :attr:`lines` is a :class:`~kivy.properties.ListProperty` and defaults to
    [].
    '''

    def _get_form(self):
        t = self.text
        if self.lines:
            t = '\n'.join(self.lines)
        return TextInput(id='text', text=t)

    def _on_click(self, instance):
        if instance.id != self.BUTTON_CANCEL:
            for widget in self._ui_form_container.walk(restrict=True):
                if widget.id == 'text':
                    self.lines = widget.text.split('\n')

        super(XForm, self)._on_click(instance)


class XAuthorization(XForm):
    """
    XAuthorization class
    ====================
    Subclass of :class:`xpopup.XForm`.
    This class is represents a simple authorization form.
    Use :attr:`xpopup.XAuthorization.login` and
    :attr:`xpopup.XAuthorization.password` to set default values for the login and
    password::

    def my_callback(instance):
        print('Auth values: ' + str(instance.values))

    XAuthorization(on_dismiss=my_callback, login='login', password='password')

    Also, you can set a default value for the checkbox "Login automatically" via
    :attr:`xpopup.XAuthorization.autologin`.

    Set :attr:`xpopup.XAuthorization.autologin` to None - checkbox will be
    hidden.

    To obtain the specific value, use following ids:

    * login -  TextInput for the login

    * password - TextInput for the password

    * autologin - checkbox "Login automatically"
    """
    BUTTON_LOGIN = _('Login')

    login = StringProperty(u'')
    '''This property represents default text in the `login` TextInput.
    For initialization only.

    :attr:`login` is a :class:`~kivy.properties.StringProperty` and defaults to
    ''.
    '''

    password = StringProperty(u'')
    '''This property represents default text in the `password` TextInput.
    For initialization only.

    :attr:`password` is a :class:`~kivy.properties.StringProperty` and defaults
    to ''.
    '''

    autologin = BooleanProperty(False, allownone=True)
    '''This property represents default value for the CheckBox
    "Login automatically". For initialization only.

    .. versionadded:: 0.2.3

        If None - checkbox is hidden.

    :attr:`autologin` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to False.
    '''

    title = StringProperty(_('Authorization'))
    '''Default title for the popup
    '''

    buttons = ListProperty([BUTTON_LOGIN, XForm.BUTTON_CANCEL])
    '''Default button set for the popup
    '''

    size_hint_x = NumericProperty(None, allownone=True)
    size_hint_y = NumericProperty(None, allownone=True)
    width = NumericProperty(metrics.dp(350))
    height = NumericProperty(metrics.dp(200))
    '''Default size properties for the popup
    '''

    def _get_form(self):
        layout = BoxLayout(orientation='vertical', spacing=5)
        layout.add_widget(Widget())

        pnl = BoxLayout(size_hint_y=None, height=metrics.dp(28), spacing=5)
        pnl.add_widget(
            Factory.XLabel(text=_('Login:'), halign='right',
                           size_hint_x=None, width=metrics.dp(80)))
        pnl.add_widget(TextInput(id='login', multiline=False,
                                 font_size=metrics.sp(14), text=self.login))
        layout.add_widget(pnl)

        pnl = BoxLayout(size_hint_y=None, height=metrics.dp(28), spacing=5)
        pnl.add_widget(
            Factory.XLabel(text=_('Password:'), halign='right',
                           size_hint_x=None, width=metrics.dp(80)))
        pnl.add_widget(TextInput(id='password', multiline=False, font_size=14,
                                 password=True, text=self.password))
        layout.add_widget(pnl)

        if self.autologin is not None:
            pnl = BoxLayout(size_hint_y=None, height=metrics.dp(28), spacing=5)
            pnl.add_widget(CheckBox(
                id='autologin', size_hint_x=None, width=metrics.dp(80),
                active=self.autologin))
            pnl.add_widget(
                Factory.XLabel(text=_('Login automatically'), halign='left'))
            layout.add_widget(pnl)

        layout.add_widget(Widget())
        return layout


class XFilePopup(XBase):
    """
    XFilePopup class
    ================
    Subclass of :class:`xpopup.XBase`.
    This class represents :class:`~kivy.uix.filechooser.FileChooser` in the
    popup with following features:

    * label which shows current path

    * buttons which allows you to select view mode (icon/list)

    * button `New folder`

    Usage example::

    popup = XFilePopup(title='XFilePopup demo', buttons=['Select', 'Close'])

    To set path on the filesystem that this controller should refer to, you can
    use :attr:`XFilePopup.path`. The same property you should use to get the
    selected path in your callback.

    By default it possible to select only one file. If you need to select multiple
    files, set :attr:`XFilePopup.multiselect` to True.

    By default it possible to select files only. If you need to select the
    files and folders, set :attr:`XFilePopup.dirselect` to True.

    To obtain selected files and/or folders you need just use
    :attr:`XFilePopup.selection`.

    You can add custom preview filters via :attr:`XFilePopup.filters`

    Following example shows how to use properties::

    def my_callback(instance):
        print(u'Path: ' + instance.path)
        print(u'Selection: ' + str(instance.selection))

    from os.path import expanduser
    popup = XFilePopup(title='XFilePopup demo', buttons=['Select', 'Close'],
                       path=expanduser(u'~'), on_dismiss=my_callback,
                       multiselect=True, dirselect=True)

    Inherited on Classes
    ====================
    * XFolder: :class:`XFilePopup` template for folder selection.
    * XFileOpen: :class:`XFilePopup` template for files selection.
    * XFileSave: :class:`XFilePopup` template for save file.
    """

    size_hint_x = NumericProperty(1., allownone=True)
    size_hint_y = NumericProperty(1., allownone=True)
    '''Default size properties for the popup
    '''

    browser = ObjectProperty(None)
    '''This property represents the FileChooser object. The property contains
    an object after creation :class:`xpopup.XFilePopup` object.
    '''

    path = StringProperty(u'/')
    '''Initial path for the browser.

    Binded to :attr:`~kivy.uix.filechooser.FileChooser.path`
    '''

    selection = ListProperty()
    '''Contains the selection in the browser.

    Binded to :attr:`~kivy.uix.filechooser.FileChooser.selection`
    '''

    multiselect = BooleanProperty(False)
    '''Binded to :attr:`~kivy.uix.filechooser.FileChooser.multiselect`
    '''

    dirselect = BooleanProperty(False)
    '''Binded to :attr:`~kivy.uix.filechooser.FileChooser.dirselect`
    '''

    filters = ListProperty()
    '''Binded to :attr:`~kivy.uix.filechooser.FileChooser.filters`
    '''

    CTRL_VIEW_ICON = 'icon'
    CTRL_VIEW_LIST = 'list'
    CTRL_NEW_FOLDER = 'new_folder'

    view_mode = OptionProperty(
        CTRL_VIEW_ICON, options=(CTRL_VIEW_ICON, CTRL_VIEW_LIST))
    '''Binded to :attr:`~kivy.uix.filechooser.FileChooser.view_mode`
    '''

    def _get_body(self):
        from kivy.lang import Builder
        import textwrap
        self.browser = Builder.load_string(textwrap.dedent('''\
        FileChooser:
            FileChooserIconLayout
            FileChooserListLayout
        '''))

        self.browser.path = self.path
        self.browser.multiselect = self.multiselect
        self.browser.dirselect = self.dirselect
        self.browser.filters = self.filters
        self.browser.bind(path=self.setter('path'),
                          selection=self.setter('selection'))
        self.bind(view_mode=self.browser.setter('view_mode'),
                  multiselect=self.browser.setter('multiselect'),
                  dirselect=self.browser.setter('dirselect'),
                  filters=self.browser.setter('filters'))

        lbl_path = Factory.XLabel(
            text=self.browser.path, valign='top', halign='left',
            size_hint_y=None, height=metrics.dp(25))
        self.browser.bind(path=lbl_path.setter('text'))

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self._ctrls_init())
        layout.add_widget(lbl_path)
        layout.add_widget(self.browser)
        return layout

    def _ctrls_init(self):
        pnl_controls = BoxLayout(size_hint_y=None, height=metrics.dp(25))
        pnl_controls.add_widget(Factory.XButton(
            text=_('Icons'), id=self.CTRL_VIEW_ICON,
            on_release=self._ctrls_click))
        pnl_controls.add_widget(Factory.XButton(
            text=_('List'), id=self.CTRL_VIEW_LIST,
            on_release=self._ctrls_click))
        pnl_controls.add_widget(Factory.XButton(
            text=_('New folder'), id=self.CTRL_NEW_FOLDER,
            on_release=self._ctrls_click))
        return pnl_controls

    def _ctrls_click(self, instance):
        if instance.id in self.property('view_mode').options:
            self.view_mode = instance.id
        elif instance.id == self.CTRL_NEW_FOLDER:
            XTextInput(title=_('Input folder name'),
                       text=_('New folder'),
                       on_dismiss=self._create_dir)

    def _create_dir(self, instance):
        """Callback for create a new folder.
        """
        if instance.is_canceled():
            return
        new_folder = self.path + path.sep + instance.get_value()
        if path.exists(new_folder):
            XError(text=_('Folder "%s" is already exist. Maybe you should '
                          'enter another name?') % instance.get_value())
            return True
        makedirs(new_folder)
        self.browser.property('path').dispatch(self.browser)

    def _filter_selection(self, folders=True, files=True):
        """Filter the list of selected objects

        :param folders: if True - folders will be included in selection
        :param files: if True - files will be included in selection
        """
        if folders and files:
            return

        t = []
        for entry in self.selection:
            if entry == '..' + path.sep:
                pass
            elif folders and self.browser.file_system.is_dir(entry):
                t.append(entry)
            elif files and not self.browser.file_system.is_dir(entry):
                t.append(entry)
        self.selection = t


class XFileSave(XFilePopup):
    """
    XFileSave class
    ===============
    Subclass of :class:`xpopup.XFilePopup`.
    This class is a template with predefined property values for entering name of
    file which will be saved.
    It contains the :class:`~kivy.uix.textinput.TextInput` widget for input
    filename.

    To set a default value in the TextInput widget, use :attr:`XFileSave.filename`.
    Also this property can be used to get the file name entered.

    To get full filename (including path), use :meth:`XFileSave.get_full_name`.

    Following example shows how to use properties::

    def my_callback(instance):
        print(u'Path: ' + instance.path)
        print(u'Filename: ' + instance.filename)
        print(u'Full name: ' + instance.get_full_name())

    popup = XFileSave(filename='file_to_save.txt', on_dismiss=my_callback)
    """

    BUTTON_SAVE = _('Save')
    TXT_ERROR_FILENAME = _('Maybe you should enter a filename?')

    filename = StringProperty(u'')
    '''Represents entered file name. Can be used for setting default value.
    '''

    title = StringProperty(_('Save file'))
    '''Default title for the popup
    '''

    buttons = ListProperty([BUTTON_SAVE, XFilePopup.BUTTON_CANCEL])
    '''Default button set for the popup
    '''

    def _get_body(self):
        txt = TextInput(id='filename', text=self.filename, multiline=False,
                        size_hint_y=None, height=metrics.dp(30))
        txt.bind(text=self.setter('filename'))
        self.bind(filename=txt.setter('text'))

        layout = super(XFileSave, self)._get_body()
        layout.add_widget(txt)
        return layout

    def on_selection(self, *largs):
        if len(self.selection) == 0:
            return

        if not self.browser.file_system.is_dir(self.selection[0]):
            self.filename = self.selection[0].split(path.sep)[-1]

    def dismiss(self, *largs, **kwargs):
        """Pre-validation before closing.
        """
        if self.button_pressed == self.BUTTON_SAVE:
            if self.filename == '':
                # must be entered filename
                XError(text=self.TXT_ERROR_FILENAME)
                return self

        return super(XFileSave, self).dismiss(*largs, **kwargs)

    def get_full_name(self):
        """Returns full filename (including path)
        """
        return self.path + path.sep + self.filename


class XFileOpen(XFilePopup):
    """
    XFileOpen class
    ===============
    Subclass of :class:`xpopup.XFilePopup`.
    This class is a template with predefined property values for selecting
    the files. He also checks the validity of the selected values. In this case,
    selection is allowed only files.
    """

    BUTTON_OPEN = _('Open')
    TXT_ERROR_SELECTION = _('Maybe you should select a file?')

    title = StringProperty(_('Open file'))
    '''Default title for the popup
    '''

    buttons = ListProperty([BUTTON_OPEN, XFilePopup.BUTTON_CANCEL])
    '''Default button set for the popup
    '''

    def dismiss(self, *largs, **kwargs):
        """Pre-validation before closing.
        """
        if self.button_pressed == self.BUTTON_OPEN:
            self._filter_selection(folders=False)
            if len(self.selection) == 0:
                # files must be selected
                XError(text=self.TXT_ERROR_SELECTION)
                return self
        return super(XFileOpen, self).dismiss(*largs, **kwargs)


class XFolder(XFilePopup):
    """
    XFolder class
    =============
    Subclass of :class:`xpopup.XFilePopup`.
    This class is a template with predefined property values for selecting
    the folders. He also checks the validity of the selected values. In this case,
    selection is allowed only folders.

    By default the folder selection is disabled. It means that the folder cannot be
    selected because it will be opened by one click on it. In this case the
    selected folder is equal to the current path.

    By the way, the folder selection is automatically enabled when you set
    :attr:`XFilePopup.multiselect` to True. But in this case the root folder
    cannot be selected.
    """

    BUTTON_SELECT = _('Select')
    TXT_ERROR_SELECTION = _('Maybe you should select a folders?')

    title = StringProperty(_('Choose folder'))
    '''Default title for the popup
    '''

    buttons = ListProperty([BUTTON_SELECT, XFilePopup.BUTTON_CANCEL])
    '''Default button set for the popup
    '''

    def __init__(self, **kwargs):
        super(XFolder, self).__init__(**kwargs)
        # enabling the folder selection if multiselect is allowed
        self.filters.append(self._is_dir)
        if self.multiselect:
            self.dirselect = True

    def _is_dir(self, directory, filename):
        return self.browser.file_system.is_dir(path.join(directory, filename))

    def dismiss(self, *largs, **kwargs):
        """Pre-validation before closing.
        """
        if self.button_pressed == self.BUTTON_SELECT:
            if not self.multiselect:
                # setting current path as a selection
                self.selection = [self.path]

            self._filter_selection(files=False)
            if len(self.selection) == 0:
                # folders must be selected
                XError(text=self.TXT_ERROR_SELECTION)
                return self
        return super(XFolder, self).dismiss(*largs, **kwargs)
