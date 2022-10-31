class Pai:
    def __init__(self, nome_pai, idade_pai):
        self.nome_pai: int = nome_pai
        self.idade_pai: str = idade_pai

        print(f"pai-{self.nome_pai}--{self.idade_pai}")


class Mae:
    def __init__(self, nome_mae, idade_mae):
        self.nome_mae: int = nome_mae
        self.idade_mae: str = idade_mae
        print(f"mae-{self.nome_mae}--{self.idade_mae}")


class Filho(Pai, Mae):
    def __init__(self, nome_filho, idade_filho):
        super(Filho, self).__init__(nome_pai="", idade_pai=2)

        self.nome_filho: int = nome_filho
        self.idade_filho: str = idade_filho
        print(f"filho-{self.nome_filho}--{self.idade_filho}")


a = Filho(nome_filho="a", idade_filho=3)
a.nome_pai = "Jorge"
a.idade_pai = 50
a.nome_mae = "karla"
a.idade_mae = 40
a.nome_filho = "Rogerio"
a.idade_filho = 5
