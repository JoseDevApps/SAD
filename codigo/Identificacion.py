'''
Codigo fuente para identificacion del tipo, codificacion, 
tipo de archivo
'''
import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
##########################################
#          Lectura base de datos
##########################################
# Parametros de conexion db
Host = 'db'
Port = '5432'
User = 'postgres_giz'
Password = 'giz_peerzoip'
DBName = 'django_gizb'
# Conexion a la base de datos
engine = create_engine('postgresql://'+User+':'+Password+'@'+Host+':'+Port+'/'+DBName)
engine.connect()
print(engine)
# Captura del array de datos con los path
data_sql = []
##########################################
#          Listado de archivos
##########################################
# path = ''
# list_files = os.listdir(path)