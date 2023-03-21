from db.infra_dataclass.mysql.engines.engine_unidade_medida import EngineUnidadeMedida
from db.infra_dataclass.mysql.extras.tipo_registro import TipoRegistro
from db.infra_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida


class WorkUnidadeMedida:
    def __init__(self):

        super(WorkUnidadeMedida, self).__init__()

        self.tp_registro = TipoRegistro.INCLUIR

        self.m_a01 = ModelUnidadeMedida()
        self.e_a01 = EngineUnidadeMedida()

        self.lst_dic_unidade_medida = self.e_a01.select_all()

    def salvar_dados(self):
        status = self.m_a01.verifica_status_final()

        if self.m_a01.a01_id == 0 and status:
            self.e_a01.incluir(dicionario=self.m_a01.dic_UnidadeMedida())
        elif self.m_a01.a01_id > 0 and status:
            print("pode alterar")
        else:
            raise  ValueError(f"Não é possivel salvar")



a = ModelUnidadeMedida()
w = WorkUnidadeMedida()
try:
    a.a01_sigla = "aa"
    a.a01_descricao = "aaaaa"
    print(a)
    print(
        f"a01_id:{a.verifica_status_campo('a01_id')} - a01_sigla:{a.verifica_status_campo('a01_sigla')} - a01_descricao:{a.verifica_status_campo('a01_descricao')}")
    print(a.verifica_status_final())
except (ValueError, TypeError) as erro:
    print(f"{erro}")
else:
    print(a.dic_UnidadeMedida())
#
w.salvar_dados()