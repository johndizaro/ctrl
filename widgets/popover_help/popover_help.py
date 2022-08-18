import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk

class PopoverHelp:
    def __init__(self):

        pass
    def open(self,pai, mensagem=""):
        popover = Gtk.Popover()
        popover.set_parent(pai)
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        lb3 = Gtk.Label()
        lb3.set_xalign(0)
        lb3.get_style_context().add_class(class_name='caption-heading')
        lb3.set_markup(str=mensagem)
        vbox.append(child=lb3)
        popover.set_child(child=vbox)
        popover.show()
