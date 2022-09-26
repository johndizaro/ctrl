from pathlib import PurePosixPath


class Geral:
    """
    Esta classe é usada para que algumas informações possa ser
    enchergado no projeto inteiro\n

    from geral.geral import Geral\n
    ...\n
    self.cf = ConfigSistema(pai=self)\n
    gr = Geral()\n
    gr.salva_dic_log(self.cf.dic_log())\n
    ...\n
    print(f"geral:{Geral.dic_log}")\n
    """
    log_dic = dict()

    sistema_path = ""
    config_nome = "config.ini"

    meu_logger = None

    def __init__(self):
        pass

    @classmethod
    def monta_caminho_e_nome_config(cls):
        return PurePosixPath(cls.sistema_path).joinpath(cls.config_nome)

    @classmethod
    def salva_dic_log(cls, log_dic):
        """
        Este methodo e um classmethod  e deverá recebero dicionario do log
        :param log_dic: dicionario do log
        :return:
        """

        if len(cls.log_dic) == 0:
            cls.log_dic = log_dic
        else:
            cls.log_dic.update(log_dic)

    @classmethod
    def salvar_sistema_path(cls, self, caminho):
        """
        Este methodo e um classmethod e deverá recever o caminho do config.ini
        :param self:
        :param caminho:
        :return:
        """
        cls.sistema_path = caminho

    @classmethod
    def salva_logger(cls, meu_logger):
        """
        Este methodo e um classmethod  e deverá recebero logger do log
        :param meu_logger:
        :return:
        """
        cls.meu_logger = meu_logger
