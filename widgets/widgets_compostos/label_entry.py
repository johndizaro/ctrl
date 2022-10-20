import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk


class LabelEntry():

    def __init__(self, **kwargs):
        self.margin_top = 10
        self.margin_end = 10
        self.margin_bottom = 10
        self.margin_start = 10


        self.tooltip_text = 'tooltip_text'

        self.label_title = 'label'
        self.e_max_length = 0
        self.e_default_text = ''
        self.e_hexpand = False

        self.e_entry = Gtk.Entry()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_e_entry_text(self,text=""):
        return  self.e_entry.set_text(text=text)
    # @property
    def get_e_entry_text(self):
        return self.e_entry.get_text()

    def setattr(self, key, value):
        # print(f"key:{key} - value:{value}")
        match key:
            case 'margin_top':
                self._validade_margin(key, value)
            case 'margin_end':
                self._validade_margin(key, value)
            case 'margin_bottom':
                self._validade_margin(key, value)
            case 'margin_start':
                self._validade_margin(key, value)
            case 'tooltip_text':
                self._validade_tooltip_text(key, value)
            case 'label_title':
                self._validade_label_title(key, value)
            case 'e_hexpand':
                self._validade_e_hexpand(key, value)
            case 'e_max_length':
                self._validade_e_max_length(key, value)
            case 'e_default_text':
                self._validade_e_default_text(key, value)
            case _:
                raise ValueError(f"key:{key} value:{value} Erro:{NotImplementedError}")

    def _validade_e_default_text(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = str(value)
        else:
            self.__dict__[key] = ""

    def _validade_e_hexpand(self, key, value):
        if value > 0:
            self.__dict__[key] = value

    def _validade_e_max_length(self, key, value):
        if value > 0:
            self.__dict__[key] = value

    def _validade_label_title(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = str(value)
        else:
            self.__dict__[key] = ""

    def _validade_tooltip_text(self, key, value):
        if len(str(value)) > 0:
            self.__dict__[key] = str(value)
        else:
            self.__dict__[key] = ""

    def _validade_margin(self, key, value):
        if not str(value).isnumeric():
            raise ValueError(f"key:{key} value:{value} Erro:{AttributeError}")
        if value >= 0:
            self.__dict__[key] = value
        else:
            self.__dict__[key] = 0

    @property
    def label_entry(self):

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_margin_top(margin=self.margin_top)
        vbox.set_margin_end(margin=self.margin_end)
        vbox.set_margin_bottom(margin=self.margin_bottom)
        vbox.set_margin_start(margin=self.margin_start)
        vbox.set_tooltip_text(self.tooltip_text)

        e_label = Gtk.Label(label=self.label_title,
                            tooltip_text=self.tooltip_text,
                            xalign=0,
                            yalign=0
                            )
        vbox.append(child=e_label)

        self.e_entry.set_max_length(self.e_max_length)
        self.e_entry.set_hexpand(expand=self.e_hexpand)
        self.e_entry.set_text(self.e_default_text)
        self.e_entry.set_tooltip_text(self.tooltip_text)

        vbox.append(child=self.e_entry)

        return vbox
