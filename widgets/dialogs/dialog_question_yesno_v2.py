import gi
from gi.repository import Gtk

gi.require_version(namespace='Gtk', version='4.0')


# def retorna_valor(valor):
#     return valor

class DialogQuestionYesNo(Gtk.Dialog):

    def __init__(self, parent, titulo, titulo_mensagem, mensagem):
        super().__init__(transient_for=parent, use_header_bar=True)

        self.parent = parent

        self.set_title(title=titulo)
        # self.use_header_bar = True
        self.set_modal(modal=True)
        self.set_deletable(False)
        self.connect("response", self.dialog_response)

        self.titulo_mensagem = titulo_mensagem
        self.mensagem = mensagem
        self.resposta1 = 0

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

        # self.present()

    def get_resposta1(self, valor):
        print('dentro do get:' + str(valor))
        self.resposta1 = valor
        return valor

    def dialog_response(self, widget, response):

        if response == Gtk.ResponseType.YES:
            self.get_resposta1(valor=Gtk.ResponseType.YES)
            self.resposta1 = Gtk.ResponseType.YES
            print('Botão YES pressionado')
            print("response:" + str(response))

        elif response == Gtk.ResponseType.NO:
            self.resposta1 = Gtk.ResponseType.NO
            self.get_resposta1(valor=Gtk.ResponseType.NO)
            print('Botão NO pressionado')
            print("dialog_response -response:" + str(response))

        # widget.close()
        self.destroy()
        # return  self.get_resposta1(valor=self.resposta1)

        # print("oi")
