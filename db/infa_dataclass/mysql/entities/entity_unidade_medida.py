from dataclasses import dataclass, field

from db.infa_dataclass.mysql.extras.tipo_registro import TipoRegistro
from geral.geral import Geral


@dataclass
class EntityUnidaMedida:
    """ classe para guardar unidades de medida"""

    um_id: int = field(init=False,default=0)
    um_sigla: str = field(init=False,
                          metadata={'default': None, 'title': 'Sigla',
                                    'description': 'abreviatura da unidade de medida'})
    um_descricao: str = field(init=False,
                              metadata={'default': None, 'title': 'Descrição',
                                        'description': 'Nome da unidade de medida'})

    # reg_valido: bool = field(init=False, default=False, metadata={'options': [True, False]})
    # tp_registro: bool = field(init=False, default='CONSULTAR',
    #                           metadata={'options': ['INCLUIR', 'ALTERAR', 'CONSULTAR', 'DELETAR']})

    # def __repr__(self):
    #     return f"um_id:{self.um_id}\t um_sigla:{self.um_sigla}\t um_descricao:{self.um_descricao}"

    # def __post_init__(self):
    #     Geral.meu_logger.info(f"inicio {self.tp_registro}")
    #     match self.tp_registro:
    #         case "CONSULTAR":
    #             # todo: rotina de consulta
    #             pass
    #         case "INCLUIR":
    #             # todo: rotina de incluir
    #             pass
    #         case "ALTERAR":
    #             # todo: rotina de alterar
    #             pass
    #         case "DELETAR":
    #             # todo: rotina de delete
    #             pass
    #         case _:
    #             Geral.meu_logger.error(f"{self.tp_registro} Erro:Opção inválida")
    #             raise ValueError(f"Tipo de registro invalido:{self.tp_registro}")

    def __setattr__(self, key, value):
        Geral.meu_logger.info(f"{key}:{value}")

        match key:
            case 'um_id':
                self._validade_um_id(key, value)
            case 'um_sigla':
                self._validade_um_sigla(key, value.strip())
            case 'um_descricao':
                self._validade_um_descricao(key, value.strip())
            case _:
                Geral.meu_logger.error(f"{key}:{value} Erro:Campo não implementado")
                raise ValueError(f"key:{key} value:{value} Erro:{NotImplementedError}")

    def _validade_um_id(self, key, value):
        self.__dict__[key] = int(value)
        if value is None or value == "":
            self.__dict__[key] = 0
            TipoRegistro.INCLUIR
        #     todo: rotina de incluir novo registro
        if value > 0:
            self.__dict__[key] = value
            TipoRegistro.ALTERAR

    #      todo: rotina para alretar um registro

    def get_um_sigla_title(self):
        return self.__dataclass_fields__['um_sigla'].metadata['title']

    def get_um_sigla_description(self):
        return self.__dataclass_fields__['um_sigla'].metadata['description']

    def get_title(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['title']

    def get_description(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['description']

    def _validade_um_sigla(self, key, value):
        if len(value) > 0:
            # todo: consultar se já existe esta sigla no banco de dados
            self.__dict__[key] = value
        else:
            # self.reg_valido = False
            raise ValueError(f'{self.get_title(key)}: {value} conteúdo inválido')

    def _validade_um_descricao(self, key, value):
        if len(value) > 0:
            # todo: consulta se já existe uma descrição no banco de dados
            self.__dict__[key] = value
        else:
            # self.reg_valido = False
            raise ValueError(f'{self.get_title(key)}: {value} conteúdo inválido')

    # def traz_dicionario(self):
    #     return  asdict(EntityUnidaMedida)
# um1 = EntityUnidaMedida(um_id=1, um_sigla='kg', um_descricao='kilograma')
# print(um1)
# um2 = EntityUnidaMedida(um_id=1)
# print(um1)
