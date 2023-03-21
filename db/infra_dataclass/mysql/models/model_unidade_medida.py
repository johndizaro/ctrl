from dataclasses import dataclass, field, InitVar, asdict


@dataclass
class ModelUnidadeMedida:
    a01_id: int = field(default=0,
                        metadata={'options': {'valid': False,
                                              'error': ''
                                              }
                                  }
                        )

    # a01_exemplo: str | None
    a01_sigla: str = field(default=None,
                           metadata={'options': {'title': 'Sigla',
                                                 'description': 'Sigla da unidade de medida',
                                                 'size': 2,
                                                 'valid': False,
                                                 'error': ''
                                                 }
                                     }
                           )
    a01_descricao: str = field(default=None,
                               metadata={
                                   'options': {'title': 'Descrição',
                                               'description': 'Nome por extenso da unidade de medida',
                                               'size': 30,
                                               'valid': False, 'error': ''}}
                               )

    _tp_register: InitVar[str] = field(default=None,
                                       metadata={'opt': ['INCLUIR', 'ALTERAR', 'CONSULTAR', 'DELETAR']})

    # def __enter__(self):
    #     print("executou enter")
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #
    #     print("executou exit")

    def __repr__(self):
        return f"a01_id:{self.a01_id} a01_sigla:{self.a01_sigla} a01_descricao:{self.a01_descricao} tp_register:{self._tp_register}"

    # def __post_init__(self, _tp_register: str):
    #     if self.a01_id == 0:
    #         self._tp_register = "INCLUIR"
    #     if self.a01_id > 0:
    #         self._tp_register = "ALTERAR"

    def __setattr__(self, key, value):
        match key:
            case "a01_id":
                self._validate_a01_id(key=key, value=value)
            case "a01_sigla":
                self._validate_a01_sigla(key, value)
            case "a01_descricao":
                self._validate_a01_descricao(key, value)
            case "_tp_register":
                self._validate_tp_register(key, value)
            case _:
                raise ValueError(f"campo:{key} valor:{value} Não definido")

    def _validate_a01_id(self, key, value):

        if type(value) is not int:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"campo:{key} valor:{value} deverá ser numérico")

        if value < 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'campo:{key} valor:{value} deverá um número positivo')

        self.__dataclass_fields__[key].metadata['options']['valid'] = True

        if value == 0:
            self.__dict__[key] = 0
            self._tp_register = "INCLUIR"
        if value > 0:
            self._tp_register = "ALTERAR"
            self.__dict__[key] = value

    def _validate_a01_sigla(self, key, value):

        if value == None:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            return

        if type(value) is not str:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"O campo {self.get_title(key)} tem valor {value} deverá ser fornecido e deverá ser texto")

        if value == "":
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"O campo {self.get_title(key)} deverá ser fornecido")

        self.__dict__[key] = value
        self.__dataclass_fields__[key].metadata['options']['valid'] = True

    def _validate_a01_descricao(self, key, value):

        if value == None:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            return

        if type(value) is not str:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"O campo {self.get_title(key)} tem valor {value} deverá ser fornecido e deverá ser texto")

        if value == "":
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"O campo {self.get_title(key)} deverá ser fornecido")

        self.__dict__[key] = value
        self.__dataclass_fields__[key].metadata['options']['valid'] = True

    def _validate_tp_register(self, key, value):
        self.__dict__[key] = value

    def get_title(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['title']

    def get_description(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['description']

    def get_size(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['size']

    def dic_UnidadeMedida(self):
        return asdict(self)

    def verifica_status_campo(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['valid']

    def verifica_status_final(self):
        status = True
        for campo in asdict(self):
            # print(self.__dataclass_fields__[campo].metadata['options']['valid'])
            if self.__dataclass_fields__[campo].metadata['options']['valid'] == False:
                status = False
        return status
        # return self.__dataclass_fields__[name_field].metadata['options']['valid']

@dataclass()
class LstModelUnidadeMedida:
    lst_unidade_medida: list[ModelUnidadeMedida]

# lst_a01 = [{'a01_id': -1, 'a01_sigla': 'kg', 'a01_descricao': 'kilograma'},
#          {'a01_id': 2, 'a01_sigla': 'g', 'a01_descricao': 'grama'}, ]
# b_unidade_medida = LstModelUnidadeMedida(lst_unidade_medida=lst_a01)
# print(b_unidade_medida)





# try:
#     a = ModelUnidadeMedida()
#     a.a01_sigla = "kg"
#     a.a01_descricao = "kilogtama"
#     print(a)
#     print(
#         f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
#     print(a.verifica_status_final())
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")
#
#

# try:
#     a = ModelUnidadeMedida()
#     a.a01_sigla = "g"
#     # a.a01_descricao = "kilogtama"
#     # print(a)
#     print(
#         f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
#     print(a.verifica_status_final())
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")
#


# try:
#     a = ModelUnidadeMedida()
#
#     a.a01_descricao = "AAAAAA"
#     print(a)
#     print(
#         f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
#     print(a.verifica_status_final())
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")


# lst_a01 = [{'a01_id': 1, 'a01_sigla': 'kg', 'a01_descricao': 'kilograma'},
#          {'a01_id': 2, 'a01_sigla': 'g', 'a01_descricao': 'grama'}, ]
# b_unidade_medida = LstModelUnidadeMedida(lst_unidade_medida=lst_a01)
# print(b_unidade_medida)
#
# try:
#     a = ModelUnidadeMedida()
#     a = ModelUnidadeMedida(a01_id=0, a01_sigla='l', a01_descricao='litro')
#     pprint(a)
#     a = ModelUnidadeMedida(a01_id=0, a01_sigla=None, a01_descricao=None)
#     a.a01_sigla = 'LT'
#     a.a01_descricao = "LITRO"
#     pprint(a)
#     a = ModelUnidadeMedida(a01_id=1, a01_sigla=None, a01_descricao=None)
#     pprint(a)
#     pprint(a.get_title('a01_sigla'))
#
#
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")

# try:
#     a = ModelUnidadeMedida()
#
#     a.a01_descricao = "AAAAAA"
#     print(a)
#     print(
#         f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
#     print(a.verifica_status_final())
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")
