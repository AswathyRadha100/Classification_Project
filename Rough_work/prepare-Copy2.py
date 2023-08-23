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

import env
import acquire

# +
#------------------- import splitting functions-------------------
from sklearn.model_selection import train_test_split

import pandas as pd

# +
# ------------------- Split dataset into three -------------------


def split_function(df, target_varible):
    """
    The function split_data splits the original DataFrame df into training, validate and 
    test sets using the train_test_split function from the library Scikit-Learn(machine learning library in
    Python that provides tools for data preprocessing, model selection, training and evaluation).
    """
    train, test = train_test_split(df,
                                   random_state=123,
                                   test_size=.20,
                                   stratify= df[target_varible])
    
    train, validate = train_test_split(train,
                                   random_state=123,
                                   test_size=.25,
                                   stratify= train[target_varible])
    return train, validate, test


# +
# ------------------- Telco dataset ( prepping for Classification project) -------------------

def prep_telco(telco):
    '''
    The prep_telco function performs various data preprocessing steps on the Telco dataset,
    including dropping columns, encoding categorical variables, creating dummy variables,
    and converting a column to float.
    '''
    
    ### Pulling data from telco_churn ###
   # telco = acquire.get_telco_data('telco_churn')
    
    ### Lowering all column names ###
    telco.columns = map(str.lower, telco.columns)
    
    ### Drop any duplicates ###
    telco = telco.drop_duplicates()
    
    ### Encoding categorical type data ###
    categorical_columns = ['multiple_lines', 'online_security', 'online_backup', 'payment_type',
                           'contract_type', 'tech_support', 'streaming_tv', 'streaming_movies',
                           'device_protection']
    
    dummy_df = pd.get_dummies(telco[categorical_columns], dtype=int, drop_first=True)
    
    binary_columns = ['partner', 'dependents', 'phone_service', 'gender', 'paperless_billing', 'churn']
    
    for col in binary_columns:
        telco[f'{col}_binary'] = pd.get_dummies(telco[col], dtype=int, drop_first=True)
    
    telco = pd.concat([telco, dummy_df], axis=1)
    
    ### Scaling numerical data (i.e normalizing numerical data) ###
    telco['total_charges'] = telco['total_charges'].str.replace(' ', '0').astype(float)
    
    # Dropping extra columns after encoding ###
    columns_to_drop = ['online_security_No internet service', 'online_backup_No internet service',
                       'tech_support_No internet service', 'streaming_tv_No internet service',
                       'streaming_movies_No internet service', 'device_protection_No internet service',
                       'tech_support', 'device_protection']
    
    telco = telco.drop(columns=columns_to_drop)
    
    
     ### Restores a column named contract_type_month_to_month, ###
     ### which represents whether the contract type is "Month-to-month" ###
    
    telco['contract_type_month_to_month'] = (telco['contract_type'] == 'Month-to-month').astype(int)
    
    # Return the original, preprocessed 'telco' dataframe
    return telco

# -



