import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
# input
path = '/opt/airflow/tmp'
filename = 'temp_T.csv'
fn = path + '/' + filename
Host = 'db'
Port = '5432'
User = 'postgres_giz'
Password = 'giz_peerzoip'
DBName = 'django_gizb'
TableName = 'data_enercon'
# Process
    # Connection to the DB
engine = create_engine('postgresql://'+User+':'+Password+'@'+Host+':'+Port+'/'+DBName)
connection = engine.connect()
    # Verify if exist the table
try: 
    metadata_obj = MetaData()
    table_db = Table(TableName, metadata_obj, autoload=True, autoload_with=engine)
    print(table_db.columns.keys())
except:
    df = pd.read_csv(fn,index_col=0, parse_dates=True)
    pd.io.sql.get_schema(df, name = 'data_enercon',)
    df.head(0).to_sql(name='data_enercon', con=engine, if_exists='replace')