import pandas as pd
import numpy as np
from sqlalchemy import create_engine
# input
path = '/opt/airflow/tmp'
filename = 'temp_T.csv'
fn = path + '/' + filename
Host = 'db'
Port = '5432'
User = 'postgres'
Password = 'cperv_db_solar'
DBName = 'cperv'
TableName = ''
# Process
engine = create_engine('postgresql://'+User+':'+Password+'@'+Host+':'+Port+'/'+DBName)
engine.connect()
print(engine)
dr = pd.read_csv('/opt/airflow/tmp/ResumeData.csv')
df = pd.read_csv(fn,index_col=0, parse_dates=True)
print(df.info())
# print(df)
pd.io.sql.get_schema(df, name = 'data_oruro', con=engine, )
print(df.columns)
# Output
df.to_sql(name='data_oruro', con=engine, if_exists='append')