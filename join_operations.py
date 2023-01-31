import pandas as pd
from sqlalchemy import create_engine


try:
    # Connecting to postgres 
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/country_capitals_currency_db')

    # Retrieving data from postgres tables 
    capitals_data = pd.read_sql_query('select * from capitals', con=engine)
    print('Countrys with capitals and country codes: \n', capitals_data, '\n')

    currency_data = pd.read_sql_query('select * from currency', con=engine)
    print('Countrys with currency and digraph: \n', currency_data, '\n')

    # Applying Inner Join based on country
    inner_join = pd.merge(left=capitals_data, right=currency_data, how='inner', on='country')
    print('Inner Join: \n', inner_join, '\n')

    # Applying Outer Join based on country
    outer_join = pd.merge(left=capitals_data, right=currency_data, how='outer', on='country')
    print('Outer Join: \n', outer_join, '\n')

    # Applying Left Join based on country
    left_join = pd.merge(left=capitals_data, right=currency_data, how='left', on='country')
    print('Left Join: \n', left_join, '\n')

    # Applying Right Join based on country
    right_join = pd.merge(left=capitals_data, right=currency_data, how='right', on='country')
    print('Right Join: \n', right_join, '\n')

except Exception as error:
    print("Error while creating data", error)

# finally:
#     # Closing database connection
#     if engine:
#         engine.close()
#         print("Database connection is closed")
