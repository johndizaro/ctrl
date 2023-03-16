
from db.infra_dataclass.mysql.connections.connection_mysql import DBConnectionHandler
from geral.geral import Geral


class EngineUnidadeMedida:

    def __init__(self):
        self._gr = Geral()

    def select_one(self, id):
        cnx = DBConnectionHandler()
        try:
            registro = cnx.execute(f"""
            select  * from a01_unidade_medida
            where a01_id = {id};
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
            select  * from a01_unidade_medida order by a01_sigla;
            """)
        except Exception as e:
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

        dicionario.pop('a01_id')

        key = ", ".join(dicionario.keys())
        dados = ' ,'.join(["'%s'" % (value) for (value) in dicionario.values()])
        try:
            sqli = """
                INSERT INTO a01_unidade_medida
                      ({key})
                      VALUES ({dados});
                 """.format(key=key, dados=dados)

            cnx = DBConnectionHandler()
            qt_registros = cnx.execute(sqli)

        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            raise ValueError(f"{e}")
            return

        return qt_registros

    def alterar(self, dicionario):
        id = dicionario["a01_id"]
        x = dicionario
        x.pop('a01_id')

        dados = ', '.join(["%s = '%s'" % (key, value) for (key, value) in dicionario.items()])
        try:
            sqli = """
            UPDATE a01_unidade_medida SET
                  {dados}
                  WHERE  a01_id = {id};
             """.format(dados=dados, id=id)

            cnx = DBConnectionHandler()
            qt_registros = cnx.execute(sqli)
        except Exception as e:
            self._gr.meu_logger.error(f"{e}")
            raise ValueError(f"{e}")
            return

        return qt_registros

    def deletar(self, id):
        sqli = """
        DELETE FROM a01_unidade_medida WHERE a01_id = {id};
         """.format(id=id)

        cnx = DBConnectionHandler()
        try:
            qt_registros = cnx.execute(sqli)
        except Exception as e:
            self._gr.meu_logger.error("{e}")
            raise ValueError(f"{e}")
            return

        return qt_registros

# engine_unidade_medida = EngineUnidadeMedida()
# a = engine_unidade_medida.select_all()
# print(a)
# b = engine_unidade_medida.select_one(5)
# print(b)
# dic_c = {'a01_id': 5, 'a01_sigla': 'g', 'a01_descricao': 'grama'}
#
# try:
#     c = engine_unidade_medida.incluir(dicionario=dic_c)
# except (Exception) as error:
#     print({error})
# else:
#     print(c)


