from dataclasses import dataclass, field, asdict

from db.infra_dataclass.mysql.extras.operacao_aritimetica import dic_operacao_aritimetica


@dataclass()
class ModelConverteUnidadeMedida:
    """
    classe para converter uma unidade de medida em outra
    """
    a02_id: int = field(default=0,
                        metadata={'options': {'valid': False,
                                              'error': ''}
                                  }
                        )

    a02_id_sigla_origem: int = field(init=False,
                                     repr=True,
                                     default=0,
                                     metadata={'options': {'title': 'Unidade de Medida para converção',
                                                           'description': 'Selecione um unidade de medida para ser convertida',
                                                           'valid': False,
                                                           'error': ''}
                                               }
                                     )
    a02_id_sigla_destino: int = field(init=False,
                                      repr=False,
                                      default=0,
                                      metadata={'options': {'title': 'Unidade de Medida para a qual será convertido',
                                                            'description': 'Selecione um unidade de medida para a qual deve ser convertido',
                                                            'valid': False,
                                                            'error': ''}
                                                }
                                      )

    a02_tp_operacao: str = field(init=False,
                                 repr=False,
                                 default=None,
                                 metadata={'options': {'title': 'Operação',
                                                       'description': 'Operação aritimética para converção[*, /, +, -]',
                                                       'valid': False,
                                                       'error': ''}
                                           })
    a02_razao: float = field(init=False,
                             repr=False,
                             default=0.0,
                             metadata={'options': {'title': 'Razão para converção',
                                                   'description': 'Valor numérico  para converção de uma unidade de medida para outra',
                                                   'size': 30,
                                                   'valid': False,
                                                   'error': ''}
                                       }
                             )

    def __repr__(self):
        return f"a02_id:{self.a02_id} a02_id_sigla_origem:{self.a02_id_sigla_origem} a02_id_sigla_destino:{self.a02_id_sigla_origem} a02_tp_operacao:{self.a02_tp_operacao}, a02_razao:{self.a02_razao}"

    def __setattr__(self, key, value):
        match key:
            case 'a02_id':
                self._validade_a02_id(key, value)
            case 'a02_id_sigla_origem':
                self._validade_a02_id_sigla_origem(key, value)
            case 'a02_id_sigla_destino':
                self._validade_a02_id_sigla_destino(key, value)
            case 'a02_tp_operacao':
                self._validade_a02_tp_operacao(key, value)
            case 'a02_razao':
                self._validade_a02_razao(key, value)
            case _:
                raise ValueError(f"Campo {key} com valor{value} Erro:{NotImplementedError}")

    def _validade_a02_id(self, key, value: int):

        if type(value) is not int:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"campo:{key} valor:{value} deverá ser numérico")

        if value < 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False

            raise ValueError(f'campo:{key} valor:{value} deverá um número positivo')

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = value


    def _validade_a02_id_sigla_origem(self, key, value: int):

        if type(value) is not int:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"campo:{key} valor:{value} deverá ser numérico")

        if value < 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'campo:{key} valor:{value} deverá um número positivo')

        if value == 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'Não poderá ser 0 (ZERO)')

        if value == self.a02_id_sigla_destino:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'Não é possivel converte para a mesma unidade de medida ')

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = value

    def _validade_a02_id_sigla_destino(self, key, value: int):

        if type(value) is not int:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"campo:{key} valor:{value} deverá ser numérico")

        if value < 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'campo:{key} valor:{value} deverá um número positivo')

        if value == 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'Não poderá ser 0 (ZERO)')

        if value == self.a02_id_sigla_destino:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'Não é possivel converte para a mesma unidade de medida ')

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = value

    def _validade_a02_tp_operacao(self, key, value):

        # if value == None:
        #     self.__dataclass_fields__[key].metadata['options']['valid'] = False
        #     raise ValueError(f"O campo {self.get_title(key)} deverá ser especificado")

        if (value not in dic_operacao_aritimetica.values()):
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"Campo tipo operação key com conteúdo inválido")

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = value

    def _validade_a02_razao(self, key, value: int | float):

        try:
            vlr_convertido = float(value)
        except:
            raise ValueError(f"O campo {self.get_title(key)} deverá ser numérico")

        # if not isinstance(value,int) and not isinstance(value, float):
        #     self.__dataclass_fields__[key].metadata['options']['valid'] = False
        #     raise ValueError(f"O campo {self.get_title(key)} tem valor {value} deverá ser números")

        if vlr_convertido == 0.0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            return

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = float(vlr_convertido)

    def get_title(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['title']

    def get_description(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['description']

    def get_size(self, name_field):
        if 'size' not in self.__dataclass_fields__[name_field].metadata['options']:
            return None
        return self.__dataclass_fields__[name_field].metadata['options']['size']

    def verifica_status_final(self):
        status = True
        for campo in asdict(self):
            if self.__dataclass_fields__[campo].metadata['options']['valid'] == False:
                status = False
        return status

    def dic_ConverteUnidadeMedida(self):
        return asdict(self)


@dataclass()
class Listclass:
    my_array: list[ModelConverteUnidadeMedida]

#
# print(TipoRegistro.INCLUIR)
#
# lst_a02 = [{'a02_id': 1, 'a02_id_sigla_origem': 2, 'a02_id_sigla_destino': 3, 'a02_tp_operacao': '*','a02_razao': 1000},
#      {'a02_id': 2, 'a02_id_sigla_origem': 3, 'a02_id_sigla_destino': 4, 'a02_tp_operacao': '/', 'a02_razao': 1.5}]
# b_converte_unidade_medida = Listclass(my_array=lst_a02)
# print(lst_a02)
# print(b_converte_unidade_medida)
# for registro in b_converte_unidade_medida.my_array:
#     print(registro)
# #
# cum1 = ModelConverteUnidadeMedida()
# cum1.a02_id = 1
# cum1.a02_id_sigla_destino = 10
# cum1.a02_id_sigla_origem = 11
# cum1.a02_tp_operacao = "p"
# cum1.a02_razao = 2.5
# print(f"valor calculado {cum1.calculo_canvercao(10)}")
# print(cum1)
# cum1 = None
# print(cum1)

# cum3 = ModelConverteUnidadeMedida()
# cum3.a02_id = 3
# cum3.a02_id_sigla_destino = 10
# cum3.a02_id_sigla_origem = 11
# cum3.a02_tp_operacao = "*"
# cum3.a02_razao = 2
# print(f"valor calculado {cum3.calculo_canvercao(10)}")
# print(cum3)
#
# cum2 = ModelConverteUnidadeMedida()
# cum2.a02_id = 2
# cum2.a02_id_sigla_destino = 10
# cum2.a02_id_sigla_origem = 11
# cum2.a02_tp_operacao = "*"
# cum2.a02_razao = .5
# print(f"valor calculado {cum2.calculo_canvercao(10)}")
# print(cum2)
# #
# mylist = [cum1, cum2, cum3]
# print(mylist)
#
#
#
# a = [{'a02_id': 1, 'a02_id_sigla_origem': 2, 'a02_id_sigla_destino': 3, 'a02_tp_operacao': '*','a02_razao': 1000},
#      {'a02_id': 2, 'a02_id_sigla_origem': 3, 'a02_id_sigla_destino': 4, 'a02_tp_operacao': '/', 'a02_razao': 1.5},
#      asdict(cum1), asdict(cum2), asdict(cum3),]
#
#
# b = Listclass(my_array=a)
# print(b)
#
# # mylist.sort()
# #
# # print(mylist)
