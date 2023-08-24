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

#-------------------Import custom libraries ------------------- 
import env
import acquire

#------------------- import splitting functions-------------------
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer




# +
#-------------------Data prepping for Telco -------------------------------------- 

def preprocess_categorical_columns(df, columns):
    '''
     Encoding categorical columns using one-hot encoding
    ''' 
    encoded_df = pd.get_dummies(df[columns], dtype=int, drop_first=True)
    return encoded_df

def preprocess_binary_columns(df, columns):
    '''
     Encoding binary columns by mapping 'Yes' to 1 and 'No' to 0
    '''
    for col in columns:
        df[f'{col.lower()}_encoded'] = df[col].map({'Yes': 1, 'No': 0})
    return df

    def preprocess_numerical_columns(df, columns):
      '''  
       Converting 'total_charges' to float after replacing empty spaces with '0'
      '''
    df['total_charges'] = df['total_charges'].str.replace(' ', '0').astype('float')
    return df

def encode_target_variable(df, target_column):
    '''
      Encoding the target variable by mapping 'Yes' to 1 and 'No' to 0
     ''' 
    df[f'{target_column.lower()}_encoded'] = df[target_column].map({'Yes': 1, 'No': 0})
    return df

def prep_telco():
    '''
    Pulls data from mySql server and preprocesses it for analysis.
    '''
    # pulling data from mysql 
    telco = acquire.get_telco_data('telco_churn')
    
    
    # removing duplicate columns
    telco = telco.loc[:, ~telco.columns.duplicated()].copy()
    
    # List of categorical, binary, and numerical columns
    categorical_columns = ['multiple_lines', 'online_security', 'online_backup', 'payment_type',
                           'contract_type', 'tech_support', 'streaming_tv', 'streaming_movies',
                           'device_protection']
    binary_columns = ['partner', 'dependents', 'phone_service', 'paperless_billing', 'churn']
    
    numerical_columns = ['total_charges']

    # Preprocess categorical columns
    encoded_categorical_df = preprocess_categorical_columns(telco, categorical_columns)
    telco = pd.concat([telco, encoded_categorical_df], axis=1)

    # Preprocess binary columns
    telco = preprocess_binary_columns(telco, binary_columns)
    

    # Encode the 'gender' column
    telco['gender_encoded'] = telco['gender'].map({'Female': 1, 'Male': 0})

    
    
    # Preprocess numerical columns
    telco = preprocess_numerical_columns(telco, numerical_columns)
    
    
    # Encode target variable
    telco = encode_target_variable(telco, 'churn')

    # Create a binary column based on 'contract type'
    telco['contract_type_month_to_month'] = (telco['contract_type'] == 'Month-to-month').astype('int')
    
    
    # Convert column names to lowercase
    telco.columns = map(str.lower, telco.columns)

    return telco


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
# -





