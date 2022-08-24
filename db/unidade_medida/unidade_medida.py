
from dataclasses import dataclass, astuple, asdict, field

import random
import string


def generate_id():
    return "".join(random.choices(string.ascii_letters,k=12))


@dataclass(order=True)
class UnidadeMedida:
    """
    Unidade de medida
    """
    sort_index_id_unidade: int = field(init=False, repr=False)

    id_unidade: int
    desc_un_medida: str
    sigla_un_medida: str
    id_letras:  str = field(default_factory=generate_id)
    active: bool = True
    _composto: str = field(init=False, repr=False)

    def __post_init__(self):
        """
        inicializa um atributo que necessita de outro atributo
        :return:
        """
        self.sort_index_id_unidade = self.id_unidade
        self._composto = f"{self.desc_un_medida}-{self.sigla_un_medida}"


registros = [
    UnidadeMedida(id_unidade=2, desc_un_medida="metro", sigla_un_medida="m"),
    UnidadeMedida(id_unidade=1, desc_un_medida="centimetro", sigla_un_medida="cm"),
    UnidadeMedida(id_unidade=3, desc_un_medida="milimetro", sigla_un_medida="mm"),
]

sorted_registros = sorted(registros)
for registro in sorted_registros:
    print(f"registos:{registro.desc_un_medida} id:{registro.id_unidade}registro:{registro}")


# Python code to demonstrate the working of
# choice() and randrange()

# # importing "random" for random operations
# import random
#
# # using choice() to generate a random number from a
# # given list of numbers.
# print("A random number from list is : ", end="")
# print(random.choice([1, 4, 8, 10, 3]))
#
# # using randrange() to generate in range from 20
# # to 50. The last parameter 3 is step size to skip
# # three numbers when selecting.
# print("A random number from range is : ", end="")
# print(random.randrange(20, 50, 3))
