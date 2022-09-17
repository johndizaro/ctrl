from config.data_config_novo import DataConfig
from config.config_sistema import ConfigSistema
from geral.geral import Geral
from widgets.dialogs.dialog_filechooser import DialogFilechooser
from widgets.popover_help.popover_help import PopoverHelp

import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk


class ConfigSistemaScreen(Gtk.ApplicationWindow):

    def __init__(self, pai):
        super(ConfigSistemaScreen, self).__init__()

        self._pai = pai
        self._gr = Geral()
        self._gr.meu_logger.info(f"{self.__class__.__name__} - gr.log_dic:{self._gr.log_dic}")

        self._dc = DataConfig()

        # self._gr.salva_dic_log(self._dc.traz_dicionario_log())

        self._montagem_janela()
        self._colocar_dados_tela()

    def _colocar_dados_tela(self):

        if 'log_no_terminal' in self._gr.log_dic.keys():
            self._cb_log_terminal.set_active(self._gr.log_dic['log_no_terminal'])
        else:
            self._cb_log_terminal.set_active(self._dc.log_no_terminal)

        if 'log_no_arquivo' in self._gr.log_dic.keys():
            self._cb_log_arquivo.set_active(self._gr.log_dic['log_no_arquivo'])
        else:
            self._cb_log_arquivo.set_active(self._dc.log_no_arquivo)

        if 'log_caminho_arquivo' in self._gr.log_dic.keys():
            self._e_log_caminho_arquivo.set_text(self._gr.log_dic['log_caminho_arquivo'])
        else:
            self._e_log_caminho_arquivo.set_text(self._dc.log_caminho_arquivo)

        if 'log_nome_arquivo' in self._gr.log_dic.keys():
            self._e_log_nome_arquivo.set_text(self._gr.log_dic['log_nome_arquivo'])
        else:
            self._e_log_nome_arquivo.set_text(self._dc.log_nome_arquivo)

        if 'log_tipo' in self._gr.log_dic.keys():
            log_tipo = self._gr.log_dic['log_tipo']
        else:
            log_tipo = self._dc.log_tipo

        match log_tipo:
            case 'INFO':
                self._tb_log_info.set_active(is_active=True)
            case 'DEBUG':
                self._tb_log_debug.set_active(is_active=True)
            case 'WARNING':
                self._tb_log_warning.set_active(is_active=True)
            case 'ERROR':
                self._tb_log_error.set_active(is_active=True)
            case 'CRITICAL':
                self._tb_log_critical.set_active(is_active=True)

    def _montagem_janela(self):
        self._gr.meu_logger.info("inicio")
        self.set_title(title="Configuração")
        self._montagem_headerbar()

        # self.set_decorated(setting=True)
        # self.set_modal(modal=True)
        self.set_destroy_with_parent(setting=True)
        self.set_transient_for(parent=self._pai)
        self.set_resizable(resizable=False)
        self._montar_layout()

        self.present()

    def _montagem_headerbar(self):
        # self.a.info("Montagem do header do menu principal")
        self._gr.meu_logger.info("inicio")
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        bt_salvar.get_style_context().add_class(class_name='destructive')
        bt_salvar.set_tooltip_text(text="Salvar alterações")
        bt_salvar.connect('clicked', self.on_bt_salvar_clicked)
        headerbar.pack_start(child=bt_salvar)

        bt_undor = Gtk.Button.new_with_label(label='Desfazer')
        bt_undor.set_icon_name(icon_name='edit-undo')
        bt_undor.get_style_context().add_class(class_name='suggested-action')
        bt_undor.set_tooltip_text(text="Restaurar configuração na tela")
        bt_undor.connect('clicked', self.on_bt_undor_clicked)
        headerbar.pack_start(child=bt_undor)

        bt_ajudar = Gtk.Button.new_with_label(label='Ajudar')
        bt_ajudar.set_icon_name(icon_name='help-browser-symbolic')
        bt_ajudar.get_style_context().add_class(class_name='')
        bt_ajudar.set_tooltip_text(text="Uma preve explicação sobre a tela")
        bt_ajudar.connect('clicked', self.on_bt_ajudar_clicked)
        headerbar.pack_end(child=bt_ajudar)

        return headerbar

    def on_bt_undor_clicked(self, widget):
        self._colocar_dados_tela()

    def _limpar_tela(self):
        self._cb_log_terminal.set_active(True)
        self._cb_log_arquivo.set_active(True)
        self._e_log_caminho_arquivo.set_text("")
        self._e_log_nome_arquivo.set_text("")
        self._tb_log_error.set_active(True)

    def on_bt_salvar_clicked(self, widget):

        campos_validados_log_dic = self.validar_campos_log()
        if not len(campos_validados_log_dic) == 0:
            self._salvar_dados(campos_validados_dic=campos_validados_log_dic)

            self._gr.salva_dic_log(log_dic=campos_validados_log_dic)

            self._limpar_tela()
            DialogInformativ(parent=self, titulo="Config.ini", titulo_mensagem="Gravação feita com sucesso",
                             mensagem="Todas as informações estão ok")
        else:
            DialogInformativ(parent=self, titulo="Config.ini", titulo_mensagem="Gravação não realizada",
                             mensagem="Verifique os campos e tente de novo")

    def _salvar_dados(self, campos_validados_dic):

        cs = ConfigSistema()

        self._gr.meu_logger.info(f"loop para gravar dados do campos_validados_dic:{campos_validados_dic}")
        for key, item in campos_validados_dic.items():
            self._gr.meu_logger.info(f"indo gravar secao=LOG opcao={key},valor={item}")
            cs.gravar_option(secao="LOG", opcao=key, valor=str(item))

    def validar_campos_log(self):
        """
        valida os campos se tudo estiver correto retornará um dicionario
        com os dados caso contrario retornará um dicionario vazio
        :return: dictionary
        """
        campos_ok = True

        self._dc.log_no_terminal = self._cb_log_terminal.get_active()
        self._dc.log_no_arquivo = self._cb_log_terminal.get_active()

        try:
            self._dc.log_caminho_arquivo = str(self._e_log_caminho_arquivo.get_text())
            self._l_log_caminho_arquivo.get_style_context().remove_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='error')
        except ValueError:
            self._l_log_caminho_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='regular')
            campos_ok = False

        try:
            self._dc.log_nome_arquivo = str(self._e_log_caminho_arquivo.get_text())
            self._l_log_nome_arquivo.get_style_context().remove_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='error')
        except ValueError:
            self._l_log_nome_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='regular')
            campos_ok = False

        if self._tb_log_info.get_active():
            self._dc.log_tipo = str("INFO")
        elif self._tb_log_debug.get_active():
            self._dc.log_tipo = str("DEBUG")
        elif self._tb_log_error.get_active():
            self._dc.log_tipo = str("ERROR")
        elif self._tb_log_warning.get_active():
            self._dc.log_tipo = str("WARNING")
        elif self._tb_log_critical.get_active():
            self._dc.log_tipo = str("CRITICAL")

        self._gr.meu_logger.info(f"Terminei - campos_validados_log_dic:{campos_validados_log_dic}")

        if not campos_ok:
            return self._dc.traz_dicionario_log()

    def on_bt_ajudar_clicked(self, widget):
        message = "Altera as configurações do sistema"
        PopoverHelp.open(self, pai=widget, message=message)

    def _montar_layout(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(margin=10)
        vbox.set_margin_end(margin=10)
        vbox.set_margin_bottom(margin=10)
        vbox.set_margin_start(margin=10)
        vbox.set_valign(Gtk.Align.CENTER)

        vbox.append(child=self._montar_campos())

        self.set_child(child=vbox)

    def _log_handler(self):
        vbox_lh = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        self._cb_log_terminal = Gtk.CheckButton.new_with_label(label=self._dc.get_log_no_terminal_title())
        self._cb_log_terminal.set_active(setting=True)
        vbox_lh.append(child=self._cb_log_terminal)

        self._cb_log_arquivo = Gtk.CheckButton.new_with_label(label=self._dc.get_log_no_arquivo_title())
        self._cb_log_arquivo.set_active(setting=True)
        vbox_lh.append(child=self._cb_log_arquivo)
        return vbox_lh

    def _log_options(self):
        hboxf1 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hboxf1.set_homogeneous(True)
        hboxf1.get_style_context().add_class(class_name='linked')
        hboxf1.set_margin_top(margin=12)
        hboxf1.set_margin_end(margin=12)
        hboxf1.set_margin_bottom(margin=12)
        hboxf1.set_margin_start(margin=12)

        self._tb_log_debug = Gtk.ToggleButton.new_with_label(label="Debug")
        # self._tb_log_debug.set_group(self._tb_log_debug)
        self._tb_log_debug.set_active(is_active=False)
        hboxf1.append(child=self._tb_log_debug)

        self._tb_log_info = Gtk.ToggleButton.new_with_label(label="Info")
        self._tb_log_info.set_group(self._tb_log_debug)
        self._tb_log_info.set_active(is_active=True)
        hboxf1.append(child=self._tb_log_info)

        self._tb_log_warning = Gtk.ToggleButton.new_with_label(label="Warning")
        self._tb_log_warning.set_group(self._tb_log_debug)
        self._tb_log_warning.set_active(is_active=False)
        hboxf1.append(child=self._tb_log_warning)

        self._tb_log_error = Gtk.ToggleButton.new_with_label(label="Error")
        self._tb_log_error.set_group(self._tb_log_debug)
        self._tb_log_error.set_active(is_active=False)
        hboxf1.append(child=self._tb_log_error)

        self._tb_log_critical = Gtk.ToggleButton.new_with_label(label="Critical")
        self._tb_log_critical.set_group(self._tb_log_debug)
        self._tb_log_critical.set_active(is_active=False)
        hboxf1.append(child=self._tb_log_critical)

        frame1 = Gtk.Frame.new(label="Opções de log")
        frame1.set_child(hboxf1)
        return frame1

    def _log_entries(self):
        vboxf1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vboxf1.get_style_context().add_class(class_name='card')

        # lbe_log_caminho = Gtk.Label.new()
        # lbe_log_caminho.set_margin_top(margin=12)
        # lbe_log_caminho.set_margin_end(margin=12)
        # lbe_log_caminho.set_margin_start(margin=12)
        # lbe_log_caminho.set_xalign(0)
        # lbe_log_caminho.get_style_context().add_class(class_name='caption')
        # # lbe_log_caminho.get_style_context().add_class(class_name='linked')
        # # lbe_log_caminho.set_markup(str="Caminho para guardar os arquivos de logs")
        # lbe_log_caminho.set_markup(str=self._dc.get_log_caminho_title())
        # vboxf1.append(child=lbe_log_caminho)
        #
        # self._e_log_caminho_arquivo = Gtk.Entry.new()
        # self._e_log_caminho_arquivo.set_margin_end(margin=12)
        # self._e_log_caminho_arquivo.set_margin_start(margin=12)
        # self._e_log_caminho_arquivo.set_text(text='')
        # self._e_log_caminho_arquivo.get_style_context().add_class(class_name='regular')
        # self._e_log_caminho_arquivo.set_icon_from_icon_name(
        #     icon_pos=Gtk.EntryIconPosition.SECONDARY,
        #     icon_name='system-search-symbolic',
        # )
        # self._e_log_caminho_arquivo.connect('icon-press', self.on_e_log_caminho_arquivo_icon_press)
        # vboxf1.append(child=self._e_log_caminho_arquivo)

        self._l_log_caminho_arquivo = Gtk.Label(label=self._dc.get_log_caminho_arquivo_title(),
                                                margin_top=10,
                                                margin_end=10,
                                                margin_start=10,
                                                xalign=0)
        self._l_log_caminho_arquivo.get_style_context().add_class(class_name='caption')
        self._l_log_caminho_arquivo.get_style_context().add_class(class_name='accent')
        vboxf1.append(child=self._l_log_caminho_arquivo)

        self._e_log_caminho_arquivo = Gtk.Entry(max_length=0,
                                                text="",
                                                tooltip_text=self._dc.get_log_caminho_arquivo_description(),
                                                margin_start=10,
                                                margin_end=10,
                                                margin_top=10,
                                                margin_bottom=10)
        self._e_log_caminho_arquivo.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        self._e_log_caminho_arquivo.connect('icon-press', self.on_e_log_caminho_arquivo_icon_press)
        vboxf1.append(child=self._e_log_caminho_arquivo)

        self._l_log_nome_arquivo = Gtk.Label(label=self._dc.get_log_nome_arquivo_title(),
                                             margin_top=10,
                                             margin_end=10,
                                             margin_start=10,
                                             xalign=0)
        self._l_log_nome_arquivo.get_style_context().add_class(class_name='caption')
        self._l_log_nome_arquivo.get_style_context().add_class(class_name='accent')
        vboxf1.append(child=self._l_log_nome_arquivo)

        self._e_log_nome_arquivo = Gtk.Entry(max_length=self._dc.get_log_nome_arquivo_field_size(),
                                             text="",
                                             tooltip_text=self._dc.get_log_nome_arquivo_description(),
                                             margin_start=10,
                                             margin_end=10,
                                             margin_top=10,
                                             margin_bottom=10)
        vboxf1.append(child=self._e_log_nome_arquivo)

        return vboxf1

    def on_e_log_caminho_arquivo_icon_press(self, Entry, EntryIconPosition):
        # print(f'Valor digitado no entry: {Entry.get_text()}')
        if EntryIconPosition == Gtk.EntryIconPosition.SECONDARY:
            self._dfc = DialogFilechooser(parent=self, titulo="Caminho para o Log")
            self._dfc.connect('response', self.on_resposta_dialogfilechooser)
        # elif EntryIconPosition == Gtk.EntryIconPosition.PRIMARY:
        #     print("primario")

    def on_resposta_dialogfilechooser(self, widget, response_id):
        if self._dfc.caminho_selecionado:
            caminho_selecionado = self._dfc.caminho_selecionado
        else:
            caminho_selecionado = ""
        self._e_log_caminho_arquivo.set_text(caminho_selecionado)

    def _montar_campos(self):
        vbox1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox1.append(self._log_handler())
        vbox1.append(child=self._log_options())
        vbox1.append(child=self._log_entries())

        return vbox1
        # vbox.append(child=vbox1)

# class ConfigSistemaTela(Gtk.Application):
#     def __init__(self):
#         super(ConfigSistemaTela, self).__init__()
#         self._gr = Geral()
#         self._gr.meu_logger.info("inicio")
#
#     def do_activate(self):
#         self._gr.meu_logger.info("entrei no do_activate")
#
#         win = self.props.active_window
#         if not win:
#             win = ConfigSistemaScreen(application=self)
#         win.present()
