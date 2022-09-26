import os
import sys

import gi

from db.infa_dataclass.mysql.entities.entity_unidade_medida import EntityUnidaMedida
from menu.cadastros_auxiliares.unidade_medida import UnidadeMedida

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gio, Gtk

from config.config_sistema_tela import ConfigSistemaMain
from geral.geral import Geral
from widgets.dialogs.dialog_informativ import DialogInformativ
from widgets.sobre_sistema.sobre_sistema import SobreSistema


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
        Gtk.ApplicationWindow.register_window()
        self.gr.meu_logger.info("finalizou")

    def do_startup(self):
        self.gr.meu_logger.info("inicio")
        print("blablabla")
        # Gtk.Application.do_startup(self)

    def montagem_janela(self):
        self.gr.meu_logger.info("inicio")

        self.set_title(title='Montagem de Preço')
        self.maximize()

        # self.set_resizable(resizable=False)

        self.montagem_headerbar()

        self.present()

    def montagem_headerbar(self):
        # self.a.info("Montagem do header do menu principal")
        self.gr.meu_logger.info("inicio")
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)

        # headerbar.get_style_context().add_class(class_name='windowtitle')
        self.set_titlebar(titlebar=headerbar)
        # self.set_subtitle("AAAAA")

        menu_button = self.montagem_menu()
        headerbar.pack_start(child=menu_button)

        return headerbar

    def montagem_menu(self):
        # Criando o menu principal.

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
        utilitarios.append('Exit', 'win.exitsistema')
        menu.append_section(label='Utilitários', section=utilitarios)

        # Acões que serão realizadas pelos itens do menu.
        action_cadastroprodudo = Gio.SimpleAction.new(name='cadastroprodudo', parameter_type=None)
        action_cadastroprodudo.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_cadastroprodudo)

        action_cadastrodeitensdoproduto = Gio.SimpleAction.new(name='cadastrodeitensdoproduto', parameter_type=None)
        action_cadastrodeitensdoproduto.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_cadastrodeitensdoproduto)

        action_unidadedemedida = Gio.SimpleAction.new(name='unidadedemedida', parameter_type=None)
        action_unidadedemedida.connect('activate', self.on_menu_unidadedemedida_clicked)
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

        action_exitsistema = Gio.SimpleAction.new(name='exitsistema', parameter_type=None)
        action_exitsistema.connect('activate', self.on_menu_exitsistema_clicked)
        self.add_action(action=action_exitsistema)

        # Botão que irá conter o menu.
        menu_button = Gtk.MenuButton()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')

        # Adicionando o menu no botão.
        menu_button.set_menu_model(menu)
        # Adicionando o botão no headerbar.
        return menu_button
        # headerbar.pack_start(child=menu_button)

    def on_configuracaosistema_clicked(self, widget, parameter):
        self.gr.meu_logger.info("inicio")
        # ConfigSistemaScreen(pai=self)
        ConfigSistemaMain(pai=self)

    def on_menu_sobreosistema_clicked(self, widget, parameter):
        SobreSistema(parent=self)

    def on_menu_exitsistema_clicked(self, widget, parameter):
        # close the full system
        sys.exit()

    def on_menu_unidadedemedida_clicked(self,widget, parameter):

        self.gr.meu_logger.info("inicio")
        # ConfigSistemaScreen(pai=self)
        UnidadeMedida(pai=self)

        # um1 = EntityUnidaMedida(um_id=1, um_sigla='kg', um_descricao='kilograma')
        # print(um1)
        

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
        self.gr.meu_logger.info("inicio")

        win = self.props.active_window
        if not win:
            win = MenuPrincipalScreen(application=self)
        win.present()

        self.gr.meu_logger.info("executei")

    def do_startup(self):
        self.gr.meu_logger.info("inicio")
        Gtk.Application.do_startup(self)
        self.gr.meu_logger.info("executei")

    def do_shutdown(self):

        """
                Handler for the "quit" signal.
                Destroys all application windows.
                In consequence, GTK will terminate the application.
                """
        for win in self.get_windows():
            win.emit("close-request")

        # as proximas linhas são usada para fechar uma(1) tela
        # close the window
        # app = self.get_application()
        # app.remove_window(self)

        # """When shutdown, finalize database and logging systems."""
        # self.logger.info('Shutting down database...')
        # SQLSession.commit()
        # SQLSession.close()
        #
        # self._daemon.terminate()
        #
        # self.logger.info('Application quit normally.')
        # logging.shutdown()
        # self.gr.meu_logger.info("inicio")
        # Gtk.Application.do_shutdown(self)
        # sys.exit()
        # self.gr.meu_logger.error("executei após o sys.exit() e não deveria")