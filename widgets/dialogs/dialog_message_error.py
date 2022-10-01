# dialog = Adw.MessageDialog.new(self._pai)

# g = Gtk.MessageDialog(
#     parent= self._pai,
#     # flags=Gtk.DialogFlags.MODAL,
#     transient_for=self._pai,
#     message_type=Gtk.MessageType.ERROR,
#     buttons=Gtk.ButtonsType.OK,
#     modal=True,
#     text=str(e),
#     secondary_text="johnn"
# )
# g.show()

import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk


class DialogMessageError():
    def __init__(self, parent, titulo, titulo_mensagem, mensagem):
        super(DialogMessageError, self).__init__()

        self.md = Gtk.MessageDialog(
            transient_for=parent,
            # flags = Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
            message_type=Gtk.MessageType.ERROR,
            # use_header_bar=True,
            # buttons= Gtk.ResponseType.OK,
            modal=True,
            destroy_with_parent=True,
            title=titulo,
            text=titulo_mensagem,
            secondary_text=mensagem
        )

        self.md.add_buttons(
            '_OK', Gtk.ResponseType.OK)

        btn_ok = self.md.get_widget_for_response(response_id=Gtk.ResponseType.OK)
        # btn_ok.get_style_context().add_class(class_name='suggested-action')
        Gtk.StyleContext.add_class(btn_ok.get_style_context(), "suggested-action")


        self.md.show()

        self.md.connect('response', self.dialog_response)

    def dialog_response(self, widget, response):
        # Verificando qual botão foi pressionado.
        # if response == Gtk.ResponseType.OK:
        #     print('Botão OK pressionado')
        # self.resposta = response
        widget.close()
