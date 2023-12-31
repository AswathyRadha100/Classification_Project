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

#------------------- import for splitting dataset-------------------
from sklearn.model_selection import train_test_split



# +
#-------------------Data prepping for Telco -------------------------------------- 


def prep_telco():
    
    # pulling data from mysql 
    telco = acquire.get_telco_data('telco_churn')
    
    # Remove rows with missing values
    telco = telco.dropna()
    
    # Remove duplicate columns
    telco = telco.loc[:, ~telco.columns.duplicated()].copy()
    
    # Convert column names to lowercase
    telco.columns = map(str.lower, telco.columns)
    
    # List of binary columns
    binary_columns = ['partner', 'dependents', 'phone_service', 'paperless_billing', 'churn']
    
    
    


    # List of categorical columns
    categorical_columns = ['multiple_lines', 'online_security', 'online_backup', 'payment_type',
                           'contract_type', 'tech_support', 'streaming_tv', 'streaming_movies',
                           'device_protection']
    
    
    
    # Preprocess categorical columns
    encoded_categorical_df = pd.get_dummies(telco[categorical_columns], dtype=int, drop_first=True)
    telco = pd.concat([telco, encoded_categorical_df], axis=1)
    
    
    
    # Preprocess binary columns
    for col in binary_columns:
        telco[f'{col.lower()}_encoded'] = telco[col].map({'Yes': 1, 'No': 0})
        

    # Encode the 'gender' column
    telco['gender_encoded'] = telco['gender'].map({'Female': 1, 'Male': 0})
    
    
    # Encode 'churn_encoded'
    telco['churn_encoded'] = telco['churn'].map({'Yes': 1, 'No': 0})
    
    # Create a binary column based on 'contract type'
    telco['contract_type_month_to_month'] = (telco['contract_type'] == 'Month-to-month').astype('int')
    
    
    
    
    # List of numerical columns
    numerical_columns = ['total_charges']
    
    # Preprocess numerical columns
    telco['total_charges'] = telco['total_charges'].str.replace(' ', '0').astype('float')
    
    
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

