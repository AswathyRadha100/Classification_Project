# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#------------------- Tabular data imports------------------- 
import pandas as pd
import numpy as np
#-------------------Import custom library ------------------- 
import env
#-------------------Import operating system interactions------
import os
#-------------------Import SQLAlchemy--------------------------
from sqlalchemy import create_engine, text



def get_telco_data(database='telco_churn',user=env.user, password=env.password, host=env.host):
    '''
    Grabs telco data from codeup mySQL database and returns a dataframe
    
    '''
    query ='SELECT * FROM customers AS cc LEFT OUTER JOIN customer_subscriptions AS cs ON cc.customer_id = cs.customer_id\
        LEFT OUTER JOIN internet_service_types AS ist ON cc.internet_service_type_id = ist.internet_service_type_id\
        LEFT OUTER JOIN payment_types AS pt ON cc.payment_type_id = pt.payment_type_id\
        LEFT OUTER JOIN contract_types AS ct ON cc.contract_type_id = ct.contract_type_id;'
    connection = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    df = pd.read_sql(query, connection)
    return df
# -












