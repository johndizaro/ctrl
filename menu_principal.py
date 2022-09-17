import os
import gi

from log.log_sistema import LogSistema
from widgets.dialogs.dialog_informativ import DialogInformativ
from config.config_sistema_tela import ConfigSistemaScreen
from config.config_sistema import ConfigSistema

from gi.repository import Gio, Gtk

from widgets.sobre_sistema.sobre_sistema import SobreSistema
from geral.geral import Geral

gi.require_version(namespace='Gtk', version='4.0')


# gi.require_version(namespace='Adw', version='1.0')
# from gi.repository import  Adw


class MenuPrincipalScreen(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gr = Geral()

        self.gr.meu_logger.info("inicio")
        self.gr.meu_logger.info(f"Geral.log_dic:{self.gr.log_dic}")

        # # desenha a janela
        self.montagem_janela()
        # # Criando headerbar.

    def on_dialog_question_response(self, widget, response_id):
        self.gr.meu_logger.info("inicio")
        print("on_dialog_question_response->>" + str(response_id))

    def do_activate_default(self, *args, **kwargs):
        self.gr.meu_logger.info("inicio")
        print("do_activate_default")

    def do_shutdown(self):
        # self.ls.logger.info("saindo do sistema via do_shutdown")
        self.gr.meu_logger.info("inicio")
        Gtk.Application.do_shutdown(self)

    def do_startup(self):
        self.gr.meu_logger.info("inicio")
        Gtk.Application.do_startup(self)

    def montagem_janela(self):
        self.gr.meu_logger.info("inicio")

        self.set_title(title='Montagem de Preço')
        self.maximize()
        self.set_resizable(resizable=False)

        self.montagem_headerbar()

        self.present()

    def montagem_headerbar(self):
        # self.a.info("Montagem do header do menu principal")
        self.gr.meu_logger.info("inicio")
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)
        menu_button = self.montagem_menu()
        headerbar.pack_start(child=menu_button)

        return headerbar

    def montagem_menu(self):
        # Criando o menu principal.
        self.gr.meu_logger.info("inicio")
        self.gr.meu_logger.info("inicio")
        menu = Gio.Menu.new()
        menu.append(label='Cadastro de Produto', detailed_action='win.cadastroprodudo')
        menu.append(label='Cadastro de Itens do Produto', detailed_action='win.cadastrodeitensdoproduto')

        # Criando um submenu Cadastros Auxiliares.
        submenu1 = Gio.Menu.new()
        submenu1.append('Unidades de Medida', 'win.unidadedemedida')
        submenu1.append('Conversão de Medidas', 'win.convercaodeunidadedemedida')
        menu.append_submenu(label='Cadastros Auxiliares', submenu=submenu1)

        # Criando  Utilitários
        utilitarios = Gio.Menu.new()
        utilitarios.append('Configuração do Sistema', 'win.configuracaosistema')
        utilitarios.append('Sobre o Sistema', 'win.sobreosistema')
        menu.append_section(label='Utilitários', section=utilitarios)

        # Acões que serão realizadas pelos itens do menu.
        action_cadastroprodudo = Gio.SimpleAction.new(name='cadastroprodudo', parameter_type=None)
        action_cadastroprodudo.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_cadastroprodudo)

        action_cadastrodeitensdoproduto = Gio.SimpleAction.new(name='cadastrodeitensdoproduto', parameter_type=None)
        action_cadastrodeitensdoproduto.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_cadastrodeitensdoproduto)

        action_unidadedemedida = Gio.SimpleAction.new(name='unidadedemedida', parameter_type=None)
        action_unidadedemedida.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_unidadedemedida)

        action_convercaodeunidadedemedida = Gio.SimpleAction.new(name='convercaodeunidadedemedida', parameter_type=None)
        action_convercaodeunidadedemedida.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_convercaodeunidadedemedida)

        action_configuracaosistema = Gio.SimpleAction.new(name='configuracaosistema', parameter_type=None)
        action_configuracaosistema.connect('activate', self.on_configuracaosistema_clicked)
        self.add_action(action=action_configuracaosistema)

        action_sobreosistema = Gio.SimpleAction.new(name='sobreosistema', parameter_type=None)
        action_sobreosistema.connect('activate', self.on_menu_sobreosistema_clicked)
        self.add_action(action=action_sobreosistema)

        # Botão que irá conter o menu.
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')

        # Adicionando o menu no botão.
        menu_button.set_menu_model(menu)
        # Adicionando o botão no headerbar.
        return menu_button
        # headerbar.pack_start(child=menu_button)

    def on_configuracaosistema_clicked(self, widget, parameter):
        self.gr.meu_logger.info("inicio")
        ConfigSistemaScreen(pai=self)

    def on_menu_sobreosistema_clicked(self, widget, parameter):
        SobreSistema(parent=self)

    def on_menu_item_clicked(self, widget, parameter):
        DialogInformativ(parent=self,
                         titulo="Cadastro de produto",
                         titulo_mensagem="Rotina não implementada",
                         mensagem="Por favor aguarde seu desenvolvimento")

        # SobreSistema(parent=self)
        # ConfigSistema.mostrar_config_tela(self)
        print("1-{}".format(os.path.dirname(os.path.realpath(__file__))))
        print("2-{}".format(os.getcwd()))
        print("3-{}".format(os.curdir))
        print("4-{}".format(os.sep))
        print("5-{}".format(os.path))
        print("6-{}".format(os.pathsep))


class MenuPrincipal(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.ctrl.johndizaro',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        # self.cf = ConfigSistema()

        self.gr = Geral()
        # self.gr.salva_dic_log(self.cf.dic_log)

        # self._ls = LogSistema(dic_log=self.cf.dic_log)


        # self.gr.salva_logger(meu_logger=self._ls.meu_logger(logger_name="ctrl.desktop"))

        self.gr.meu_logger.info("inicio")
        self.gr.meu_logger.info(f"dicionario gr.log_dic:{self.gr.log_dic}")

    def do_activate(self):
        self.gr.meu_logger.info("executei do_activate")

        win = self.props.active_window
        if not win:
            win = MenuPrincipalScreen(application=self)
        win.present()

    def do_startup(self):
        self.gr.meu_logger.info("executei do_startup")
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        """When shutdown, finalize database and logging systems."""
        # self.logger.info('Shutting down database...')
        # SQLSession.commit()
        # SQLSession.close()
        #
        # self._daemon.terminate()
        #
        # self.logger.info('Application quit normally.')
        # logging.shutdown()
        self.gr.meu_logger.info("executei do_shutdown")
        Gtk.Application.do_shutdown(self)
