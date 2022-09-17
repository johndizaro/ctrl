import os

import pydantic
from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path


class DataConfig(pydantic.BaseModel):
    log_no_terminal: Optional[bool] = True
    log_no_arquivo: Optional[bool] = True
    log_caminho: Optional[str]
    log_nome_arquivo: Optional[str]
    log_tipo: str  = Field('INFO',title='Tipo de log', description="escolha uma das opções",)

    @pydantic.validator("log_caminho")
    @classmethod
    def log_caminho_valid(cls, value):
        root_project = os.path.abspath(os.curdir)

        if len(value) == 0 or not value:
            log_caminho = os.path.join(root_project, "fileslog")
            Path(log_caminho).mkdir(parents=True, exist_ok=True)
            return log_caminho
        else:
            Path(value).mkdir(parents=True, exist_ok=True)
            return value

    @pydantic.validator("log_tipo")
    @classmethod
    def log_tipo_valid(cls, value):
        lst_log_tipo = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

        if (value not in lst_log_tipo):
            raise ValueError("Log tipo deverá ser:'DEBUG', 'INFO', 'WARNING', 'ERROR' ou 'CRITICAL")
        else:
            return value

    @pydantic.validator("log_nome_arquivo")
    @classmethod
    def log_nome_arquivo_valid(cls, value):
        if len(value) == 0 or not value:
            return "logfile.log"
        else:
            return value


# dataconfig1 = DataConfig(log_no_terminal=True,
#                          log_no_arquivo=True,
#                          log_tipo='INFO')

dataconfig1 = DataConfig()
dataconfig1.log_tipo = "ERR"
print(f"dict:{dataconfig1.dict()}")
print(f'log_tipo:{dataconfig1.log_tipo}')
dataconfig1.dict()
print(f'log_no_arquivo:{dataconfig1.log_no_arquivo}')

