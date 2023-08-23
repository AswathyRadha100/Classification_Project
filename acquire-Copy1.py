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

import os
import pandas as pd
import numpy as np
import env
from sqlalchemy import create_engine, text



def get_telco_data(database='telco_churn',user=env.user, password=env.password, host=env.host):
    '''
    Grabs telco data from codeup mySql database.
    Returns as dataframe.
    '''
    query ='SELECT * FROM customers AS cc LEFT OUTER JOIN customer_subscriptions AS cs ON cc.customer_id = cs.customer_id\
        LEFT OUTER JOIN internet_service_types AS ist ON cc.internet_service_type_id = ist.internet_service_type_id\
        LEFT OUTER JOIN payment_types AS pt ON cc.payment_type_id = pt.payment_type_id\
        LEFT OUTER JOIN contract_types AS ct ON cc.contract_type_id = ct.contract_type_id;'
    connection = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    df = pd.read_sql(query, connection)
    return df


# +
import os
import pandas as pd
import numpy as np
import env
from sqlalchemy import create_engine, text

##############################################################################


# -
# Get telco data 
# def get_telco_data():
#    sql_query = ("SELECT * from customers JOIN contract_types USING (contract_type_id) JOIN internet_service_types USING (internet_service_type_id) JOIN payment_types USING (payment_type_id)")
#    # Read in dataframe from Codeup db
#    df = pd.read_sql(sql_query,env.get_db_url(env.user,env.host,env.password,'telco_churn'))
#    return df


def get_telco_data():
    '''
       Grabs telco data from codeup mySql database
    
    '''
    sql_query = ("SELECT * FROM customers AS cc LEFT OUTER JOIN customer_subscriptions AS cs ON cc.customer_id = cs.customer_id LEFT OUTER JOIN internet_service_types AS ist ON cc.internet_service_type_id = ist.internet_service_type_id LEFT OUTER JOIN payment_types AS pt ON cc.payment_type_id = pt.payment_type_id LEFT OUTER JOIN contract_types AS ct ON cc.contract_type_id = ct.contract_type_id")
    # Read in dataframe from Codeup db
    df = pd.read_sql(sql_query,env.get_db_url(env.user,env.host,env.password,'telco_churn'))
    return df








