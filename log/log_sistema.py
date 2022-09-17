import os
import sys
import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

class LogSistema:
    """
    Log para o sistema
    dic_log: dicionario com as opções do log
        exemplo:
        self.ls = LogSistema(dic_log=self.cf.dic_log)
        a = self.ls.meu_logger(logger_name="ssdd")
        a.info("asdasdasdasdasd")
        a.error("wwwww")
        a.debug("CCCCC")
    """

    def __init__(self, dic_log):
        """
        dicionario_log={log_no_terminal: True,
                        log_no_arquivo: True,
                        log_ativar: True,
                        log_separar_por_data: True,
                        log_caminho: aa/aa/aa,
                        log_nome_arquivo: ctrllog.log,
                        log_format: %(asctime)s %(name)-12s %(levelname)-15s  módulo:%(module)-20s função:%(funcName)s  mensagem:%(message)s,
                        log_tipo: INFO
                        }
        :param dic_log: dicionario com os paramentros de log


OS TIPO_LOG podem ser :('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
DEBUG  ----->Informações detalhadas, interece tipicamente somente quando for diagnosticar problemas.
INFO   ----->Confirmação que a coisas estão  trabalhando como esperado.
WARNING----->Uma indicação que alguma coisa inesperada aconteceu
             ou indicativo que de algum problema num furuto próximo
             (e.g. ‘disk space low’). Este software ainda está funcionando como esperado.
ERROR  ----->Por causa de problemas mais sérios, o software não é capas de executar algumas funções.
CRITICAL---->Erro sério, indicando que o probrama poderá não conseguir continuar executando.

        """

        if len(dic_log) == 0:
            # raise Exception(f"Desculpe mas {dic_log} está vazio")
            sys.exit(f"O dic_log não poderá estar vazio")

        self._dic_log = dic_log
        # print(self._dic_log)

        # if not self._dic_log['log_ativar']:
        #     return

        if self._dic_log['log_no_terminal']:
            self.meu_console_handler()

        if self._dic_log['log_no_arquivo']:
            self.meu_file_handler()

    def meu_file_handler(self):
        """
        Prepara um arquivo para receber a log
        :return:
        """
        Path(self._dic_log['log_caminho_arquivo']).mkdir(parents=True, exist_ok=True)
        file_handler = TimedRotatingFileHandler(filename=os.path.join(self._dic_log['log_caminho_arquivo'],
                                                                      self._dic_log['log_nome_arquivo']),
                                                backupCount=5,
                                                when='midnight')

        formato = logging.Formatter(self._dic_log['log_format'])
        file_handler.setFormatter(formato)
        # logging.disable(logging.NOTSET)

        return file_handler

    def meu_console_handler(self):
        """
        Prepara o console para receber a log
        :return:
        """

        console_handler = logging.StreamHandler(sys.stdout)
        formato = logging.Formatter(self._dic_log['log_format'])
        console_handler.setFormatter(formato)

        return console_handler

    def meu_logger(self, logger_name):
        """
        Inicializa um novo log com o nome passado para o parametro
        :param logger_name: nome para o logger exemplo: "ctrl.desktop"
        :return:  logger
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(level=self._dic_log['log_tipo'])  # better to have too much log than not enough

        if self._dic_log['log_no_terminal']:
            logger.addHandler(hdlr=self.meu_console_handler())
        if self._dic_log['log_no_arquivo']:
            logger.addHandler(hdlr=self.meu_file_handler())

        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False

        return logger
