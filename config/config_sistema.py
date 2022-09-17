from pathlib import Path,PurePosixPath
import configparser
from config.data_config_novo import DataConfig
from geral.geral import Geral


class ConfigSistema:
    def __init__(self):

        self._gr = Geral()
        self._dc = DataConfig()

        self._dic_log = self._dc.traz_dicionario_log()
        self._dic_paths = dict()

        self._dc.config_caminho = Geral.sistema_path
        self._caminho_config = Geral.sistema_path
        self._config_nome_arquivo = Geral.config_nome
        self._config_caminho_nome_arquivo = PurePosixPath(self._caminho_config).joinpath(self._config_nome_arquivo)

        #         self._log_tipo_opts = """
        # ##############################################################################
        # #OS TIPO_LOG podem ser :('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        # #DEBUG  ----->Informações detalhadas, interece tipicamente somente quando for diagnosticar problemas.
        # #INFO   ----->Confirmação que a coisas estão  trabalhando como esperado.
        # #WARNING----->Uma indicação que alguma coisa inesperada aconteceu
        # #             ou indicativo que de algum problema num furuto próximo
        # #             (e.g. ‘disk space low’). Este software ainda está funcionando como esperado.
        # #ERROR  ----->Por causa de problemas mais sérios, o software não é capas de executar algumas funções.
        # #CRITICAL---->Erro sério, indicando que o probrama poderá não conseguir continuar executando.
        # ##############################################################################
        # """
        self._ler_config()

    # def traz_dicionario_log(self):
    #     return self.dic_log

    def _ler_config(self):
        self._tem_arquivo_config()

    def _tem_arquivo_config(self):

        if not Path(self._config_caminho_nome_arquivo).exists():
            self._criar_arquivo_config()

        # self._config = configparser.ConfigParser(interpolation=None)
        # self._config.read(filenames=self._config_caminho_nome_arquivo)

        self._carregar_paths()
        self._carregar_log()

    def _carregar_log(self):

        config = configparser.ConfigParser(interpolation=None)
        config.read(filenames=self._config_caminho_nome_arquivo)

        if not config.has_section(section='LOG'):
            config.add_section(section="LOG")

        try:
            self._dc.log_no_terminal = config.getboolean(section='LOG', option='log_no_terminal')
        except:
            config.set(section='LOG', option='log_no_terminal', value=self._dc.log_no_terminal)
            self.gravar_option(config=config, secao='LOG', opcao='log_no_terminal', valor=self._dc.log_no_terminal)

        try:
            self._dc.log_no_arquivo = config.getboolean(section='LOG', option='log_no_arquivo')
        except:
            config.set(section='LOG', option='log_no_arquivo', value=self._dc.log_no_arquivo)
            self.gravar_option(config=config, secao='LOG', opcao='log_no_arquivo', valor=self._dc.log_no_arquivo)

        try:
            self._dc.log_caminho_arquivo = config.get(section='LOG', option='log_caminho_arquivo')
        except:
            config.set(section='LOG', option='log_caminho_arquivo', value=self._dataconfig.log_caminho_arquivo)
            self.gravar_option(config=config, secao='LOG', opcao='log_caminho_arquivo',
                               valor=self._dataconfig.log_caminho_arquivo)

        try:
            self._dc.log_nome_arquivo = config.get(section='LOG', option='log_nome_arquivo')
        except:
            config.set(section='LOG', option='log_nome_arquivo', value=self._dataconfig.log_nome_arquivo)
            self.gravar_option(config=config, secao='LOG', opcao='log_nome_arquivo',
                               valor=self._dataconfig.log_nome_arquivo)

        try:
            self._dc.log_tipo = config.get(section='LOG', option='log_tipo')
        except:
            config.set(section='LOG', option='log_tipo', value="WARNING")
            self.gravar_option(config=config, secao='LOG', opcao='log_tipo', valor="WARNING")

        try:
            self._dc.log_format = config.get(section='LOG', option='log_format')
        except:
            config.set(section='LOG', option='log_format', value=self._dc.log_format)
            self.gravar_option(config=config, secao='LOG', opcao='log_format', valor=self._dc.log_format)

        self._dic_log = self._dc.traz_dicionario_log()
        self._gr.salva_dic_log(self._dic_log)

    def gravar_option(self, config, secao, opcao, valor):
        config.set(section=secao, option=opcao, value=valor)
        with open(self._config_caminho_nome_arquivo, 'w') as configfile:
            config.write(configfile)
            # configfile.flush()
            configfile.close()

    def _carregar_paths(self):
        pass

    def _criar_arquivo_config(self):
        config = configparser.ConfigParser(allow_no_value=True, interpolation=None)
        # if not config.has_section("PATHS"):
        #     config.add_section(section='PATHS')
        #     config.set(section='PATHS', option='path_system', value='aa/aa')

        if not config.has_section("LOG"):
            config.add_section(section='LOG')
            config.set(section='LOG', option='log_no_terminal', value=str(self._dc.log_no_terminal))
            config.set(section='LOG', option='log_no_arquivo', value=str(self._dc.log_no_arquivo))
            config.set(section='LOG', option='log_tipo', value=self._dc.log_tipo)
            config.set(section='LOG', option='log_caminho_arquivo', value=self._dc.log_caminho_arquivo)
            config.set(section='LOG', option='log_nome_arquivo', value=self._dc.log_nome_arquivo)
            # config.set(section='LOG', option='log_format', value=self._dataconfig.log_format)
        with open(self._config_caminho_nome_arquivo, 'w') as configfile:
            config.write(configfile)
            configfile.close()
