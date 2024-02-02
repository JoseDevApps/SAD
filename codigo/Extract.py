'''
Codigo de extraccion de datos
'''
import pandas as pd
import numpy as np
from datetime import date
'''
Lectura de Base de datos para interpretar el esquema
'''
# Solicitud SQL de Tabla Parque

# Bucle For Solicitud de ESQUEMA por parque
'''
Lectura del archivo CSV en el directorio SAMBA
'''
path = 'E:/CPERv/Centralizacion de datos/DataSCADA/' #SQL DB
filename = 'Aero_10 minutos_6861_2024-01-30_2024-01-31.csv' #SQL DB
skiprows = 0 # SQL DB
source = path+'/'+filename
df = pd.read_csv(source, skiprows=skiprows,sep=';', engine='python',quotechar='"', decimal=",", parse_dates=['Hora']).replace('"','')
df.dropna(axis=1, how='all', inplace=True)
df.to_feather("QII_"+str(date.today())+".feather")
df.to_csv("QII_"+str(date.today())+".csv")