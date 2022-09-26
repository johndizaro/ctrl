import gi

from config.config_sistema import ConfigSistema
from config.data_config_novo import DataConfig
from geral.geral import Geral
from widgets.dialogs.dialog_filechooser import DialogFilechooser
from widgets.popover_help.popover_help import PopoverHelp

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw

Adw.init()


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
                self._tb_log_info.set_active(True)
            case 'DEBUG':
                self._tb_log_debug.set_active(True)
            case 'WARNING':
                self._tb_log_warning.set_active(True)
            case 'ERROR':
                self._tb_log_error.set_active(True)
            case 'CRITICAL':
                self._tb_log_critical.set_active(True)

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
        self._gr.log_dic = campos_validados_log_dic

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
        dic_campos_log_validos = dic()

        # self._dc.log_no_terminal = self._cb_log_terminal.get_active()
        # self._dc.log_no_arquivo = self._cb_log_arquivo.get_active()
        dic_campos_log_validos['log_no_terminal'] = self._cb_log_terminal.get_active()
        dic_campos_log_validos['log_no_arquivo'] = self._cb_log_arquivo.get_active()

        try:
            dic_campos_log_validos['log_caminho_arquivo'] = str(self._e_log_caminho_arquivo.get_text())
            # self._dc.log_caminho_arquivo = str(self._e_log_caminho_arquivo.get_text())
            self._l_log_caminho_arquivo.get_style_context().remove_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='error')
        except ValueError:
            self._l_log_caminho_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='regular')
            campos_ok = False

        try:
            dic_campos_log_validos['log_nome_arquivo'] = str(self._e_log_nome_arquivo.get_text())
            self._dc.log_nome_arquivo = str(self._e_log_nome_arquivo.get_text())
            self._l_log_nome_arquivo.get_style_context().remove_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='error')
        except ValueError:
            self._l_log_nome_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().add_class(class_name='error')
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='regular')
            campos_ok = False

        if self._tb_log_info.get_active():
            # self._dc.log_tipo = str("INFO")
            dic_campos_log_validos['log_tipo'] = str("INFO")
        elif self._tb_log_debug.get_active():
            # self._dc.log_tipo = str("DEBUG")
            dic_campos_log_validos['log_tipo'] = str("DEBUG")
        elif self._tb_log_error.get_active():
            # self._dc.log_tipo = str("ERROR")
            dic_campos_log_validos['log_tipo'] = str("ERROR")
        elif self._tb_log_warning.get_active():
            # self._dc.log_tipo = str("WARNING")
            dic_campos_log_validos['log_tipo'] = str("WARNING")
        elif self._tb_log_critical.get_active():
            # self._dc.log_tipo = str("CRITICAL")
            dic_campos_log_validos['log_tipo'] = str("CRITICAL")

        self._gr.meu_logger.info(f"campos validados - campos_validados_log_dic:{self._dc.traz_dicionario_log()}")

        if campos_ok:
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

    # def _log_handler(self):
    #     vbox_lh = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    #
    #     self._cb_log_terminal = Gtk.CheckButton.new_with_label(label=self._dc.get_log_no_terminal_title())
    #     self._cb_log_terminal.set_active(setting=True)
    #     vbox_lh.append(child=self._cb_log_terminal)
    #
    #     self._cb_log_arquivo = Gtk.CheckButton.new_with_label(label=self._dc.get_log_no_arquivo_title())
    #     self._cb_log_arquivo.set_active(setting=True)
    #     vbox_lh.append(child=self._cb_log_arquivo)
    #     return vbox_lh
    def _log_handler(self):
        vbox_lh = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox.get_style_context().add_class(class_name='boxed-list')
        vbox_lh.append(child=listbox)

        self._cb_log_terminal = Gtk.Switch.new()
        self._cb_log_terminal.set_valign(align=Gtk.Align.CENTER)
        self._cb_log_terminal.set_active(is_active=True)
        # switch_01.connect('notify::active', self.on_switch_button_clicked)

        _cb_log_terminal = Adw.ActionRow.new()
        _cb_log_terminal.set_icon_name(icon_name='utilities-terminal-symbolic')
        _cb_log_terminal.set_title(title=self._dc.get_log_no_terminal_title())
        _cb_log_terminal.set_subtitle(subtitle=self._dc.get_log_no_terminal_description())
        _cb_log_terminal.add_suffix(widget=self._cb_log_terminal)
        listbox.append(child=_cb_log_terminal)

        self._cb_log_arquivo = Gtk.Switch.new()
        self._cb_log_arquivo.set_valign(align=Gtk.Align.CENTER)
        self._cb_log_arquivo.set_active(is_active=True)
        # switch_02.connect('notify::active', self.on_switch_button_clicked)

        _cb_log_arquivo = Adw.ActionRow.new()
        _cb_log_arquivo.set_icon_name(icon_name='text-x-generic-symbolic')
        _cb_log_arquivo.set_title(title=self._dc.get_log_no_arquivo_title())
        _cb_log_arquivo.set_subtitle(subtitle=self._dc.get_log_no_arquivo_description())
        _cb_log_arquivo.add_suffix(widget=self._cb_log_arquivo)
        listbox.append(child=_cb_log_arquivo)

        return vbox_lh

    def _log_options(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.get_style_context().add_class(class_name='card')

        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox.get_style_context().add_class(class_name='boxed-list')
        vbox.append(child=listbox)

        self._tb_log_debug = Gtk.CheckButton()
        self._tb_log_debug.set_group(group=None)
        self._tb_log_debug.set_active(True)

        _tb_log_debug = Adw.ActionRow.new()
        _tb_log_debug.set_icon_name(icon_name='computer-fail')
        _tb_log_debug.set_title(title="DEBUG")
        _tb_log_debug.set_subtitle(
            subtitle='Informações detalhadas, interece tipicamente somente quando for diagnosticar problemas')
        _tb_log_debug.add_suffix(widget=self._tb_log_debug)
        listbox.append(child=_tb_log_debug)

        self._tb_log_warning = Gtk.CheckButton()
        self._tb_log_warning.set_group(group=self._tb_log_debug)

        _tb_log_warning = Adw.ActionRow.new()
        _tb_log_warning.set_icon_name(icon_name='dialog-warning-symbolic')
        _tb_log_warning.set_title(title="WARNING")
        _tb_log_warning.set_subtitle(
            subtitle='Uma indicação que alguma coisa inesperada aconteceu\n indicativo que de algum problema num furuto próximo')
        _tb_log_warning.add_suffix(widget=self._tb_log_warning)
        listbox.append(child=_tb_log_warning)

        self._tb_log_info = Gtk.CheckButton()
        self._tb_log_info.set_group(group=self._tb_log_debug)

        _tb_log_info = Adw.ActionRow.new()
        _tb_log_info.set_icon_name(icon_name='dialog-information-symbolic')
        _tb_log_info.set_title(title="INFO")
        _tb_log_info.set_subtitle(subtitle='Confirmação que a coisas estão  trabalhando como esperado')
        _tb_log_info.add_suffix(widget=self._tb_log_info)
        listbox.append(child=_tb_log_info)

        self._tb_log_error = Gtk.CheckButton()
        self._tb_log_error.set_group(group=self._tb_log_debug)

        _tb_log_error = Adw.ActionRow.new()
        _tb_log_error.set_icon_name(icon_name='dialog-error-symbolic')
        _tb_log_error.set_title(title="ERROR")
        _tb_log_error.set_subtitle(
            subtitle='Por causa de problemas mais sérios, o software não é capas de executar algumas funções')
        _tb_log_error.add_suffix(widget=self._tb_log_error)
        listbox.append(child=_tb_log_error)

        self._tb_log_critical = Gtk.CheckButton()
        self._tb_log_critical.set_group(group=self._tb_log_debug)

        _tb_log_critical = Adw.ActionRow.new()
        _tb_log_critical.set_icon_name(icon_name='face-worried')
        _tb_log_critical.set_title(title="CRÍTICO")
        _tb_log_critical.set_subtitle(
            subtitle='Erro sério, indicando que o probrama poderá não conseguir continuar executando')
        _tb_log_critical.add_suffix(widget=self._tb_log_critical)
        listbox.append(child=_tb_log_critical)

        return vbox

    def _log_entries(self):
        vboxf1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vboxf1.get_style_context().add_class(class_name='card')

        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox.get_style_context().add_class(class_name='boxed-list')
        vboxf1.append(child=listbox)

        self._l_log_caminho_arquivo = Gtk.Label(label=self._dc.get_log_caminho_arquivo_title(),
                                                margin_top=10,
                                                margin_end=10,
                                                margin_start=10,
                                                xalign=0)
        self._l_log_caminho_arquivo.get_style_context().add_class(class_name='caption')
        self._l_log_caminho_arquivo.get_style_context().add_class(class_name='accent')
        listbox.append(child=self._l_log_caminho_arquivo)

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
        listbox.append(child=self._e_log_caminho_arquivo)

        self._l_log_nome_arquivo = Gtk.Label(label=self._dc.get_log_nome_arquivo_title(),
                                             margin_top=10,
                                             margin_end=10,
                                             margin_start=10,
                                             xalign=0)
        self._l_log_nome_arquivo.get_style_context().add_class(class_name='caption')
        self._l_log_nome_arquivo.get_style_context().add_class(class_name='accent')
        listbox.append(child=self._l_log_nome_arquivo)

        self._e_log_nome_arquivo = Gtk.Entry(max_length=self._dc.get_log_nome_arquivo_field_size(),
                                             text="",
                                             tooltip_text=self._dc.get_log_nome_arquivo_description(),
                                             margin_start=10,
                                             margin_end=10,
                                             margin_top=10,
                                             margin_bottom=10)
        listbox.append(child=self._e_log_nome_arquivo)

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
        # vbox1.append(child=self._log_options_1())
        vbox1.append(child=self._log_entries())

        return vbox1
        # vbox.append(child=vbox1)


class ConfigSistemaMain(ConfigSistemaScreen):
    def __init__(self, pai):
        super().__init__(pai)

        self._pai = pai

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ConfigSistemaScreen(pai=self._pai)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

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
