import sys
from pathlib import Path

from config.config_sistema import ConfigSistema
from geral.geral import Geral
from log.log_sistema import LogSistema
from menu.menu_principal import MenuPrincipal
# from config.data_config_novo import DataConfig

# Adw.init()
#
BASE_DIR = Path(__file__).resolve().parent
FILENAME = str(BASE_DIR.joinpath('MainWindow.ui'))
#

class Ctrl:
    def __init__(self):
        # print(f"base-dir:{BASE_DIR}--- FILENAME: {FILENAME}")
        self._g = Geral()

        # self._g.salvar_sistema_path(self, caminho=os.path.abspath(os.curdir))
        self._g.salvar_sistema_path(self, caminho=BASE_DIR)

        self._cf = ConfigSistema()

        self._ls = LogSistema(dic_log=Geral.log_dic)
        self._g.salva_logger(meu_logger=self._ls.meu_logger(logger_name="ctrl.desktop"))

        self._g.meu_logger.info(f"base-dir:{BASE_DIR} --- FILENAME: {FILENAME}")
        self._g.meu_logger.info(f"Caminho config:{self._g.monta_caminho_e_nome_config()}")


        app = MenuPrincipal()
        app.run(sys.argv)


if __name__ == '__main__':
    Ctrl()
