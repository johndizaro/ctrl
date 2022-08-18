import configparser
import copy
import os
import sys

from datetime import date
from pathlib import Path
import gi
from gi.repository import Gio, Gtk

gi.require_version(namespace='Gtk', version='4.0')

from widgets.dialogs.dialog_question_yesno_v2 import DialogQuestionYesNo
from widgets.dialogs.dialog_informativ_v2 import DialogInformativ


class ConfigSistema:
    def __init__(self, pai, config_nome="config.ini"):
        super(ConfigSistema, self).__init__()

        self._pai = pai
        self.root_project = os.path.abspath(os.curdir)
        # self.dic_paramentos_sistema = dict()
        self.dic_log = dict()
        self.dic_paths = dict()

        if config_nome:
            self._config_nome = config_nome
        else:
            self._config_nome = "config.ini"
        self._caminho_config = self.root_project
        self._config_caminho_nome = os.path.join(self._caminho_config, self._config_nome)

        self._log_nome = "ctrl_log.log"
        self._log_caminho = os.path.join(self.root_project, "fileslog")
        self._log_caminho_nome = os.path.join(self._log_caminho, self._log_nome)
        self._log_format = '%%(levelname)-10s  logger:%%(name)-15s %%(asctime)s filename:%%(filename)s  módulo:%%(module)-20s função:%%(funcName)-20s  mensagem:%%(message)s'
        self._log_tipo_opts = """
##############################################################################
#OS TIPO_LOG podem ser :('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
#DEBUG  ----->Informações detalhadas, interece tipicamente somente quando for diagnosticar problemas.
#INFO   ----->Confirmação que a coisas estão  trabalhando como esperado.
#WARNING----->Uma indicação que alguma coisa inesperada aconteceu
#             ou indicativo que de algum problema num furuto próximo
#             (e.g. ‘disk space low’). Este software ainda está funcionando como esperado.
#ERROR  ----->Por causa de problemas mais sérios, o software não é capas de executar algumas funções.
#CRITICAL---->Erro sério, indicando que o probrama poderá não conseguir continuar executando.
##############################################################################
"""

        self._config = configparser.ConfigParser()
        self._config.read(filenames=self._config_caminho_nome)

    def ler_config(self):
        self._tem_arquivo_config()

    def traz_dicionario_log(self):
        return  self.dic_log

    def _tem_arquivo_config(self):
        if not os.path.exists(self._config_caminho_nome):
            dialog_question = DialogQuestionYesNo(parent=self._pai,
                                                  titulo=f"Arquivo não foi encontrado",
                                                  titulo_mensagem=f"O arquivo {self._config_nome} não foi encontrado",
                                                  mensagem=f"""
Não foi encontrado no caminho <b>{self._config_caminho_nome}</b>
Posso criar um novo?""")
            dialog_question.connect('response', self.on_tem_arquivo_config)
        else:
            self._criar_arquivo_config()
            self._carregar_config()

    def on_tem_arquivo_config(self, widget, response_id):
        if response_id == Gtk.ResponseType.YES:
            # arquivo config.ini não localiado o mesmo será criado
            self.criar_arquivo_config()
            self._carregar_config()
        elif response_id == Gtk.ResponseType.NO:
            # arquivo config.ini não localisado  o responsavel deverá providenciar uma copia
            self.avisar_providenciar()

    def avisar_providenciar(self):
        dip = DialogInformativ(parent=self._pai,
                               titulo="Atenção",
                               titulo_mensagem=f"Providencie um {self._config_nome}",
                               mensagem="Após providenciar entre no sistema outra vez.")
        dip.connect('response', self.on_avisar_providenciar)

    def on_avisar_providenciar(self, widget, response_id):
        if Gtk.ResponseType.OK:
            sys.exit("O usuario deverá providenciar um config.ini")
            # Gtk.Application.quit()
            # Gtk.main_quit()

    def _carregar_config(self):
        self._carregar_paths()
        self._carregar_log()

    def _carregar_log(self):

        config = configparser.ConfigParser()
        config.read(filenames=self._config_caminho_nome)

        # todo: fazer caregar_log
        if not config.has_section(section='LOG'):
            config.add_section(section="LOG")

        # log_no_terminal = True or False
        try:
            log_no_terminal = config.getboolean(section='LOG', option='log_no_terminal')
            self.dic_log['log_no_terminal'] = log_no_terminal
        except:
            config.set(section='LOG', option='log_no_terminal', value='True')
            self.dic_log['log_no_terminal'] = True
            self.gravar_option(secao='LOG', opcao='log_no_terminal', valor='True')

        # log_no_arquivo = True or False
        try:
            log_no_arquivo = config.getboolean(section='LOG', option='log_no_arquivo')
            self.dic_log['log_no_arquivo'] = log_no_arquivo
        except:
            config.set(section='LOG', option='log_no_arquivo', value='True')
            self.dic_log['log_no_arquivo'] = True
            self.gravar_option(secao='LOG', opcao='log_no_arquivo', valor='True')

        # log_ativar = True or False
        # try:
        #     log_ativar = config.getboolean(section='LOG', option='log_ativar')
        #     self.dic_log['log_ativar'] = log_ativar
        # except:
        #     config.set(section='LOG', option='log_ativar', value='True')
        #     self.dic_log['log_ativar'] = True
        #     self.gravar_option(secao='LOG', opcao='log_ativar', valor='True')

        # # log_separar_por_data = True or False
        # try:
        #     log_separar_por_data = config.getboolean(section='LOG', option='log_separar_por_data')
        #     self.dic_log['log_separar_por_data'] = log_separar_por_data
        # except:
        #     config.set(section='LOG', option='log_separar_por_data', value='True')
        #     self.dic_log['log_separar_por_data'] = True
        #     self.gravar_option(secao='LOG', opcao='log_separar_por_data', valor='True')

        # log_caminho = /home/john/Documentos/sistemas/python/desktop/gtk4/ctrl/fileslog
        try:
            log_caminho = config.get(section='LOG', option='log_caminho')
            self.dic_log['log_caminho'] = log_caminho
            self._log_caminho = log_caminho
        except:
            config.set(section='LOG', option='log_caminho', value=self._log_caminho)
            self.dic_log['log_caminho'] = self._log_caminho
            self.gravar_option(secao='LOG', opcao='log_caminho', valor=self._log_caminho)

        # log_nome = ctrl_log.log
        try:
            log_nome = config.get(section='LOG', option='log_nome')
            self.dic_log['log_nome'] = log_nome
            self._log_nome = log_nome
        except:
            config.set(section='LOG', option='log_nome', value=self._log_nome)
            self.dic_log['log_nome'] = self._log_nome
            self.gravar_option(secao='LOG', opcao='log_nome', valor=self._log_nome)

        # log_tipo = WARNING
        try:
            log_tipo = config.get(section='LOG', option='log_tipo')
            self.dic_log['log_tipo'] = log_tipo
        except:
            config.set(section='LOG', option='log_tipo', value="WARNING")
            self.dic_log['log_tipo'] = "WARNING"
            self.gravar_option(secao='LOG', opcao='log_tipo', valor="WARNING")
            # self.gravar_option(secao='LOG', opcao=self._log_opt, valor=None)

        # log_format = %%(asctime)s %%(name)-12s %%(levelname)-15s  módulo:%%(module)-20s função:%%(funcName)s  mensagem:%%(message)s
        try:
            log_format = config.get(section='LOG', option='log_format')
            self.dic_log['log_format'] = log_format
        except:
            log_format = '%%(asctime)s %%(name)-12s %%(levelname)-15s  módulo:%%(module)-20s função:%%(funcName)s  mensagem:%%(message)s'
            config.set(section='LOG', option='log_format', value=log_format)
            self.dic_log['log_format'] = log_format
            self.gravar_option(secao='LOG', opcao='log_format', valor=log_format)
        # self.dic_log = self.dic_paramentos_sistema.copy()
        # print(f"dic_log:{self.dic_log}")

    def gravar_option(self, secao, opcao, valor):

        self._config.set(section=secao, option=opcao, value=valor)
        with open(self._config_caminho_nome, 'w') as configfile:
            self._config.write(configfile)
            # configfile.flush()
            configfile.close()



    def _carregar_paths(self):

        config = configparser.ConfigParser()
        config.read(filenames=self._config_caminho_nome)

        # todo: fazer caregar_log
        if not config.has_section(section='PATHS'):
            config.add_section(section="PATHS")

        # log_no_terminal = True or False
        try:
            path_system = config.getboolean(section='PATHS', option='path_system')
            self.dic_paths['path_system'] = path_system
        except:
            config.set(section='PATHS', option='path_system', value='aa/aa')
            self.dic_paths['path_system'] = 'aa/aa'
            self.gravar_option(secao='PATHS', opcao='path_system', valor='aa/aa')
        # print(f'self.dic_paths:{self.dic_paths}')

    def _criar_arquivo_config(self):
        config = configparser.ConfigParser(allow_no_value=True)
        if not config.has_section("PATHS"):
            config.add_section(section='PATHS')
            config.set(section='PATHS', option='path_system', value='aa/aa')

        if not config.has_section("LOG"):
            config.add_section(section='LOG')
            config.set(section='LOG', option='log_no_terminal', value='True')
            config.set(section='LOG', option='log_no_arquivo', value='True')
            # config.set(section='LOG', option='log_ativar', value='True')
            # config.set(section='LOG', option='log_separar_por_data', value='True')
            config.set(section='LOG', option='log_caminho', value=self._log_caminho)
            config.set(section='LOG', option='log_nome', value='ctrl_log.log')
            config.set(section='LOG', option='log_format', value=self._log_format)
            config.set(section='LOG', option='log_tipo', value='WARNING')
            config.set(section='LOG', option=self._log_tipo_opts)
        with open(self._config_nome, 'w') as configfile:
            config.write(configfile)

    def criar_arquivo_config_from_dict(self):

        config = configparser.ConfigParser(allow_no_value=True)
        config['PATHS'] = {'path_system': "aa/aa",
                           'path_system_pictures': "bb/bb",
                           'path_system_icons': "cc/cc"
                           }
        config['LOG'] = {'log_no_terminal': True,
                         'log_no_arquivo': True,
                         # 'log_ativar': True,
                         # 'log_separar_por_data': True,
                         'log_caminho': f"{self._log_caminho}",
                         'log_nome': self._log_nome,
                         'log_format': '%%(asctime)s %%(name)-12s %%(levelname)-15s  módulo:%%(module)-20s função:%%(funcName)s  mensagem:%%(message)s',
                         'log_tipo': "WARNING",
                         self._log_tipo_opts: None
                         }
        with open(self._config_nome, 'a') as configfile:
            config.write(configfile)
