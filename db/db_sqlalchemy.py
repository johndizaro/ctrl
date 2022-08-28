from sqlalchemy import create_engine, Integer
# from sqlalchemy.types import Numeric
# from sqlalchemy.dialects.sqlite import json

# engine = create_engine('sqlite:////home/john/Documentos/sistemas/python/desktop/gtk4/ctrl/db/ctrldb.db')
# engine = create_engine('sqlite:///:memory:')
# connection = engine.connect()

from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, create_engine)
from sqlalchemy import insert

metadata = MetaData()
unidade_medida = Table('t01_un_medida', metadata,
                       Column('t01_un_medida_id', Integer,  primary_key=True),
                       Column('t01_desc', String(20), nullable=False, index=True),
                       Column('t01_sigla', String(5), nullable=False, unique=True),
                       Column("t01_dthr_created_on", DateTime(timezone=True), default=datetime.now),
                       Column("t01_dthr_update_on", DateTime(timezone=True), default=datetime.now(),
                              onupdate=datetime.now),
                       )

# convercao_unidade_medida = Table('t02_convercao', metadata,
#                                  Column('t02_id', Integer(),  ForeignKey=True),
#                                  Column('t02_un_medida_de', Integer(), ForeignKey('t01_un_medida.t01_un_medida_id')),
#                                  Column('t02_un_medida_ate', Integer(), ForeignKey('t01_un_medida.t01_un_medida_id')),
#                                  Column('t02_calculo_convercao', String(20), nullable=False),
#                                  Column("t01_dthr_created_on", default=datetime.now),
#                                  Column("t01_dthr_update_on", default=datetime.now(), onupdate=datetime.now),
#                                  )

engine = create_engine('sqlite:///:memory:')
metadata.create_all(engine)

ins = unidade_medida.insert(t01_desc='kilograma', t01_sigla='kg')

print(ins)
