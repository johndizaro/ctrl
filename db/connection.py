from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+pymysql://root:aoDt1snnMYSQL@localhost:3306/orca')
# engine = create_engine('mysql+pymysql://johndizaro:ao[D]t1snnMYSQL@localhost:3306/orca')

print(engine)
#
conn = engine.connect()
response = conn.execute('SELECT * FROM unidade_medida;')

for row in response:
    print(row)
    print(row.sigla)

# Base = declarative_base()
#
# class unidade_medida(Base):
#

