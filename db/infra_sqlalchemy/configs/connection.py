from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'mysql+pymysql://root:aoDt1snnMYSQL@localhost:3306/orca'
        #### engine = create_engine('mysql+pymysql://johndizaro:ao[D]t1snnMYSQL@localhost:3306/orca')
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        """
        usado para executar um SQL na mão
        :return:
        """
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close
