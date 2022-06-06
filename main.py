from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# df = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/mobility.csv')
# df3 = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/state_to_fips.csv')
# df2 = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/county_to_fips.csv')
# df4 = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/state_wise_cases.csv')
# df5 = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/county_wise_death.csv')
# #print(df.head())
# engine = create_engine('postgresql://postgres:SuNdArAm129@localhost:5432/postgres')
# df.to_sql('mobility', engine)
# df3.to_sql('state_to_fips', engine)
# df2.to_sql('county_to_fips', engine)
# df4.to_sql('state_wise_cases', engine)
# df5.to_sql('county_wise_death', engine)

df = pd.read_csv('Qure.ai Data Engineer Assignment Files (2) (1)/for_doc.csv')
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')
df.to_sql('for_doc', engine)