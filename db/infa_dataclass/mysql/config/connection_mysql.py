import mysql
from mysql.connector import connect


class DBConnectionHandler:
    def __init__(self):
        self._host = "localhost"
        self._user = "johndizaro"
        self._password = "ao[D]t1snnMYSQL"
        self._database = 'orca'
        self._port = 3306

        self._conn = None
        self._dic_cur = dict()
        # self._connection_string = 'mysql+pymysql://root:aoDt1snnMYSQL@localhost:3306/orca'
        #### engine = create_engine('mysql+pymysql://johndizaro:ao[D]t1snnMYSQL@localhost:3306/orca')

    def _open_connection(self):

        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                port=self._port)

            # if (self._conn):
            #     # INFO_LOG("DB init success")
            #     pass
            # else:
            #     # INFO_LOG("DB init fail")
            #     pass

        except Exception as e:
            raise ValueError(f"{e}")
            self.flagConnOpen = False
            return

        return self._conn

    def execute(self, query):

        # if not self._conn:
        #     self.__open_connection()
        # # if not self._conn.is_connected:
        # #     self.__open_connection()

        self._open_connection()
        # if not self._conn.is_connected:
        self._dic_cur = self._conn.cursor(buffered=True, dictionary=True)

        self._dic_cur.execute(query)

        self._conn.commit()
        self._close_connection()
        return self._dic_cur

    def _close_connection(self):
        if self._conn.is_connected():
            self._conn.close()
