from dataclasses import dataclass, field

from db.infa_dataclass.mysql.extras.tipo_registro import TipoRegistro


@dataclass
class UnidadeMedida:
    """ classe para guardar unidades de medida"""

    um_id: int
    um_sigla: str
    um_descricao: str

    reg_valido: bool = field(init=False, default=False, metadata={'options': [True, False]})
    tp_registro: bool = field(init=False, default='CONSULTA',
                              metadata={'options': ['INCLUIR', 'ALTERAR', 'CONSULTAR']})

    def __repr__(self):
        return f"um_id:{self.um_id}\t um_sigla:{self.um_sigla}\t um_descricao:{self.um_descricao}"

    def __setattr__(self, key, value):

        match key:
            case 'um_id':
                self._validade_um_id(key, value)
            case 'um_sigla':
                self._validade_um_sigla(key, value)
            case 'um_descricao':
                self._validade_um_descricao(key, value)
            case _:
                raise ValueError(f"key:{key} value:{value} Erro:{NotImplementedError}")

    def _validade_um_id(self, key, value):
        self.__dict__[key] = int(value)
        if value == 0 or value is None:
            TipoRegistro.INCLUIR
        #     todo: rotina de incluir novo registro
        if value > 0:
            TipoRegistro.ALTERAR
    #         todo: rotina para alretar um registro

    def _validade_um_sigla(self, key, value):
        if len(value) > 0:
            # todo:  consultar se já existe esta sigla no banco de dados
            self.__dict__[key] = value
        else:
            raise ValueError(f'{key}: {value} não é um arquivo válido')

    def _validade_um_descricao(self, key, value):
        if len(value) > 0:
            # todo: consulta se já existe uma descrição no banco de dados
            self.__dict__[key] = value
        else:
            raise ValueError(f'{key}: {value} não é um arquivo válido')


um1 = UnidadeMedida(um_id=1, um_sigla='kg', um_descricao='kilograma')
print(um1)
