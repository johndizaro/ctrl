import dataclasses
import unittest
from unittest import TestCase, mock
from unittest.mock import Mock, MagicMock, patch
from db.infra_dataclass.mysql.models.model_converte_unidade_medida import ModelConverteUnidadeMedida


class TestModelConverteUnidadeMedida(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cum1 = ModelConverteUnidadeMedida()


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        """
        This method is called before each test
        """
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_validate_fields_type(self):

        mock_ModelConverteUnidadeMedida = ModelConverteUnidadeMedida.__annotations__

        self.assertEqual(mock_ModelConverteUnidadeMedida['a02_id'], int)
        self.assertEqual(mock_ModelConverteUnidadeMedida['a02_id_sigla_origem'], int)
        self.assertEqual(mock_ModelConverteUnidadeMedida['a02_id_sigla_destino'], int)
        self.assertEqual(mock_ModelConverteUnidadeMedida['a02_tp_operacao'], str)
        self.assertEqual(mock_ModelConverteUnidadeMedida['a02_razao'], float)

    def test_validate_a02_id_positivo(self):

        valor_atual = 1
        valor_esperado = ModelConverteUnidadeMedida(a02_id=valor_atual)
        self.assertEqual(valor_esperado.a02_id, valor_atual)

    def test_validate_a02_id_negativo(self):

        valor_atual = -1
        try:
            valor_retornado = ModelConverteUnidadeMedida(a02_id=valor_atual)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"campo:a02_id valor:{valor_atual} deverá um número positivo")

    def test_validate_a02_id_zero(self):

        valor_atual = 0
        valor_esperado = ModelConverteUnidadeMedida(a02_id=valor_atual)
        self.assertEqual(valor_esperado.a02_id, valor_atual)

    def test_validate_id_sigla_origem_positivo(self):

        valor_atual = 1
        ModelConverteUnidadeMedida.a02_id_sigla_origem = valor_atual
        valor_esperado = ModelConverteUnidadeMedida.a02_id_sigla_origem = valor_atual
        self.assertEqual(valor_esperado, valor_atual)

    def test_validate_id_sigla_origem_negativo(self):

        valor_atual = -1
        try:
            ModelConverteUnidadeMedida.a02_id_sigla_origem = valor_atual
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"campo:a02_id valor:{valor_atual} deverá um número positivo")

    def test_validate_id_sigla_origem_zero(self):

        valor_atual = 0
        ModelConverteUnidadeMedida.a02_id_sigla_origem = valor_atual
        self.assertEqual(ModelConverteUnidadeMedida.a02_id_sigla_origem, valor_atual)

    def test_validade_a02_id_sigla_destino_negativo(self):

        valor_atual = -1
        try:
            ModelConverteUnidadeMedida.a02_id_sigla_destino = valor_atual
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"campo:a02_id valor:{valor_atual} deverá um número positivo")

    def test_validade_a02_id_sigla_destino_zero(self):

        valor_atual = 0
        ModelConverteUnidadeMedida.a02_id_sigla_destino = valor_atual
        self.assertEqual(ModelConverteUnidadeMedida.a02_id_sigla_destino, valor_atual)

    def test_validade_a02_id_sigla_destino_positivo(self):

        valor_atual = 1
        ModelConverteUnidadeMedida.a02_id_sigla_destino = valor_atual
        valor_esperado = ModelConverteUnidadeMedida.a02_id_sigla_destino
        self.assertEqual(valor_esperado, valor_atual)

    def test_validade_a02_tp_operacao_invalido(self):

        operacao_atual = "i"
        cum = ModelConverteUnidadeMedida()
        try:
            cum.a02_tp_operacao = operacao_atual
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"Campo tipo operação key com conteúdo inválido")

    def test_validade_a02_tp_operacao_valido(self):

        operacao_atual =  '*'
        ModelConverteUnidadeMedida.a02_tp_operacao = operacao_atual
        operacao_esperado = ModelConverteUnidadeMedida.a02_tp_operacao
        self.assertEqual(operacao_esperado, operacao_atual)


    def test_validade_a02_razao_valido(self):

        razao_atual =  1.1
        ModelConverteUnidadeMedida.a02_razao = razao_atual
        razao_esperado = ModelConverteUnidadeMedida.a02_razao
        self.assertEqual(razao_esperado, razao_atual)

    def test_validade_a02_razao_invalido(self):

        razao_atual = "i"
        cum = ModelConverteUnidadeMedida()
        try:
            cum.a02_razao = razao_atual
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"O campo Razão para converção deverá ser numérico")



if __name__ == '__main__':
    unittest.TestModelConverteUnidadeMedida()
