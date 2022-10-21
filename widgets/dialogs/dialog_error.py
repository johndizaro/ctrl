import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk


class DialogError(Gtk.Dialog):
    """
    Caixa de dialogo para mensagen de erro
    Exemplo:
            from widgets.dialogs.dialog_error import DialogError\n
            ...\n
            DialogError(parent=self,titulo="Título",titulo_mensagem="Mensagem de titulo",mensagem="Mensagem de error")
    """

    def __init__(self, parent, titulo, titulo_mensagem, mensagem):
        super(DialogError, self).__init__(transient_for=parent, use_header_bar=True)

        # self.parent = parent
        # self.set_transient_for(parent)
        # self.set_keep_above(True)

        self.set_title(title=titulo)
        # self.use_header_bar = True
        self.set_modal(modal=True)
        self.set_deletable(False)
        self.set_resizable(False)
        self.connect("response", self.dialog_response)

        self._titulo_mensagem = titulo_mensagem
        self._mensagem = mensagem

        self.add_buttons(
            '_OK', Gtk.ResponseType.OK)

        # Adicionando class action nos botões.
        btn_ok = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK)
        btn_ok.get_style_context().add_class(class_name='destructive-action')

        # Acessando o box do dialogo.
        content_area = self.get_content_area()
        #
        content_area.set_orientation(orientation=Gtk.Orientation.HORIZONTAL)
        content_area.set_valign(Gtk.Align.FILL)
        content_area.set_vexpand(True)
        content_area.set_spacing(spacing=10)
        content_area.set_margin_top(margin=10)
        content_area.set_margin_end(margin=10)
        content_area.set_margin_bottom(margin=10)
        content_area.set_margin_start(margin=10)
        content_area.set_halign(Gtk.Align.FILL)

        # iconErro = Gtk.Image(icon_name="dialog-error", pixel_size=100)
        iconErro = Gtk.Image(icon_name="dialog-error-symbolic", icon_size= Gtk.IconSize.LARGE)
        content_area.append(child=iconErro)

        # iconErro.set_from_icon_name("dialog-error")

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_valign(Gtk.Align.CENTER)
        content_area.append(child=vbox)

        lb1 = Gtk.Label.new()
        lb1.set_xalign(0)
        lb1.get_style_context().add_class(class_name='heading')
        lb1.set_markup(str=self._titulo_mensagem.upper())
        # lb1.set_margin_top(20)
        vbox.append(child=lb1)

        lb2 = Gtk.Label.new()
        lb2.set_wrap(True)
        lb2.set_justify(Gtk.Justification.FILL)
        lb2.set_max_width_chars(50)
        lb2.set_wrap_mode(Gtk.WrapMode.WORD)
        # lb2.set_justify(Gtk.Justification.FILL)
        # lb2.set_wrap(True)
        lb2.set_xalign(0)
        lb2.get_style_context().add_class(class_name='body')
        lb2.set_markup(str=self._mensagem)
        # lb2.set_margin_top(20)
        # lb2.set_margin_end(20)
        vbox.append(child=lb2)

        self.show()

    def dialog_response(self, widget, response):
        # Verificando qual botão foi pressionado.
        # if response == Gtk.ResponseType.OK:
        #     print('Botão OK pressionado')
            # self.resposta = response
        widget.close()
