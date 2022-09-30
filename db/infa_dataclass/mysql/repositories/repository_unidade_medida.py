from db.infa_dataclass.mysql.config.connection_mysql import DBConnectionHandler


class RepositoryUnidaMedida:

    def select_one(self, id):
        cnx = DBConnectionHandler()
        try:
            registro = cnx.execute(f"""
            select  * from unidade_medide
            where um_id = {id};
            """)
        except Exception as e:
            raise ValueError(f"{e}")
            return
        else:
            row = registro.fetchone()

        return row

    def select_all(self):
        """
        traz todos os registros com todos os cmapos da tabela unidade_medida or ordem de um_sigla
        Returns: Uma lista de tuplas
        """

        cnx = DBConnectionHandler()
        try:
            registros = cnx.execute(f"""
            select  * from unidade_medida order by um_sigla;
            """)
        except Exception as e:
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
        key = ", ".join(dicionario.keys())
        dados = ' ,'.join(["'%s'" % (value) for (value) in dicionario.values()])

        sqli = """
        INSERT INTO unidade_medida
              ({key})
              VALUES ({dados});
         """.format(key=key, dados=dados)

        cnx = DBConnectionHandler()
        qt_registros = cnx.execute(sqli)
        return qt_registros

    def alterar(self, dicionario):
        id = dicionario["id"]
        x = dicionario
        x.pop('id')

        dados = ', '.join(["%s = '%s'" % (key, value) for (key, value) in dicionario.items()])

        sqli = """
        UPDATE unidade_medida SET
              {dados}
              WHERE  um_id = {id};
         """.format(dados=dados, id=id)

        cnx = DBConnectionHandler()
        qt_registros = cnx.execute(sqli)
        return qt_registros

    def deletar(self, id):
        sqli = """
        DELETE FROM unidade_medida WHERE um_id = {id};
         """.format(id=id)

        cnx = DBConnectionHandler()
        try:
            qt_registros = cnx.execute(sqli)
        except Exception as e:
            raise ValueError(f"{e}")
            return

        return qt_registros
