import dataclasses
import unittest

from db.infra.models.model_unidade_medida import ModelUnidadeMedida


class TestModelUnidadeMedida(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test
        """
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test__validate_fields_type(self):
        MUM = ModelUnidadeMedida()
        self.assertEqual(MUM.__annotations__['a01_id'], int)
        self.assertEqual(MUM.__annotations__['a01_sigla'], str)
        self.assertEqual(MUM.__annotations__['a01_descricao'], str)
        # self.assertEqual(MUM.__annotations__['_tp_register'], dataclasses.InitVar[str])

    def test__validate_a01_id_numero_positivo(self):
        aaa = ModelUnidadeMedida(a01_id=1)
        self.assertEqual(aaa.a01_id, 1)

    def test__validate_a01_id_numero_alfatetico(self):
        try:
            ModelUnidadeMedida(a01_id='a')
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'campo:a01_id valor:a deverá ser numérico')

    def test__validate_a01_id_numero_negativo(self):
        try:
            ModelUnidadeMedida(a01_id=-1)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'campo:a01_id valor:-1  deverá um número positivo')

    def test__validate_a01_sigla1(self):
        try:
            ModelUnidadeMedida(a01_sigla='')
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'O campo Sigla deverá ser fornecido')

    def test__validate_a01_sigla2(self):
        try:
            ModelUnidadeMedida(a01_sigla=None)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'O campo Sigla deverá ser fornecido')

    def test__validate_a01_sigla3(self):
        try:
            ModelUnidadeMedida(a01_sigla=1)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'O campo Sigla tem valor 1 deverá ser fornecido e deverá ser texto')

    def test__validate_a01_sigla3(self):
        aaa = ModelUnidadeMedida(a01_sigla='aa')
        self.assertEqual(aaa.a01_sigla, 'aa')

    def test__validate_a01_descricao(self):
        try:
            ModelUnidadeMedida(a01_descricao='')
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'O campo Descrição deverá ser fornecido')

    def test__validate_a01_descricao1(self):
        try:
            ModelUnidadeMedida(a01_descricao=1)
        except ValueError as error:
            x = f'{error}'
            self.assertEqual(x, 'O campo Descrição tem valor 1 deverá ser fornecido e deverá ser texto')

    def test__validate_tp_register_alterar1(self):

        a = ModelUnidadeMedida(a01_id=1)
        self.assertEqual(a._tp_register, 'ALTERAR')

    def test__validate_tp_register_alterar2(self):

        a = ModelUnidadeMedida(a01_id=0)
        self.assertNotEqual(a._tp_register, 'ALTERAR')

    def test__validate_tp_register_incluir1(self):

        a = ModelUnidadeMedida(a01_id=0)
        self.assertEqual(a._tp_register, 'INCLUIR')

    def test__validate_tp_register_incluir2(self):

        a = ModelUnidadeMedida(a01_id=1)
        self.assertNotEqual(a._tp_register, 'INCLUIR')

    def test_dic_UnidadeMedida(self):
        a = ModelUnidadeMedida()
        dict_a = dataclasses.asdict(a)
        self.assertEqual(type(dict_a), dict)

    def test_verifica_status_final_1(self):
        a = ModelUnidadeMedida(a01_id=1, a01_sigla='aa', a01_descricao="aaa")
        status = a.verifica_status_final()
        self.assertEqual(status, True)

    def test_verifica_status_final_1(self):
        a = ModelUnidadeMedida(a01_id=1, a01_sigla='aa', a01_descricao="aaa")
        status = a.verifica_status_final()
        self.assertEqual(status, True)

    def test_verifica_status_final_2(self):
        a = ModelUnidadeMedida(a01_id=1, a01_descricao="aaa")
        status = a.verifica_status_final()
        self.assertEqual(status, False)

    def test_verifica_status_final_3(self):
        a = ModelUnidadeMedida(a01_id=1, a01_sigla='aa')
        status = a.verifica_status_final()
        self.assertEqual(status, False)

    def test_verifica_status_final_4(self):
        a = ModelUnidadeMedida(a01_id=1, a01_sigla='aa', a01_descricao=None)
        status = a.verifica_status_final()
        self.assertEqual(status, False)

    def test_get_title_a01_sigla(self):
        a = ModelUnidadeMedida().get_title('a01_sigla')
        self.assertEqual(a, 'Sigla')

    def test_get_title_a01_descricao(self):
        a = ModelUnidadeMedida().get_title('a01_descricao')
        self.assertEqual(a, 'Descrição')

    def test_get_description_a01_sigla(self):
        a = ModelUnidadeMedida().get_description('a01_sigla')
        self.assertEqual(a, 'Sigla da unidade de medida')

    def test_get_description_a01_descricao(self):
        a = ModelUnidadeMedida().get_description('a01_descricao')
        self.assertEqual(a, 'Nome por extenso da unidade de medida')


if __name__ == '__main__':
    unittest.TestModelUnidadeMedida()
