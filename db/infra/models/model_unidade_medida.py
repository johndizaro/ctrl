from dataclasses import dataclass, field, InitVar, asdict
from typing import Any


@dataclass
class ModelUnidadeMedida:
    a01_id: int = field(default=0,
                        metadata={'options': {'valid': False,
                                              'error': ''}}
                        )
    # a01_exemplo: str | None
    a01_sigla: str = field(default=None,
                           metadata={
                               'options': {'title': 'Sigla',
                                           'description': 'Sigla da unidade de medida',
                                           'size': 2,
                                           'valid': False,
                                           'error': ''}}
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

    def lixo(self):
        return "AAA"

    def __repr__(self):
        return f"a01_id:{self.a01_id} a01_sigla:{self.a01_sigla} a01_descricao:{self.a01_descricao} tp_register:{self._tp_register}"

    # def __post_init__(self, _tp_register: str):
    #     if self.a01_id == 0:
    #         self._tp_register = "INCLUIR"
    #     if self.a01_id > 0:
    #         self._tp_register = "ALTERAR"

    def __setattr__(self, key: str, value: Any):
        """
        Verifica se os campos referenciados estão  no dataclass
        se o campo constar na dfataclass o valor será guardfado no mesmo
        caso contrario retornará uma mensagem de erro via raise ValueError

        Parameters
        ----------
        key :  nome do campo
        value : valor do campo

        Returns
        -------

        """
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

    def _validate_a01_id(self, key: str, value: int):
        """
        Valida o campo e o valor para saberse foram definidos  na dataclass
        e verifica se o  conteúdo de value está dentro das especificações
        Caso o conteúdo de value seja  ZERO sera marcado que tratase de um registro para INCLUIR
        caso contrario ALTERAR

        Parameters
        ----------
        key : nome do campo na dataclass que receberá o valor
        value : valor a ser atribuido ao campo

        Returns: Se tudo ocorrer bem  o value será atribuido ao campo definodo pelo campo key

        se tiver algum problema retornará uma mensagem de erro
        -------

        """

        if type(value) is not int:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f"campo:{key} valor:{value} deverá ser numérico")

        if value < 0:
            self.__dataclass_fields__[key].metadata['options']['valid'] = False
            raise ValueError(f'campo:{key} valor:{value}  deverá um número positivo')

        self.__dataclass_fields__[key].metadata['options']['valid'] = True
        self.__dict__[key] = value

        if value == 0:
            self._tp_register = "INCLUIR"
        if value > 0:
            self._tp_register = "ALTERAR"

    def _validate_a01_sigla(self, key, value):
        """
        Valida o campo e o valor para saberse foram definidos  na dataclass
        e verifica se o  conteúdo de value está dentro das especificações


        Parameters
        ----------
        key : nome do campo na dataclass que receberá o valor
        value : valor a ser atribuido ao campo

        Returns: Se tudo ocorrer bem  o value será atribuido ao campo definodo pelo campo key

        se tiver algum problema retornará uma mensagem de erro via raise ValueError
        -------
        """
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
        """
        Valida o campo e o valor para saberse foram definidos  na dataclass
        e verifica se o  conteúdo de value está dentro das especificações


        Parameters
        ----------
        key : nome do campo na dataclass que receberá o valor
        value : valor a ser atribuido ao campo

        Returns: Se tudo ocorrer bem  o value será atribuido ao campo definodo pelo campo key

        se tiver algum problema retornará uma mensagem de erro via raise ValueError
        -------
        """
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

    def get_title(self, name_field: str) -> str:
        """
        recebe o nome do campo do dataclass e retornar  o TITLE  para se colocar no label do campo
        Parameters
        ----------
        name_field :  nome do campo  do dataclass para se trazer o title

        Returns uma string
        -------

        """

        return self.__dataclass_fields__[name_field].metadata['options']['title']

    def get_description(self, name_field: str) -> str:
        """
        recebe o nome do campo do dataclass e retornar  o DESCRITION  no tooltip_text do campo
        Parameters
        ----------
        name_field :  nome do campo  do dataclass para se trazer o para o tooltip_text

        Returns uma string
        -------

        """
        return self.__dataclass_fields__[name_field].metadata['options']['description']

    def get_size(self, name_field: str) -> int:
        """
        recebe o nome do campo do dataclass e retornar  o size do campo
        Parameters
        ----------
        name_field :  nome do campo  do dataclass para se trazer o texto para o size para se colocar no max_length

        Returns um integer
        -------
        """

        return self.__dataclass_fields__[name_field].metadata['options']['size']

    def dic_UnidadeMedida(self):
        return asdict(self)

    def verifica_status_campo(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['options']['valid']

    def verifica_status_final(self) -> bool:
        """
        Verifica se todos os campos estão validados e se todos estiverem corrtos retornará True
        e se tivar pelo menos um  não correto retornará False
        Returns boolean
        -------
        """

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

# lst_a = [{'a01_id': 1, 'a01_sigla': 'kg', 'a01_descricao': 'kilograma'},
#          {'a01_id': 2, 'a01_sigla': 'g', 'a01_descricao': 'grama'}, ]
# b_unidade_medida = LstModelUnidadeMedida(lst_unidade_medida=lst_a)
# pprint(b_unidade_medida)
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
#     a.a01_id = 1
#
#     # a.a01_descricao = "AAAAAA"
#
#     print(f"a01_id:{a.a01_id}")
#     # print(f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
#     # print(a.verifica_status_final())
# except (ValueError, TypeError) as erro:
#     print(f"{erro}")

# print(vars(ModelUnidadeMedida))
