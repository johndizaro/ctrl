class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        x.attr = x.attr + 1
        return x

class Lib:
    msg = "aaa"
    __init__ = None

    @classmethod
    def print_msg(cls):
        print(cls.msg)

class Geral(metaclass=Meta):
    def __init__(self):
        self.nome_geral = "john"
        self.idade_geral = 58
        self.sexo_geral = "M"
        print(f"G- nome:{self.nome_geral} idade:{str(self.idade_geral)} sexo:{self.sexo_geral} attr:{Geral.attr}")
        Lib.msg = "abc"
        Lib.print_msg()
        Lib.msg = 'ABC'


class Filho1(metaclass=Meta):
    def __init__(self):
        self.campo1_filho = "Priscila"
        self.nome_geral = 'priscila'
        self.idade_geral = 30
        self.sexo_geral = 'F'
        print(f"1- nome:{self.nome_geral} idade:{str(self.idade_geral)}  sexo:{self.sexo_geral} attr:{Filho1.attr}")
        # Filho1.attr = 200
        # g2 = Geral()
        # g2.attr = 300
        f2 = Filho2()
        print(f"11- nome:{self.nome_geral} idade:{str(self.idade_geral)}  sexo:{self.sexo_geral} attr:{Filho1.attr} {Geral.attr}")
        print(f"111- nome:{self.nome_geral} idade:{str(self.idade_geral)}  sexo:{self.sexo_geral} attr:{Filho1.attr}")
        Lib.print_msg()



class Filho2(metaclass=Meta):
    def __init__(self):


        self.nome_geral = "matheus"
        self.idade_geral = 20
        self.sexo_geral = 'M'
        Lib.print_msg()
        print(f"2- nome:{self.nome_geral} idade:{str(self.idade_geral)}  sexo:{self.sexo_geral} attr:{Filho2.attr}")








if __name__ == '__main__':
    a = Geral()
    b = Filho1()
    c = Filho2()


