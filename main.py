import os
import sys

from config.config_sistema import ConfigSistema
from geral.geral import Geral
from log.log_sistema import LogSistema
from menu_principal import MenuPrincipal
from config.data_config_novo import DataConfig


class Ctrl:
    def __init__(self):
        self._g = Geral()
        self._g.salvar_sistema_path(self, caminho=os.path.abspath(os.curdir))

        self._cf = ConfigSistema()

        self._ls = LogSistema(dic_log=Geral.log_dic)
        self._g.salva_logger(meu_logger=self._ls.meu_logger(logger_name="ctrl.desktop"))

        self._g.meu_logger.info("inicio")

        app = MenuPrincipal()
        app.run(sys.argv)


if __name__ == '__main__':
    Ctrl()
