import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/orca')
connection = engine.connect()
results = engine.execute('select * from unidade_medida;')
first_result = results.fetchone()

import pandas as pd
query = 'select * from unidade_medida'
post_df = pd.read_sql_query(query,engine)


