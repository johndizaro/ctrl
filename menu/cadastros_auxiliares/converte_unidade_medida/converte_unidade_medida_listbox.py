import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw

Adw.init()


class ConverteUnidadeMedidaListBox():
    def __init__(self):
        pass

    def desenhar_listbox(self):
        vbox_listbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_listbox.get_style_context().add_class(class_name='card')

        scrolledwindow = Gtk.ScrolledWindow.new()
        scrolledwindow.set_propagate_natural_height(True)
        vbox_listbox.append(child=scrolledwindow)

        listbox = Gtk.ListBox.new()
        # Definindo o modo de seleção.
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        scrolledwindow.set_child(child=listbox)

        for n in range(1, 10):
            row = Gtk.ListBoxRow.new()
            row.set_selectable(selectable=False)

            vbox_card = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            vbox_card.get_style_context().add_class(class_name='card')
            row.set_child(child=vbox_card)

            label = Gtk.Label.new(str=f'Linha {n}')
            vbox_card.append(child=label)

            switch = Gtk.Switch.new()
            switch.set_margin_top(margin=6)
            switch.set_margin_end(margin=6)
            switch.set_margin_bottom(margin=6)
            switch.set_margin_start(margin=6)
            vbox_card.append(child=switch)

            listbox.append(child=row)

        # scrolledwindow.set_child(child=vbox_card)

        return vbox_listbox
