
class Geral:
    """
    Esta classe é usada para quealgumas informações possa ser
    enchergado no projeto inteiro\n

    from geral.geral import Geral\n
    ...\n
    self.cf = ConfigSistema(pai=self)\n
    gr = Geral()\n
    gr.salva_dic_log(self.cf.traz_dicionario_log())\n
    ...\n
    print(f"geral:{Geral.dic_log}")\n
    """
    log_dic = dict()
    meu_logger = None


    def __init__(self):
        pass
    @classmethod
    def salva_dic_log(cls, log_dic):
        """
        Este methodo e um classmethod  e deverá recebero dicionario do log
        :param log_dic: dicionario do log
        :return:
        """
        cls.log_dic = log_dic

    @classmethod
    def salva_logger(cls,meu_logger):
        """
        Este methodo e um classmethod  e deverá recebero logger do log
        :param meu_logger:
        :return:
        """
        cls.meu_logger=meu_logger
