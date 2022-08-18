import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk


class DialogError(Gtk.Dialog):
    """Caixa de dialogo para mensagen de erro"""

    def __init__(self, parent, titulo, titulo_mensagem, mensagem):
        super(DialogError, self).__init__(transient_for=parent, use_header_bar=True)

        self.parent = parent

        self.set_title(title=titulo)
        # self.use_header_bar = True
        self.set_modal(modal=True)
        self.set_deletable(False)
        self.connect("response", self.dialog_response)

        self.titulo_mensagem = titulo_mensagem
        self.mensagem = mensagem

        self.add_buttons(
            '_OK', Gtk.ResponseType.OK)

        # Adicionando class action nos botões.
        btn_ok = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK)
        btn_ok.get_style_context().add_class(class_name='suggested-action')

        # Acessando o box do dialogo.
        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        content_area.set_spacing(spacing=12)
        content_area.set_margin_top(margin=12)
        content_area.set_margin_end(margin=12)
        content_area.set_margin_bottom(margin=12)
        content_area.set_margin_start(margin=12)

        lb1 = Gtk.Label.new()
        lb1.set_xalign(0)
        lb1.get_style_context().add_class(class_name='caption-heading')
        lb1.set_markup(str=self.titulo_mensagem.upper())
        lb1.set_margin_top(20)
        content_area.append(child=lb1)

        lb2 = Gtk.Label.new()
        lb2.set_xalign(0)
        lb2.get_style_context().add_class(class_name='caption')
        lb2.set_markup(str=self.mensagem)
        lb2.set_margin_top(20)
        lb2.set_margin_end(20)
        content_area.append(child=lb2)

        self.show()

    def dialog_response(self, widget, response):
        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
            # self.resposta = response
        widget.close()
