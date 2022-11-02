import pandas as pd
import sqlalchemy
# import psycopg2



data_property = pd.read_csv('dataset/TR_PropertyInfo.csv')
data_user = pd.read_csv('dataset/TR_UserInfo.csv')

col_prop = {'Prop ID':'prop_id',   'PropertyCity':'property_city',  'PropertyState':'property_state'}
col_user = {'UserID':'user_id', 'UserSex':'user_sex', 'UserDevice':'user_device'}

data_property = data_property.rename(columns=col_prop)
data_user = data_user.rename(columns=col_user)

# conn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port="1234")
conn = sqlalchemy.create_engine(url='postgresql://postgres:password@localhost:1234/postgres')

data_property.to_sql('property', con=conn, index=False)
data_user.to_sql('user', con=conn, index=False)