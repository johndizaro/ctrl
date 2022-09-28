import mysql
from mysql.connector import connect


class DBConnectionHandler:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "johndizaro"
        self.__password = "ao[D]t1snnMYSQL"
        self.__database = 'orca'
        self.__port = 3306

        self.__conn = None
        self.__dic_cur = dict()
        # self.__connection_string = 'mysql+pymysql://root:aoDt1snnMYSQL@localhost:3306/orca'
        #### engine = create_engine('mysql+pymysql://johndizaro:ao[D]t1snnMYSQL@localhost:3306/orca')

    def __open_connection(self):
        print('faz connection')

        try:
            self.__conn = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                port=self.__port)

            # if (self.__conn):
            #     # INFO_LOG("DB init success")
            #     pass
            # else:
            #     # INFO_LOG("DB init fail")
            #     pass

        except Exception as e:
            raise ValueError(f"{e}")
            self.flagConnOpen = False
            return

        return self.__conn

    def execute(self, query):

        # if not self.__conn:
        #     self.__open_connection()
        # # if not self.__conn.is_connected:
        # #     self.__open_connection()

        self.__open_connection()
        # if not self.__conn.is_connected:
        self.__dic_cur = self.__conn.cursor(buffered=True, dictionary=True)

        self.__dic_cur.execute(query)

        self.__conn.commit()
        self.__close_connection()
        return self.__dic_cur

    def __close_connection(self):
        if self.__conn.is_connected():
            self.__conn.close()
