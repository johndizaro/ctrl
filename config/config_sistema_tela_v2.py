import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk,Gdk

from geral.geral import Geral
from widgets.popover_help.popover_help import PopoverHelp
from widgets.dialogs.dialog_filechooser import DialogFilechooser


class ConfigSistemaScreen(Gtk.ApplicationWindow):

    def __init__(self, pai):
        super(ConfigSistemaScreen, self).__init__()
        self.pai = pai
        self.gr = Geral()
        self.gr.meu_logger.info(f"entrei no class ConfigSistemaScreen - {self.gr.log_dic}")

        self.montagem_janela()
        self.colocar_dados_tela()

    def colocar_dados_tela(self):

        if 'log_no_terminal' in self.gr.log_dic.keys():
            self._cb_log_terminal.set_active(self.gr.log_dic['log_no_terminal'])

        if 'log_no_arquivo' in self.gr.log_dic.keys():
            self._cb_log_arquivo.set_active(self.gr.log_dic['log_no_arquivo'])

        if 'log_caminho' in self.gr.log_dic.keys():
            self._e_log_caminho_arquivo.set_text(self.gr.log_dic['log_caminho'])
        else:
            self._e_log_caminho_arquivo.set_text(self.gr.log_dic[''])

        if 'log_nome' in self.gr.log_dic.keys():
            self._e_log_nome_arquivo.set_text(self.gr.log_dic['log_nome'])
        else:
            self._e_log_nome_arquivo.set_text(self.gr.log_dic[''])

        if 'log_tipo' in self.gr.log_dic.keys():
            log_tipo = self.gr.log_dic['log_tipo']
        else:
            log_tipo = 'INFO'

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

    def montagem_janela(self):
        self.gr.meu_logger.info("inicio")
        self.set_title(title="Configuração")
        self.set_resizable(resizable=True)
        self.montagem_headerbar()

        # self.set_decorated(setting=True)
        # self.set_modal(modal=True)
        self.set_destroy_with_parent(setting=True)
        self.set_transient_for(parent=self.pai)
        self.montar_layout()

        self.present()

    def montagem_headerbar(self):
        # self.a.info("Montagem do header do menu principal")
        self.gr.meu_logger.info("inicio")
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        self._bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        self._bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        self._bt_salvar.get_style_context().add_class(class_name='destructive')
        self._bt_salvar.set_tooltip_text(text="Salvar alterações")
        self._bt_salvar.connect('clicked', self.on_bt_salvar_clicked)
        headerbar.pack_start(child=self._bt_salvar)

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
        self.colocar_dados_tela()

    def on_bt_salvar_clicked(self, widget):
        # todo: salvar dados da tela no arquivo ini
        # validar campos
        # salvar dados
        if self.validar_campos():
            print("ok")
        else:
            print("nok")

    def validar_campos(self):
        """
        valida os campos se tudo estiver correto retornará True senão False
        :return: Boolean
        """
        campos_ok = True

        if len(str(self._e_log_caminho_arquivo.get_text())) == 0:
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='regular')
            self._e_log_caminho_arquivo.get_style_context().add_class(class_name='error')
            campos_ok = False
        else:
            self._e_log_caminho_arquivo.get_style_context().remove_class(class_name='error')
            self._e_log_caminho_arquivo.get_style_context().add_class(class_name='regular')

        if len(str(self._e_log_nome_arquivo.get_text())) == 0:
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='regular')
            self._e_log_nome_arquivo.get_style_context().add_class(class_name='warning')
            campos_ok = False
        else:
            self._e_log_nome_arquivo.get_style_context().remove_class(class_name='warning')
            self._e_log_nome_arquivo.get_style_context().add_class(class_name='regular')

        # if campos_ok:
        #     self._bt_salvar.set_sensitive(sensitive=True)
        # else:
        #     self._bt_salvar.set_sensitive(sensitive=False)
        return  campos_ok

    def on_bt_ajudar_clicked(self, widget):

        message = "Altera as configurações do sistema"
        PopoverHelp.open(self, pai=widget, message=message)

    def montar_layout(self):
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(margin=10)
        vbox.set_margin_end(margin=10)
        vbox.set_margin_bottom(margin=10)
        vbox.set_margin_start(margin=10)
        vbox.set_valign(Gtk.Align.CENTER)

        vbox.append(child=self.montar_campos())

        self.set_child(child=vbox)

    def _log_handler(self):

        vbox_lh = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        self._cb_log_terminal = Gtk.CheckButton.new_with_label(label='Mostrar log no Terminal')
        self._cb_log_terminal.set_active(setting=True)
        vbox_lh.append(child=self._cb_log_terminal)

        self._cb_log_arquivo = Gtk.CheckButton.new_with_label(label='Salvar log no Arquivo')
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
        vboxf1.get_style_context().add_class(class_name='linked')

        self._e_log_caminho_arquivo = Gtk.Entry.new()
        self._e_log_caminho_arquivo.set_text(text='Caminho para guardar os arquivos de logs')
        self._e_log_caminho_arquivo.get_style_context().add_class(class_name='regular')
        self._e_log_caminho_arquivo.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        self._e_log_caminho_arquivo.connect('icon-press', self.on_e_log_caminho_arquivo_icon_press)
        vboxf1.append(child=self._e_log_caminho_arquivo)

        self._e_log_nome_arquivo = Gtk.Entry.new()
        self._e_log_nome_arquivo.set_text(text='Nome do aquivo de log')
        self._e_log_nome_arquivo.get_style_context().add_class(class_name='regular')
        vboxf1.append(child=self._e_log_nome_arquivo)

        return vboxf1

    def on_e_log_caminho_arquivo_icon_press(self, Entry, EntryIconPosition):

        print(f'Valor digitado no entry: {Entry.get_text()}')
        if EntryIconPosition == Gtk.EntryIconPosition.SECONDARY:
            self._dfc = DialogFilechooser(parent=self, titulo="Caminho para o Log")
            self._dfc.connect('response', self.on_resposta_dialogfilechooser)
        elif EntryIconPosition == Gtk.EntryIconPosition.PRIMARY:
            print("primario")

    def on_resposta_dialogfilechooser(self, widget, response_id):

        if self._dfc.caminho_selecionado:
            caminho_selecionado = self._dfc.caminho_selecionado
        else:
            caminho_selecionado = ""
        self._e_log_caminho_arquivo.set_text(caminho_selecionado)

    def montar_campos(self):
        vbox1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox1.append(self._log_handler())
        vbox1.append(child=self._log_options())
        vbox1.append(child=self._log_entries())

        return vbox1
        # vbox.append(child=vbox1)


class ConfigSistemaTela(Gtk.Application):
    def __init__(self):
        super(ConfigSistemaTela, self).__init__()
        self.gr = Geral()
        self.gr.meu_logger.info("inicio")

    def do_activate(self):
        self.gr.meu_logger.info("entrei no do_activate")

        win = self.props.active_window
        if not win:
            win = ConfigSistemaScreen(application=self)
        win.present()
