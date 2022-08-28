from typing import Type
import dataclasses
import sqlite3
from dataclasses import dataclass, field, astuple, asdict


@dataclass(order=True)
class UnidadeMedidaData:
    """
    dados da tabela de unidade de medida
    """
    sort_index_t01_id_unidade_medida: int = field(init=False, repr=False)

    t01_id_unidade_medida: int
    t01_desc: str
    t01_sigla: str

    valido: bool = field(init=False)
    tem_registro: bool = field(init=False)

    def validar(self):
        valido = True

        if self.t01_id_unidade_medida == 0 or not self.t01_id_unidade_medida:
            valido = False
        if len(self.t01_desc) == 0:
            valido = False
        if len(self.t01_sigla) == 0:
            valido = False

        return valido

    def __post_init__(self):
        """
        inicializa um atributo que necessita de outro atributo
        :return:
        """
        self.sort_index_t01_id_unidade_medida = self.t01_id_unidade_medida
        self.valido = self.validar()


@dataclass
class UnidadeMedidaList:
    mydict: dict()
    mylist: list[dict] = field(init=False, default_factory=list)

    def __post_init__(self):
        print(f"self.mydict: {self.mydict}")
        self.mylist.append(self.mydict)
        print(f"self.mylist: {self.mylist}")
        # self.mylist.append(self.mydict)


class UnidadeMedida:

    def __init__(self):
        self.flagConnOpen = False

    def open_conn(self, db_file):
        if (not self.flagConnOpen):
            conn = sqlite3.connect(db_file)
            self.flagConnOpen = True

    def close_conn(self, db_file, conn):
        try:
            conn.close()
        except Exception as error:
            print(error)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as error:
            print(error)

        return conn

    def insert(self, conn, dictionary):
        """
        Create a new project into the projects table
        :param conn:
        :param dictionary:
        :return: lastrowid
        """
        sql = ''' INSERT INTO t01_unidade_medida(t01_desc,t01_sigla)
                  VALUES(?,?) '''
        cur = conn.cursor()
        try:
            with cur:
                cur.execute(sql, dictionary)
        except sqlite3.IntegrityError as error:
            print(error)

        conn.commit()
        return cur.lastrowid


lista = []


def montar_lista_dict(dicionario):
    lista.append(dicionario)

    # UnidadeMedidaList.mylist.append(dicionario)


# um = UnidadeMedida(t01_id_unidade_medida=1, t01_desc="kilograma", t01_sigla="Kg")
# montar_lista_dict(dataclasses.asdict(um))
#
# um = UnidadeMedida(t01_id_unidade_medida=2, t01_desc="grama", t01_sigla="gr")
# montar_lista_dict(dataclasses.asdict(um))
#
# um = UnidadeMedida(t01_id_unidade_medida=3, t01_desc="unidade", t01_sigla="un")
# montar_lista_dict(dataclasses.asdict(um))
# print(lista)
#
# UnidadeMedidaList.mylist = lista
# print(UnidadeMedidaList.mylist)

#
um1 = UnidadeMedidaData(t01_id_unidade_medida=1, t01_desc="kilograma", t01_sigla="Kg")
um2 = UnidadeMedidaData(t01_id_unidade_medida=2, t01_desc="grama", t01_sigla="gr")
um3 = UnidadeMedidaData(t01_id_unidade_medida=3, t01_desc="unidade", t01_sigla="un")

um1d = dataclasses.asdict(um1)
um2d = dataclasses.asdict(um2)
um3d = dataclasses.asdict(um3)

registros_unidademedida = UnidadeMedidaList([um1d, um2d, um3d])
#

#
# registros = [
#     UnidadeMedida(t01_id_unidade_medida=1, t01_desc="kilograma", t01_sigla="Kg"),
#     UnidadeMedida(t01_id_unidade_medida=2, t01_desc="grama", t01_sigla="gr"),
#     UnidadeMedida(t01_id_unidade_medida=3, t01_desc="unidade", t01_sigla="un"),
# ]
#
# sorted_registros = sorted(registros)
# for  registro in sorted_registros:
#     print(f"{registro.t01_id_unidade_medida} - {registro.t01_desc} - {registro.t01_sigla}")

# dic_um = dict()
# dica = dataclasses.asdict(
#    obj= UnidadeMedida(t01_id_unidade_medida=1, t01_desc="kilograma", t01_sigla="Kg"),
#     dict_factory=dic_um
# )
#
# print(dica)

# listaA = []
# umA = UnidadeMedida(t01_id_unidade_medida=1, t01_desc="kilograma", t01_sigla="Kg")
# listaA.append(dataclasses.astuple(obj=umA))
# umA = UnidadeMedida(t01_id_unidade_medida=2, t01_desc="grama", t01_sigla="gr")
# listaA.append(dataclasses.astuple(obj=umA))
#
# print(listaA)



# @dataclass
# class MyDataclass(DataclassFromDict):
#     name_in_dataclass: str = field_from_dict("nameInDictionary")
#
# origin_dict = {
#     "nameInDictionary": "field value"
# }
#
# dataclass_instance = MyDataclass.from_dict(origin_dict)
#
# >>> dataclass_instance.name_in_dataclass
# "field value"




# from dataclasses import dataclass
# from dacite import from_dict
#
# @dataclass
# class User:
#     name: str
#     age: int
#     is_active: bool
#
# data = {
#     'name': 'john',
#     'age': 30,
#     'is_active': True,
# }
#
# user = from_dict(data_class=User, data=data)
#
# assert user == User(name='john', age=30, is_active=True)


# class Pai(object):
#     def __init__(self, peso, altura):
#         self.peso = peso
#         self.altura = altura
#
#
# class Filha(Pai):
#     def __init__(self, peso, altura, cabelo):
#         super().__init__(peso, altura)
#         self.cabelo = cabelo

