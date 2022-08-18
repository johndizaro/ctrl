import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk, Gdk, Gio

from geral.geral import Geral
from widgets.popover_help.popover_help import PopoverHelp


class ConfigSistemaScreen(Gtk.ApplicationWindow):
    def __init__(self, pai):
        super(ConfigSistemaScreen, self).__init__()
        self.pai = pai
        self.gr = Geral()
        self.gr.meu_logger.info("entrei no class ConfigSistemaScreen")

        self.montagem_janela()

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

        bt_salvar = Gtk.Button.new_with_label(label='Salvar')
        bt_salvar.set_icon_name(icon_name='document-save-symbolic')
        bt_salvar.get_style_context().add_class(class_name='suggested-action')
        bt_salvar.set_tooltip_text(text="Salvar alterações")
        headerbar.pack_start(child=bt_salvar)

        bt_ajudar = Gtk.Button.new_with_label(label='Ajudar')
        bt_ajudar.set_icon_name(icon_name='help-browser-symbolic')
        bt_ajudar.get_style_context().add_class(class_name='')
        bt_ajudar.set_tooltip_text(text="Uma preve explicação sobre a tela")
        bt_ajudar.connect('clicked', self.on_bt_ajudar_clicked)
        headerbar.pack_end(child=bt_ajudar)

        return headerbar

    def on_bt_ajudar_clicked(self, widget):

        mensagem = "Altera as configurações do sistema"

        PopoverHelp.open(self, pai=widget, mensagem=mensagem)

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

        checkbutton1 = Gtk.CheckButton.new_with_label(label='Mostrar log no Terminal')
        checkbutton1.set_active(setting=True)
        vbox_lh.append(child=checkbutton1)

        checkbutton2 = Gtk.CheckButton.new_with_label(label='Salvar log no Arquivo')
        checkbutton2.set_active(setting=True)
        vbox_lh.append(child=checkbutton2)
        return vbox_lh

    def _log_options(self):
        hboxf1 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hboxf1.set_homogeneous(True)
        hboxf1.get_style_context().add_class(class_name='linked')
        hboxf1.set_margin_top(margin=12)
        hboxf1.set_margin_end(margin=12)
        hboxf1.set_margin_bottom(margin=12)
        hboxf1.set_margin_start(margin=12)

        togglebuttun1 = Gtk.ToggleButton.new_with_label(label="Debug")
        # togglebuttun1.set_group(togglebuttun1)
        togglebuttun1.set_active(is_active=False)
        hboxf1.append(child=togglebuttun1)

        togglebuttun2 = Gtk.ToggleButton.new_with_label(label="Info")
        togglebuttun2.set_group(togglebuttun1)
        togglebuttun2.set_active(is_active=True)
        hboxf1.append(child=togglebuttun2)

        togglebuttun3 = Gtk.ToggleButton.new_with_label(label="Warning")
        togglebuttun3.set_group(togglebuttun1)
        togglebuttun3.set_active(is_active=False)
        hboxf1.append(child=togglebuttun3)

        togglebuttun4 = Gtk.ToggleButton.new_with_label(label="Error")
        togglebuttun4.set_group(togglebuttun1)
        togglebuttun4.set_active(is_active=False)
        hboxf1.append(child=togglebuttun4)

        togglebuttun5 = Gtk.ToggleButton.new_with_label(label="Critical")
        togglebuttun5.set_group(togglebuttun1)
        togglebuttun5.set_active(is_active=False)
        hboxf1.append(child=togglebuttun5)

        frame1 = Gtk.Frame.new(label="Opções de log")
        frame1.set_child(hboxf1)
        return frame1

    def _log_entries(self):
        vboxf1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vboxf1.get_style_context().add_class(class_name='linked')
        vboxf1.set_margin_top(margin=12)
        # vboxf1.set_margin_end(margin=12)
        # vboxf1.set_margin_bottom(margin=12)
        # vboxf1.set_margin_start(margin=12)

        entry1 = Gtk.Entry.new()
        entry1.set_text(text='Caminho para guardar os arquivos de logs')
        entry1.get_style_context().add_class(class_name='regular')
        entry1.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='system-search-symbolic',
        )
        vboxf1.append(child=entry1)

        entry2 = Gtk.Entry.new()
        entry2.set_text(text='Nome do aquivo de log')
        entry2.get_style_context().add_class(class_name='regular')
        vboxf1.append(child=entry2)

        return vboxf1

    def montar_campos(self):
        vbox1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        # vbox1.get_style_context().add_class(class_name='linked')

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
