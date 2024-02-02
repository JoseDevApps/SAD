from datetime import datetime
import pandas as pd
import numpy as np
# funciones auxiliares
def datetime_valid(dt_str):
    try:
        datetime.fromisoformat(dt_str)
    except:
        return True
    return False

# Input
path = '/opt/airflow/tmp'
filename = 'QII_2024-02-02.feather'
date_format = '%d/%m/%Y %H:%M:%S'
# Process
fn = path + '/' + filename
df = pd.read_feather(fn)
inds = pd.isnull(df).any(1).to_numpy().nonzero()[0]
# Numero de datos nulos
NoNaN = len(inds)
# Numero de datos totales
NoData = df.shape[0]
# Numero de campos
NoFields = df.shape[1]
df.iloc[inds].to_csv('/opt/airflow/tmp/null_data.csv')
# delete null data
df.dropna(inplace=True)
# verificar cuantos datos son isodatetime
mask = [datetime_valid(a) for a in df.index]
# Output
df.to_csv('/opt/airflow/tmp/temp_T.csv')
df.to_feather('/opt/airflow/tmp/temp_T.feather')
# report null data in transform
print(df.index[0])
df_r = pd.Series({
    'Fecha': np.array(df.index[0]),
    'NoNan': np.array(NoNaN),
    'NoData':np.array(NoData),
    'NoCampos': np.array(NoFields)
})
df_r.to_csv('/opt/airflow/tmp/ResumeData.csv')