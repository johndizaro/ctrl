from dataclasses import dataclass, field

from db.infa_dataclass.mysql.extras.tipo_registro import TipoRegistro


@dataclass
class EntityConverteUnidadeMedida:
    """
    classe para converter uma unidade de medida em outra
    """
    cum_id: int = field(init=False, default=0)
    cum_id_sigla_origem: int = field(init=False, default=0)
    cum_id_sigla_destino: int = field(init=False, default=0)
    cum_calculo: str = field(init=False, metadata={
        'options': {'max_size': 20, 'title': 'Calculo para converção', 'description': "exemplo x*1000"}})

    def __repr__(self):
        return f"cum_id:{self.cum_id} cum_id_sigla_origem:{self.cum_id_sigla_origem} cum_id_sigla_destino:{self.cum_id_sigla_destino} cum_calculo: {self.cum_calculo}"

    def __setattr__(self, key, value):
        match key:
            case 'cum_id':
                pass
            case 'cum_id_sigla_origem':
                pass
            case 'cum_id_sigla_destino':
                pass
            case 'cum_calculo':
                pass
            case _:
                raise ValueError(f"key:{key} value:{value} Erro:{NotImplementedError}")

    def _validade_cum_id(self, key, value):
        self.__dict__[key] = int(value)
        if value is None or value == "":
            self.__dict__[key] = 0
            TipoRegistro.INCLUIR
        #     todo: rotina de incluir novo registro
        if value > 0:
            self.__dict__[key] = value
            TipoRegistro.ALTERAR

    def _validade_cum_id_sigla_origem(self, key, value):

        if value == 0:
            raise ValueError(f'Não poderá ser 0 (ZERO)')
        if key == 'cum_id_sigla_destino':
            raise ValueError(f'Não é possivel converte para a mesma unidade de medida ')

        self.__dict__[key] = value

    def _validade_cum_id_sigla_destino(self, key, value):

        if value == 0:
            raise ValueError(f'Não poderá ser 0 (ZERO)')
        if key == 'cum_id_sigla_origem':
            raise ValueError(f'Não é possivel converte para a mesma unidade de medida ')

        self.__dict__[key] = value

    def get_title(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['title']

    def get_description(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['description']

    def get_max_size(self, name_field):
        return self.__dataclass_fields__[name_field].metadata['max_size']
