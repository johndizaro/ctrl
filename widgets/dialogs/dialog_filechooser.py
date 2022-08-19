import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk, Gio


class DialogFilechooser(Gtk.FileChooserDialog):
    def __init__(self, parent, titulo):
        super(DialogFilechooser, self).__init__(transient_for=parent, use_header_bar=True)

        self.parent = parent

        print('secundario')
        # fcd = Gtk.FileChooserDialog()
        self.set_title(title="pasta para log")
        self.set_modal(modal=True)
        # self.set_transient_for(parent=self)
        # self.set_current_folder(Gio.File.new_for_path(path=str(self.home)), )
        self.set_action(action=Gtk.FileChooserAction.SELECT_FOLDER)

        self.connect('response', self.dialog_response)

        self.resposta = 0
        self.caminho_selecionado = ""
        self.arquivo_selecionado = ""

        self.add_buttons(
            '_ACEITAR', Gtk.ResponseType.ACCEPT,
            '_CANCELAR', Gtk.ResponseType.CANCEL)

        # Adicionando class action nos botões.
        btn_accept = self.get_widget_for_response(
            response_id=Gtk.ResponseType.ACCEPT)
        btn_accept.get_style_context().add_class(class_name='suggested-action')

        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL)
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        self.show()

    def dialog_response(self, widget, response):

        caminho = self.get_file()
        self.arquivo_selecionado = caminho.get_basename()
        self.caminho_selecionado = caminho.get_path()

        if response == Gtk.ResponseType.ACCEPT:
            self.resposta = Gtk.ResponseType.ACCEPT
        elif response == Gtk.ResponseType.CANCEL:
            self.resposta = Gtk.ResponseType.CANCEL

        widget.close()
