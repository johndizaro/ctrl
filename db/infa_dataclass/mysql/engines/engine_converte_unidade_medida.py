
from db.infa_dataclass.mysql.connections.connection_mysql import DBConnectionHandler
from geral.geral import Geral

class EngineConverteUnidadeMedida:
    def __init__(self):
        self._gr = Geral()

    def select_one(self, id):
        cnx = DBConnectionHandler()
        try:
            registro = cnx.execute(f"""
            select  * from a02_converte_unidade_medida
            where a02_id = {id};
            """)
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            raise ValueError(f"{e}")
            return
        else:
            row = registro.fetchone()

        return row

    def select_all(self):
        """
        traz todos os registros com todos os cmapos da tabela unidade_medida or ordem de um_sigla
        Returns: Uma lista de dicionarios
        """

        cnx = DBConnectionHandler()
        try:
            registros = cnx.execute(f"""
            select  * from a02_converte_unidade_medida order by a02_id;
            """)
        except (Exception) as e:
            self._gr.meu_logger.error(f"{e}")
            raise ValueError(f"{e}")
            return
        else:
            rows = registros.fetchall()
        return rows



    def incluir(self, dicionario):
        """
        Args:
            dicionario: (dicionario) dicionario com os dados para incluir na table do banco de dados
        Returns:(int) quantidade de registros afetados
        """

        dicionario.pop('a02_id')

        key = ", ".join(dicionario.keys())
        dados = ' ,'.join(["'%s'" % (value) for (value) in dicionario.values()])
        try:
            sqli = """
                INSERT INTO a02_converte_unidade_medida
                      ({key})
                      VALUES ({dados});
                 """.format(key=key, dados=dados)

            cnx = DBConnectionHandler()
            qt_registros = cnx.execute(sqli)

        except (Exception) as e:
            self._gr.meu_logger.error(f"{e}")
            raise ValueError(f"{e}")
            return

        return qt_registros

