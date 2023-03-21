from db.infra_dataclass.mysql.engines.engine_converte_unidade_medida import EngineConverteUnidadeMedida
from db.infra_dataclass.mysql.engines.engine_unidade_medida import EngineUnidadeMedida
from db.infra_dataclass.mysql.extras.operacao_aritimetica import lst_dic_operacao_aritimetica
from db.infra_dataclass.mysql.extras.tipo_registro import TipoRegistro
from db.infra_dataclass.mysql.models.model_converte_unidade_medida import ModelConverteUnidadeMedida
from db.infra_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida


class WorkConverteUnidadeMedida:
    def __init__(self):

        super(WorkConverteUnidadeMedida, self).__init__()

        self.tp_registro = TipoRegistro.INCLUIR

        self.m_a01 = ModelUnidadeMedida()
        self.e_a01 = EngineUnidadeMedida()

        self.lst_dic_unidade_medida = self.e_a01.select_all()

        self.m_a02 = ModelConverteUnidadeMedida()
        self.e_a02 = EngineConverteUnidadeMedida()

        self.lst_dic_converte_medida = self.e_a02.select_all()

        self.lst_dic_operacao_aritimetica = lst_dic_operacao_aritimetica

    def calculo_canvercao(self, valor_para_converter, operacao, razao):

        try:
            novo_valor_para_converter = float(valor_para_converter)
            novo_razao = float(razao)
        except:
            raise ValueError(f"Os campos deverão ser numéricos")
        else:
            montagem_operacao = f"{novo_valor_para_converter}{operacao}{novo_razao}"
            resultado = eval(montagem_operacao)
            return f'{resultado}'

    def salvar_dados(self):

        status = self.m_a02.verifica_status_final()

        if self.m_a02.a02_id == 0 and status:
            self.e_a02.incluir(dicionario=self.m_a02.dic_ConverteUnidadeMedida())
        elif self.m_a02.a02_id > 0 and status:
            print("pode alterar")
        else:
            raise ValueError(f"Não é possivel salvar")
