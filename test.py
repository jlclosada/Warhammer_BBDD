import pandas as pd
from model.conexion_db import ConexionDB

data = pd.read_sql_table("/database/warhammer.db", con = ConexionDB)

print(data)
