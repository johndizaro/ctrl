import os
import configparser
from geral.geral import Geral

class ConfigSistema:
    def __init__(self, config_nome="config.ini"):
        # print("executei ConfigSistema __init__")
        self.root_project = os.path.abspath(os.curdir)
        self.dic_log = dict()
        self.dic_paths = dict()

        if config_nome:
            self._config_nome = config_nome
        else:
            self._config_nome = "config.ini"

        self._caminho_config = self.root_project
        self._config_caminho_nome = os.path.join(self._caminho_config, self._config_nome)

        self._log_nome_arquivo = "ctrl_log.log"
        self._log_caminho = os.path.join(self.root_project, "fileslog")
        self._log_caminho_nome = os.path.join(self._log_caminho, self._log_nome_arquivo)
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
        # self._config = configparser.ConfigParser()
        # self._config.read(filenames=self._config_caminho_nome)

        self.ler_config()

    def traz_dicionario_log(self):
        return  self.dic_log

    def ler_config(self):
        self._tem_arquivo_config()

    def _tem_arquivo_config(self):
        if not os.path.exists(self._config_caminho_nome):
            self._criar_arquivo_config()

        self._config = configparser.ConfigParser()
        self._config.read(filenames=self._config_caminho_nome)
        self._carregar_config()

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

        # log_nome_arquivo = ctrl_log.log
        try:
            log_nome_arquivo = config.get(section='LOG', option='log_nome_arquivo')
            self.dic_log['log_nome_arquivo'] = log_nome_arquivo
            self._log_nome_arquivo = log_nome_arquivo
        except:
            config.set(section='LOG', option='log_nome_arquivo', value=self._log_nome)
            self.dic_log['log_nome_arquivo'] = self._log_nome_arquivo
            self.gravar_option(secao='LOG', opcao='log_nome_arquivo', valor=self._log_nome)

        # log_tipo = WARNING
        try:
            log_tipo = config.get(section='LOG', option='log_tipo')
            self.dic_log['log_tipo'] = log_tipo
        except:
            config.set(section='LOG', option='log_tipo', value="WARNING")
            self.dic_log['log_tipo'] = "WARNING"
            self.gravar_option(secao='LOG', opcao='log_tipo', valor="WARNING")

        # log_format = %%(asctime)s %%(name)-12s %%(levelname)-15s  módulo:%%(module)-20s função:%%(funcName)s  mensagem:%%(message)s
        try:
            log_format = config.get(section='LOG', option='log_format')
            self.dic_log['log_format'] = log_format
        except:
            log_format = '%%(asctime)s %%(name)-12s %%(levelname)-15s  módulo:%%(module)-20s função:%%(funcName)s  mensagem:%%(message)s'
            config.set(section='LOG', option='log_format', value=log_format)
            self.dic_log['log_format'] = log_format
            self.gravar_option(secao='LOG', opcao='log_format', valor=log_format)

    def gravar_option(self, secao, opcao, valor):

        self._config.set(section=secao, option=opcao, value=valor)
        with open(self._config_caminho_nome, 'w') as configfile:
            self._config.write(configfile)
            # configfile.flush()
            configfile.close()



    def _carregar_paths(self):

        config = configparser.ConfigParser()
        config.read(filenames=self._config_caminho_nome)

        if not config.has_section(section='PATHS'):
            config.add_section(section="PATHS")

        try:
            path_system = config.getboolean(section='PATHS', option='path_system')
            self.dic_paths['path_system'] = path_system
        except:
            config.set(section='PATHS', option='path_system', value='aa/aa')
            self.dic_paths['path_system'] = 'aa/aa'
            self.gravar_option(secao='PATHS', opcao='path_system', valor='aa/aa')

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

        with open(self._config_caminho_nome, 'w') as configfile:
            config.write(configfile)
            configfile.close()
