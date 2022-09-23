from db.connection import Base, engine
from db.infra_sqlalchemy.repository.unidade_medida_repository import UnidadeMedidaReposistory
from  db.infra_sqlalchemy.repository.converte_unidade_medida_repository import ConverteUnidadeMedidaReposistory

repo_um = UnidadeMedidaReposistory()
# repo_um.insert(sigla='m',descricao='metro')
data_um = repo_um.select()
print(data_um)



# repo_cum = ConverteUnidadeMedidaReposistory()
# data_cum = repo_cum.select()
# cum = data_cum
# print(data_cum)
# print(cum)
