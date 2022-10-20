import gi

from db.infa_dataclass.mysql.engines.engine_converte_unidade_medida import EngineConverteUnidadeMedida
from db.infa_dataclass.mysql.engines.engine_unidade_medida import EngineUnidadeMedida
from db.infa_dataclass.mysql.extras.operacao_aritimetica import lst_dic_operacao_aritimetica
from db.infa_dataclass.mysql.models.model_converte_unidade_medida import ModelConverteUnidadeMedida
from db.infa_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida
from geral.geral import Geral
from widgets.dialogs.dialog_message_error import DialogMessageError
from widgets.widgets_compostos.label_dropdown import LabelDropdown
from widgets.widgets_compostos.label_entry import LabelEntry

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw

Adw.init()


class ConverteUnidadeMedidaScreen(Gtk.ApplicationWindow):
    def __init__(self, pai):
        super(ConverteUnidadeMedidaScreen, self).__init__()

        self._pai = pai
        self._gr = Geral()

        self._m_a01 = ModelUnidadeMedida()
        self._e_a01 = EngineUnidadeMedida()
        self._m_a02 = ModelConverteUnidadeMedida()
        self._e_a02 = EngineConverteUnidadeMedida()

        self._lst_dic_unidade_medida = self._e_a01.select_all()

        self._criar_layout_janela(layout_janela=self)
        # self.ler_dados_para_treeview()

    def ler_dados_para_treeview(self):

        try:
            self._lst_dic_converte_unidade_medida = self._e_a02.select_all()
            print(f"self._lst_dic_converte_unidade_medida:{self._lst_dic_converte_unidade_medida}")
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            DialogMessageError(parent=self._pai, titulo='Problema ao carregar Unidade de Medida',
                               titulo_mensagem='Problemas ao executar select_all()',
                               mensagem=f'{e}')
        else:
            self._criar_layout_janela(layout_janela=self)

        # self._dic_a02_registro = dict()
        # self._lst_dic_a02_registro = []

    def _criar_layout_janela(self, layout_janela):

        layout_janela.set_title(title="Conversão de Medidas")
        layout_janela.set_default_size(width=-1, height=400)
        layout_janela._montagem_headerbar(layout_janela=layout_janela)

        layout_janela.set_destroy_with_parent(setting=True)

        layout_janela.set_transient_for(parent=self._pai)
        layout_janela.set_resizable(resizable=True)

        layout_janela.set_child(self._distribuir_layout())

        layout_janela.present()

    def _montagem_headerbar(self, layout_janela):
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        Gtk.StyleContext.add_class(headerbar.get_style_context(), "headerbar")
        layout_janela.set_titlebar(titlebar=headerbar)

        bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        bt_salvar.get_style_context().add_class(class_name='suggested-action')
        bt_salvar.set_tooltip_text(text="Salvar alterações no banco de dados")
        bt_salvar.connect('clicked', self.on_bt_salvar_clicked)
        headerbar.pack_start(child=bt_salvar)

        bt_undor = Gtk.Button.new_with_label(label='Limpar Tela')
        bt_undor.set_icon_name(icon_name='edit-clear-all-symbolic')
        bt_undor.get_style_context().add_class(class_name='plain')
        bt_undor.set_tooltip_text(text="Restaurar apelas a tela")
        # bt_undor.connect('clicked', self.on_bt_undor_clicked)
        headerbar.pack_start(child=bt_undor)

        bt_apagar = Gtk.Button.new_with_label(label='Apagar')
        bt_apagar.set_icon_name(icon_name='edit-delete-symbolic')
        bt_apagar.get_style_context().add_class(class_name='destructive-action')
        bt_apagar.set_tooltip_text(text="Apagar do banco de dados")
        bt_apagar.connect('clicked', self.on_bt_apagar_clicked)
        headerbar.pack_start(child=bt_apagar)

        bt_ajudar = Gtk.Button.new_with_label(label='Ajudar')
        bt_ajudar.set_icon_name(icon_name='help-browser-symbolic')
        bt_ajudar.get_style_context().add_class(class_name='')
        bt_ajudar.set_tooltip_text(text="Uma preve explicação sobre a tela")
        # bt_ajudar.connect('clicked', self.on_bt_ajudar_clicked)
        headerbar.pack_end(child=bt_ajudar)

        # return headerbar

    def _distribuir_layout(self):

        vbox_layout = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_layout.set_margin_top(margin=10)
        vbox_layout.set_margin_end(margin=10)
        vbox_layout.set_margin_bottom(margin=10)
        vbox_layout.set_margin_start(margin=10)
        vbox_layout.set_valign(Gtk.Align.FILL)
        vbox_layout.set_halign(Gtk.Align.FILL)

        vbox_layout.append(child=self._desenhar_campos())
        return vbox_layout

    def _desenhar_campos(self):
        vbox_campos = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0, )
        vbox_campos.get_style_context().add_class(class_name='card')

        self._ld_a02_id_sigla_origem = LabelDropdown(campo_para_incluir='a01_descricao',
                                                     campo_chave='a01_id',
                                                     lst_dic_registros=self._lst_dic_unidade_medida,
                                                     title=self._m_a02.get_title('a02_id_sigla_origem'),
                                                     tooltip_text=self._m_a02.get_description('a02_id_sigla_origem'))
        vbox_campos.append(child=self._ld_a02_id_sigla_origem.label_dropdown)

        self._ld_a02_id_sigla_destino = LabelDropdown(campo_para_incluir='a01_descricao',
                                                      campo_chave='a1_id',
                                                      lst_dic_registros=self._lst_dic_unidade_medida,
                                                      title=self._m_a02.get_title('a02_id_sigla_destino'),
                                                      tooltip_text=self._m_a02.get_description('a02_id_sigla_destino'))
        vbox_campos.append(child=self._ld_a02_id_sigla_destino.label_dropdown)

        vbox_campos1 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        vbox_campos1.set_homogeneous(True)
        vbox_campos.append(child=vbox_campos1)

        self._ld_a02_tp_operacao = LabelDropdown(campo_para_incluir='operacao',
                                                 campo_chave='simbolo',
                                                 lst_dic_registros=lst_dic_operacao_aritimetica,
                                                 title=self._m_a02.get_title('a02_tp_operacao'),
                                                 tooltip_text=self._m_a02.get_description('a02_tp_operacao'))
        vbox_campos1.append(child=self._ld_a02_tp_operacao.label_dropdown)

        self._le_a02_razao = LabelEntry(label_title=self._m_a02.get_title('a02_razao'),
                                        tooltip_text=self._m_a02.get_description('a02_razao'),
                                        e_max_length=self._m_a02.get_size('a02_razao'),
                                        e_hexpand=False,
                                        margin_top=10,
                                        margin_bottom=10,
                                        margin_start=0,
                                        margin_end=10)
        vbox_campos1.append(child=self._le_a02_razao.label_entry)

        vbox_campos2 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        # vbox_campos2.set_margin_top(margin=10)
        # vbox_campos2.set_margin_end(margin=10)
        # vbox_campos2.set_margin_bottom(margin=10)
        # vbox_campos2.set_margin_start(margin=10)
        # vbox_campos2.get_style_context().add_class(class_name='card')
        # vbox_campos.append(child=vbox_campos2)

        frame_teste = Gtk.Frame.new(label='Forneça um valor para testar sua converção este teste não será salvo')
        frame_teste.get_style_context().add_class(class_name='caption-heading')
        frame_teste.set_margin_top(margin=10)
        frame_teste.set_margin_end(margin=10)
        frame_teste.set_margin_bottom(margin=10)
        frame_teste.set_margin_start(margin=10)
        frame_teste.set_child(vbox_campos2)
        vbox_campos.append(child=frame_teste)

        self._le_valor_para_convercao = LabelEntry(label_title="Valor para converção",
                                                   tooltip_text="Forneça um valor para testar",
                                                   e_hexpand=False,
                                                   e_max_length=10,
                                                   margin_top=10,
                                                   margin_bottom=10,
                                                   margin_start=10,
                                                   margin_end=10
                                                   )
        vbox_campos2.append(child=self._le_valor_para_convercao.label_entry)

        self.bt_calcular = Gtk.Button.new()
        self.bt_calcular.set_icon_name(icon_name='accessories-calculator-symbolic')
        self.bt_calcular.get_style_context().add_class(class_name='AdwButtonContent')
        self.bt_calcular.set_tooltip_text(text='Calcular a converção para verificação')
        self.bt_calcular.set_margin_bottom(10)
        self.bt_calcular.set_valign(Gtk.Align.END)
        self.bt_calcular.connect('clicked', self.on_bt_calcular_clicked)
        vbox_campos2.append(child=self.bt_calcular)

        self.l_label1 = Gtk.Label(label='100')
        self.l_label1.get_style_context().add_class(class_name='title-4')
        self.l_label1.get_style_context().add_class(class_name='accent')
        self.l_label1.set_margin_bottom(10)
        self.l_label1.set_margin_start(10)
        self.l_label1.set_hexpand(True)
        self.l_label1.set_valign(Gtk.Align.END)
        vbox_campos2.append(child=self.l_label1)

        return vbox_campos

    def on_selected_item(self, widget):
        pass

        print('liliana')

    def on_bt_apagar_clicked(self, widget):
        pass

    def on_bt_calcular_clicked(self, widget):
        pass

    def on_bt_salvar_clicked(self, widget):

        if self.validar_campos():
            if self._m_a02.a02_id == 0:
                print("incluir")
                # self._e_a02.incluir(dicionario=asdict(self._m_a02))
            else:
                print('alteração')
            self.limpar_campos()
        else:
            print('problemas')

    def limpar_campos(self):

        self._le_a02_razao.set_e_entry_text("")

    def validar_campos(self):

        try:

            self._m_a02.a02_id_sigla_origem = self._ld_a02_id_sigla_origem.return_selected_data(field_name='a01_id')
            self._m_a02.a02_id_sigla_destino = self._ld_a02_id_sigla_destino.return_selected_data(field_name='a01_id')
            self._m_a02.a02_tp_operacao = self._ld_a02_tp_operacao.return_selected_data(field_name='simbolo')
            self._m_a02.a02_razao = self._le_a02_razao.get_e_entry_text()


        except Exception as error:

            DialogMessageError(parent=self,
                               titulo="Erro",
                               titulo_mensagem="Campo com conteúdo inválido",
                               mensagem=error)

        return self._m_a02.verifica_status_final()


class ConverteUnidadeMedida(ConverteUnidadeMedidaScreen):
    def __init__(self, pai):
        super(ConverteUnidadeMedida, self).__init__(pai)
        self._pai = pai

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ConverteUnidadeMedida(pai=self._pai)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)
