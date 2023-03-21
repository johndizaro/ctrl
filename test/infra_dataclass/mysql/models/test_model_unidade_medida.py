import dataclasses
import unittest
from unittest import TestCase, mock
from unittest.mock import Mock, MagicMock, patch
from db.infra_dataclass.mysql.models.model_unidade_medida import ModelUnidadeMedida


class TestModelUnidadeMedida(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

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

        mock_ModelUnidadeMedida = ModelUnidadeMedida.__annotations__

        self.assertEqual(mock_ModelUnidadeMedida['a01_id'], int)
        self.assertEqual(mock_ModelUnidadeMedida['a01_sigla'], str)
        self.assertEqual(mock_ModelUnidadeMedida['a01_descricao'], str)

    def test_validate_a01_id_negativo(self):

        try:
            valor = ModelUnidadeMedida(a01_id=-1)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"campo:a01_id valor:-1 deverá um número positivo")

    def test_validate_a01_id_positivo(self):

        valor = ModelUnidadeMedida(a01_id=1)
        self.assertEqual(valor.a01_id, 1)

    def test_validate_incluir(self):

        a = ModelUnidadeMedida(a01_id=0)
        self.assertEqual(a._tp_register, 'INCLUIR')

    def test_validate_alterar(self):

        a = ModelUnidadeMedida(a01_id=1)
        self.assertEqual(a._tp_register, 'ALTERAR')

    def test_validate_a01_sigla(self):

        a = ModelUnidadeMedida(a01_sigla='a')
        self.assertEqual(a.a01_sigla, 'a')

    def test_validate_a01_sigla_None(self):

        a = ModelUnidadeMedida(a01_sigla=None)
        self.assertEqual(a.a01_sigla, None)

    def test_validate_a01_sigla_numero(self):
        valor = 1
        try:
            ModelUnidadeMedida(a01_sigla=valor)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"O campo Sigla tem valor {valor} deverá ser fornecido e deverá ser texto")

    def test_validate_a01_descricao(self):

        a = ModelUnidadeMedida(a01_descricao='a')
        self.assertEqual(a.a01_descricao, 'a')

    def test_validate_a01_descricao_none(self):

        a = ModelUnidadeMedida(a01_descricao=None)
        self.assertEqual(a.a01_descricao, None)

    def test_validate_a01_descricao_numero(self):
        valor = 1
        try:
            ModelUnidadeMedida(a01_descricao=valor)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, f"O campo Descrição tem valor {valor} deverá ser fornecido e deverá ser texto")


if __name__ == '__main__':
    unittest.TestModelUnidadeMedida()
