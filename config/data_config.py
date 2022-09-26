import os
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


@dataclass()
class DataConfig:
    log_no_terminal: bool = field(init=False, default=True, metadata={'options': [True, False],
                                                                      "title": 'Log no terminal',
                                                                      "description": 'O log será enviado para um terminal'})
    log_no_arquivo: bool = field(init=False, default=True, metadata={'options': [True, False],
                                                                     "title": 'Log no arquivo',
                                                                     "description": 'O log será enviado para um arquivo'})
    log_tipo: str = field(init=False, default='INFO',
                          metadata={'options': ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                                    'title': "Tipo de log",
                                    'description': "O tipo do log deverá ser uma das opções: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'"
                                    }
                          )

    log_caminho_arquivo: Optional[str] = field(init=False,
                                               default=os.path.join(os.path.abspath(os.curdir),
                                                                    "fileslog"),
                                               metadata={'title': "Caminho para guardar os arquivos de logs",
                                                         'description': "Local de armazenamento de arquivos de log"})
    log_nome_arquivo: Optional[str] = field(init=False, default='logfile.log',
                                            metadata={'title': "Nome do arquivo de log",
                                                      'description': "Nome do arquivo que conterá o log",
                                                      'field_size': 20})
    log_format: str = field(
        init=False,
        default='%(levelname)-10s  logger:%(name)-15s %(asctime)s filename:%(filename)-20s \tmódulo:%(module)-20s função:%(funcName)-20s  linha:%(lineno)-20s mensagem:%(message)s')

    def get_log_no_terminal_title(self):
        return self.__dataclass_fields__['log_no_terminal'].metadata['title']

    def get_log_no_terminal_description(self):
        return self.__dataclass_fields__['log_no_terminal'].metadata['description']

    def get_log_no_arquivo_title(self):
        return self.__dataclass_fields__['log_no_arquivo'].metadata['title']

    def get_log_no_arquivo_description(self):
        return self.__dataclass_fields__['log_no_arquivo'].metadata['description']

    def get_log_tipo_title(self):
        return self.__dataclass_fields__['log_tipo'].metadata['title']

    def get_log_tipo_description(self):
        return self.__dataclass_fields__['log_tipo'].metadata['description']

    def get_log_caminho_arquivo_title(self):
        return self.__dataclass_fields__['log_caminho_arquivo'].metadata['title']

    def get_log_caminho_arquivo_description(self):
        return self.__dataclass_fields__['log_caminho_arquivo'].metadata['description']

    def get_log_nome_arquivo_title(self):
        return self.__dataclass_fields__['log_nome_arquivo'].metadata['title']

    def get_log_nome_arquivo_description(self):
        return self.__dataclass_fields__['log_nome_arquivo'].metadata['description']

    def get_log_nome_arquivo_field_size(self):
        return self.__dataclass_fields__['log_nome_arquivo'].metadata['field_size']

    def __setattr__(self, attrname, attrvalue):

        match attrname:
            case 'config_caminho':
                self._validade_config_caminho(attrname, attrvalue)
            case 'log_no_terminal':
                self._validade_log_no_terminal(attrname, attrvalue)
            case 'log_no_arquivo':
                self._validade_log_no_arquivo(attrname, attrvalue)
            case 'log_caminho_arquivo':
                self._validate_log_caminho_arquivo(attrname, attrvalue)
            case "log_nome_arquivo":
                self._validade_log_nome_arquivo(attrname, attrvalue)
            case 'log_tipo':
                self._validate_log_tipo(attrname, attrvalue)
            case 'log_format':
                self._validate_log_format(attrname, attrvalue)
            case _:
                raise ValueError(f"{attrname} - {NotImplementedError}")

    # @property
    # def _log_tipo(self) -> str:
    #     return self._log_tipo

    # @_log_tipo.setter
    # def _log_tipo(self, value: str) -> None:
    #     # print(f"_validate_choices - field:{field} - value: {value}")
    #     options = field.metadata['options']
    #     if value not in options:
    #         raise ValueError(f'--->{field.name} value ({value}) not in options: {options}')
    #     else:
    #         self.log_tipo = value

    # def traz_caminho_e_nome_arquivo_config(self):
    #     return os.path.join(self.config_caminho, self.config_nome_arquivo)

    def traz_caminho_nome_arquivo_log(self):
        return os.path.join(self.log_caminho_arquivo, self.log_no_arquivo)

    def _validade_config_caminho(self, attrname, attrvalue):
        if (attrvalue is None or attrvalue == ""):
            attrvalue = self.config_caminho

        if not (Path(attrvalue).is_dir()):
            raise ValueError(f'--->{attrname}: {attrvalue} não é um diretório válido')

        if not (Path(attrvalue).exists()):
            Path(attrvalue).mkdir(parents=True, exist_ok=True)

        self.__dict__[attrname] = attrvalue

    def _validade_log_nome_arquivo(self, attrname, attrvalue):
        if len(attrvalue) > 0:
            self.__dict__[attrname] = attrvalue
        else:
            raise ValueError(f'--->{attrname}: {attrvalue} não é um arquivo válido')

    def _validate_log_caminho_arquivo(self, attrname, attrvalue):

        if (attrvalue is None or attrvalue == ""):
            # attrvalue = self.log_caminho_arquivo
            raise ValueError(f'--->{attrname}: {attrvalue} não é um caminho válido')

        if not (Path(attrvalue).is_dir()):
            raise ValueError(f'--->{attrname}: {attrvalue} não é um diretório válido')

        if not (Path(attrvalue).exists()):
            Path(attrvalue).mkdir(parents=True, exist_ok=True)

        self.__dict__[attrname] = attrvalue

        # a = self.__dict__[attrname]
        # b = Path.home()
        # c = PurePosixPath(a)
        # d = c.parent
        # e = 2

    def _validate_log_format(self, attrname, attrvalue):
        self.__dict__[attrname] = DataConfig.log_format

    def _validade_log_no_terminal(self, attrname, attrvalue):
        options = self.__dataclass_fields__[attrname].metadata['options']
        if attrvalue not in options:
            self.__dict__[attrname] = DataConfig.log_no_terminal
        else:
            self.__dict__[attrname] = attrvalue

    def _validade_log_no_arquivo(self, attrname, attrvalue):
        options = self.__dataclass_fields__[attrname].metadata['options']
        if attrvalue not in options:
            self.__dict__[attrname] = DataConfig.log_no_arquivo
        else:
            self.__dict__[attrname] = attrvalue

    def _validate_log_tipo(self, attrname, attrvalue):
        options = self.__dataclass_fields__[attrname].metadata['options']
        if attrvalue in options:
            self.__dict__[attrname] = attrvalue
        else:
            self.__dict__[attrname] = DataConfig.log_tipo

    def traz_dicionario_log(self):
        return asdict(self)

# dataconfig1 = DataConfig()
#
# dataconfig1.log_tipo = "ERROR"
# dataconfig1.log_caminho_arquivo = "/home/john/Documentos/sistemas/python/desktop/gtk4/ctrl/fileslog"
# dataconfig1.log_tipo
# print(dataconfig1)
# print(dataconfig1.get_log_no_terminal_title())
# print(dataconfig1.get_log_tipo_title())
# print(dataconfig1.get_log_tipo_description())
# x = dataconfig1.log_tipo
# print(asdict(dataconfig1))
# print(dataconfig1.traz_dicionario_log())
# print(dataconfig1.traz_caminho_e_nome_arquivo_config())
