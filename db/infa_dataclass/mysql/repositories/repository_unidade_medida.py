from db.infa_dataclass.mysql.config.connection_mysql import DBConnectionHandler


class RepositoryUnidaMedida:

    def select_one(self, id):
        cnx = DBConnectionHandler()
        registro = cnx.execute(f"""
        select  * from unidade_medida
        where id = {id};
        """)
        return registro

    def select_all(self):
        cnx = DBConnectionHandler()
        registros = cnx.execute(f"""
        select  * from unidade_medida order by sigla;
        """)
        return registros

    def incluir(self, dicionario):
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
              WHERE  id = {id};
         """.format(dados=dados, id=id)

        cnx = DBConnectionHandler()
        qt_registros = cnx.execute(sqli)
        return qt_registros
        

    def deletar(self, id):
        sqli = """
        DELETE FROM unidade_medida WHERE id = {id};
         """.format(id=id)
        cnx = DBConnectionHandler()
        qt_registros = cnx.execute(sqli)
        return qt_registros


# umr = RepositoryUnidaMedida()
# registros = umr.select_all()
# if registros:
#     for registro in registros:
#         print(registro)
# a = {'id': 1, 'sigla': 'kg', 'descricao': 'kilograma'}

# print(f"a:{a}")
# umr.incluir(dicionario=a)
# umr.alterar(dicionario=a)
# umr.deletar(id=87)
# registros = umr.select_all()
# if registros:
#     for registro in registros:
#         print(registro)
