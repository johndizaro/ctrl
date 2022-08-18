import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk


class PopoverHelp:
    def __init__(self):
        pass

    def open(self, pai, message=""):
        popover = Gtk.Popover()
        popover.set_parent(pai)
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        lb_menssagem = Gtk.Label()
        lb_menssagem.set_xalign(0)
        lb_menssagem.get_style_context().add_class(class_name='caption-heading')
        lb_menssagem.set_markup(str=message)
        vbox.append(child=lb_menssagem)
        popover.set_child(child=vbox)
        popover.show()
