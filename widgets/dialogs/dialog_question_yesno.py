import gi
from gi.repository import Gtk, GLib

gi.require_version(namespace='Gtk', version='4.0')


# def retorna_valor(valor):
#     return valor

class DialogQuestionYesNo(Gtk.Dialog):

    def __init__(self, parent, titulo, titulo_mensagem, mensagem):
        super().__init__(transient_for=parent, use_header_bar=True)

        # self.parent = parent

        self.set_title(title=titulo)
        # self.use_header_bar = True
        self.set_modal(modal=True)
        self.set_deletable(False)
        self.set_resizable(False)
        self.connect("response", self.dialog_response)

        self._titulo_mensagem = titulo_mensagem
        self._mensagem = mensagem
        self.resposta = 0

        self.add_buttons(
            '_YES', Gtk.ResponseType.YES,
            '_NO', Gtk.ResponseType.NO)

        # Adicionando class action nos botões.
        btn_yes = self.get_widget_for_response(
            response_id=Gtk.ResponseType.YES)
        btn_yes.get_style_context().add_class(class_name='suggested-action')
        btn_no = self.get_widget_for_response(
            response_id=Gtk.ResponseType.NO)
        btn_no.get_style_context().add_class(class_name='destructive-action')

        # Acessando o box do dialogo.
        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.HORIZONTAL)
        content_area.set_valign(Gtk.Align.FILL)
        content_area.set_vexpand(True)
        content_area.set_spacing(spacing=10)
        content_area.set_margin_top(margin=10)
        content_area.set_margin_end(margin=10)
        content_area.set_margin_bottom(margin=10)
        content_area.set_margin_start(margin=10)
        content_area.set_halign(Gtk.Align.FILL)

        # vbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        # content_area.append(child=vbox)

        iconErro = Gtk.Image(icon_name="dialog-question", icon_size= Gtk.IconSize.LARGE)
        content_area.append(child=iconErro)

        # iconErro.set_from_icon_name("dialog-error")
        # iconErro.set_
        content_area.append(child=iconErro)

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
        vbox.append(child=lb2)

        self.show()

        self.loop = GLib.MainLoop.new(None, False)
        self.loop.run()

        # self.present()

    def get_resposta(self, valor):
        # print('dentro do get:' + str(valor))
        self.resposta = valor
        return valor

    def dialog_response(self, widget, response):

        if response == Gtk.ResponseType.YES:
            self.get_resposta(valor=Gtk.ResponseType.YES)
            self.resposta = Gtk.ResponseType.YES
            # print('Botão YES pressionado')
            # print("response:" + str(response))
        elif response == Gtk.ResponseType.NO:
            self.resposta = Gtk.ResponseType.NO
            self.get_resposta(valor=Gtk.ResponseType.NO)
            # print('Botão NO pressionado')
            # print("dialog_response -response:" + str(response))


        # widget.close()
        self.destroy()
        self.loop.quit()

        # return  self.get_resposta(valor=self.resposta)

        # print("oi")
