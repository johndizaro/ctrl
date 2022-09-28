from dataclasses import dataclass, field


@dataclass()
class UnidadeMedida:
    um_id: int
    um_sigla: str

    def __repr__(self):
        return f" um_id:{self.um_id} um_sigla:{self.um_sigla}"


@dataclass()
class ConUnidadeMedida:
    cum_id: int
    cum_unidade_medida_origem: UnidadeMedida
    cum_unidade_medida_destino: UnidadeMedida
    cum_calculo: str = field(metadata={'options': ['*', '/', '+', '-']})
    cum_razao: int


um1 = UnidadeMedida(um_id=1, um_sigla='kg')
um2 = UnidadeMedida(um_id=2, um_sigla='gr')

# cum1 = ConUnidadeMedida(um_id=1,um_sigla='m',um_descricao='metro',calculo='*',razao=100)
# cum1 = ConUnidadeMedida(um_id=1, um_sigla='kg', cum_calculo='*', cum_razao=100)
cum1 = ConUnidadeMedida(cum_id=1,
                        cum_unidade_medida_origem=UnidadeMedida(um_id=1, um_sigla='kg'),
                        cum_unidade_medida_destino=UnidadeMedida(um_id=2, um_sigla='gr'),
                        cum_calculo='/',
                        cum_razao=1000
                        )
print(um1)
print(um2)
print(cum1)
print(cum1.cum_unidade_medida_origem)
print(cum1.cum_unidade_medida_destino)

cum2 = ConUnidadeMedida(cum_id=0,
                        cum_unidade_medida_origem=um1,
                        cum_unidade_medida_destino=um2,
                        cum_razao=1000,
                        cum_calculo='/')
print(cum2)

# print(cum1.um_id)
# print(cum1.um_sigla)
# print(cum1.cum_calculo)
# print(cum1.cum_razao)


# print(help(UnidadeMedida))
# print(help(ConverteUnidadeMedida))
