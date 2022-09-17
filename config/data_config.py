# # import dataclasses
# from dataclasses import dataclass, field, asdict
# import os
# from pathlib import Path
# from typing import Optional
#
#
# @dataclass()
# class DataConfig:
#     log_no_terminal: bool = field(init=False, default=True, metadata=dict(title='Log no terminal', description='O log será enviado para um terminal'))
#     log_no_arquivo: bool = field(init=False, default=True, metadata=dict(title='Log no arquivo', description='O log será enviado para um arquivo'))
#     log_caminho: Optional[str] = field(init=False, default=os.path.join(os.path.abspath(os.curdir), "fileslog"))
#     log_nome_arquivo: Optional[str] = field(init=False, default='logfile.log',metadata=dict(title="Nome do arquivo", field_size=20))
#     log_tipo: str = field(init=False, default='INFO')
#     log_format: str = field(
#         init=False,
#         default='%(levelname)-10s  logger:%(name)-15s %(asctime)s filename:%(filename)s  módulo:%(module)-20s função:%(funcName)-20s  mensagem:%(message)s')
#
#     # def __post_init__(self):
#     #     valido = self.validar()
#
#     @property
#     def _log_no_terminal(self) -> str:
#
#         return self.log_no_terminal
#
#     @_log_no_terminal.setter
#     def _log_no_terminal(self, value: str) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usando valor default
#             value = DataConfig.log_no_terminal
#         self.log_no_terminal = value
#
#     @property
#     def _log_no_arquivo(self) -> str:
#         return self.log_no_arquivo
#
#     @_log_no_arquivo.setter
#     def _log_no_arquivo(self, value) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usando valor default
#             value = DataConfig.log_no_arquivo
#         self.log_no_arquivo = value
#
#     @property
#     def _log_caminho(self) -> str:
#         return self.log_caminho
#
#     @_log_caminho.setter
#     def _log_caminho(self, value: str) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usando valor default
#             value = DataConfig.log_caminho
#         self.log_caminho = value
#
#     @property
#     def _log_nome_arquivo(self) -> str:
#         return self.log_nome_arquivo
#
#     @_log_nome_arquivo.setter
#     def _log_nome_arquivo(self, value: str) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usando valor default
#             value = DataConfig.log_nome_arquivo
#         self.log_nome_arquivo = value
#
#
#     @property
#     def _log_tipo(self) -> str:
#         return self._log_tipo
#
#     @_log_tipo.setter
#     def _log_tipo(self, value: str) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usa o valor default
#             value = DataConfig.log_tipo
#         self.log_tipo = value
#
#     @property
#     def _log_format(self) -> str:
#         return self._log_format
#
#     @_log_format.setter
#     def _log_format(self, value: str) -> None:
#         if type(value) is property:
#             # valor inicial não especificado, usa o valor default
#             value = DataConfig.log_format
#         self.log_tipo = value
#
#     def __setattr__(self, key, value):
#         valido = True
#
#         lst_log_tipo = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
#         lst_log_parameter = ['name', 'level', 'pathname', 'lineno', 'msg', 'args', 'exc_info', 'func', 'sinfo']
#         lst_boolean = [True, False]
#
#         if key == "log_no_terminal":
#             if value not in lst_boolean:
#                 self.__dict__[key] = True
#
#         if key == "log_no_arquivo":
#             if value not in lst_boolean:
#                 self.__dict__[key] = True
#
#         if key == "log_tipo":
#             if value in lst_log_tipo:
#                 self.__dict__[key] = value
#             # assert value in lst_log_tipo, f"key:{key} value:{value} inválido"
#
#         if key == "log_caminho":
#             if len(value) > 0:
#                 Path(value).mkdir(parents=True, exist_ok=True)
#                 self.__dict__[key] = value
#             else:
#                 caminho = os.path.join(os.path.abspath(os.curdir), "fileslog")
#                 Path(caminho).mkdir(parents=True, exist_ok=True)
#                 self.__dict__[key] = caminho
#
#         if key == "log_nome_arquivo":
#             if len(value) > 0:
#                 self.__dict__[key] = value
#             else:
#                 self.__dict__[key] = "filelog.log"
#
#     def traz_dic(self) -> dict:
#         return asdict(self)
#
#     def validar(self):
#         valido = True
#         lst_log_tipo = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
#         # root_project = os.path.abspath(os.curdir)
#
#         if self.log_tipo not in lst_log_tipo:
#             valido = False
#         if len(self.log_tipo) == 0:
#             valido = False
#
#         if len(self.log_caminho) == 0 or not os.path.exists(self.log_caminho):
#             caminho = os.path.join(os.path.abspath(os.curdir), "fileslog")
#             Path(caminho).mkdir(parents=True, exist_ok=True)
#         else:
#             Path(self.log_caminho).mkdir(parents=True, exist_ok=True)
#
#         if len(self.log_nome_arquivo) == 0:
#             valido = False
#         if len(self.log_format) == 0:
#             valido = False
#         print(f"valido{valido}")
#         return valido
#
# dataconfig1 = DataConfig()
# dataconfig1.log_no_terminal = True
# dataconfig1.log_no_arquivo = False
# dataconfig1.log_nome_arquivo = "aaa.log"
# dataconfig1.log_tipo = "ERRO"
# print(dataconfig1)
# print(asdict(dataconfig1))
