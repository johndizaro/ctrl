# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.MessageDialog()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class DialogError(Adw.MessageDialog):
    def __init__(self, parent):
        super(DialogError, self).__init__(transient_for=parent)

        self.set_heading(heading='Adw.MessageDialog() - heading')
        self.set_body(body='Adw.MessageDialog() - body')
        self.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancelar')
        self.add_response(Gtk.ResponseType.OK.value_nick, 'OK')
        self.connect('response', self.dialog_response)

        self.present()

    def dialog_response(self, dialog, response, ):
        if response == Gtk.ResponseType.OK.value_nick:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL.value_nick:
            print('Botão CANCELAR pressionado')