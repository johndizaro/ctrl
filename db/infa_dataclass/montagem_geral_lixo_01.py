from typing import Type

from dataclasses import dataclass


@dataclass
class UnidadeMedida:
    """ classe para guardar unidades de medida"""

    um_id: int
    um_sigla: str
    um_descricao: str

    def __repr__(self):
        return f"um_id:{self.um_id}\t um_sigla:{self.um_sigla}\t um_descricao:{self.um_descricao}"

    @property
    def um_id(self):
        return self._um_id

    @property
    def um_sigla(self):
        return self._um_sigla

    @property
    def um_descricao(self):
        return self._um_descricao

    @um_id.setter
    def um_id(self, value):
        self._um_id = value

    @um_sigla.setter
    def um_sigla(self, value):
        self._um_sigla = value + "r"

    @um_descricao.setter
    def um_descricao(self, value):
        self._um_descricao = value

    @um_descricao.getter
    def um_desricao(self):
        return  f"{self._um_descricao} retorno "


um1 = UnidadeMedida(um_id=1, um_sigla='kg', um_descricao='kilograma')
print(um1)
um1.um_descricao = "oi"
print(um1)
um1.um_sigla = "oi"
print(um1)
