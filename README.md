--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                                                      #
# **Investigating Drivers For Telco customer churn - A project on Machine Learning Classification Models**                                               
#                                                                                                                                                                      # 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Description** 

### This project aims to analyze customer churn at a Telco company to understand the factors influencing customer attrition. By building a predictive model, the project seeks to provide insights that can lead to effective retention strategies, ultimately benefiting the Telco's business.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Goal** 

###  The main goals of the Telco customer churn project are
  - &#9733; Identify Churn Drivers 
  - &#9733; Build three models, pick the best
  - &#9733; Improve customer Retention Strategies
  - &#9733; Reduce Churn Rate
  - &#9733; Enhance Customer Experience
  - &#9733; Increase Revenue and Profitability
  - &#9733; Data-Driven Decision Making
  - &#9733; Continuous Improvement

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Initial Thoughts**

### In the early stages, we're focusing on understanding Telco churn, building a predictive model from collected data, and using these insights to smartly reduce customer attrition. This foundational step sets the path for using data effectively to keep more customers and improve overall business results.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **The Plan** 

- &#9733; Acquire data from SQL:
- &#9733; Prepare data that's acquired:
       - ** Feature Selection/Engineering
           - &#9642; Encoding categorical columns
           - &#9642; Encoding binary columns
           - &#9642; preprocess_numerical_columns
- &#9733; Explore data in search of drivers of churn:
      - **  Answer the following initial questions
           - &#9642; Why are customers churning?
           - &#9642; What can stop them ?
           - &#9642; How does it affect the company?  
           - &#9642; Is the company's service quality adequate?  
           - &#9642; Is the pricing competitive?

- &#9733; Model Selection:
      - **  Choose classification algorithms 
           - &#9642; Logistic Regression
           - &#9642; Random Forest
           - &#9642; K-Nearest Neighbors (KNN)
- &#9733; Data Splitting and Model Training:
      - **  Divide the dataset into train,validate,test 
           - &#9642; Train chosen models on training dataset             
- &#9733; Model Evaluation:
      - **  Check performance of models on test/validate dataset
      - **  metrics used 
                - &#9642; accuracy
                - &#9642; precision
                - &#9642; recall
                - &#9642; F1-score
                - &#9642; ROC-AUC

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Data Dictionary** 
---------------------------------------------------------------------------------------
| Feature         | Description                                       |  Data Type    |       
| ----------------| ------------------------------------------------------------------|
|CustomerID       | Unique identifier for each customer	              |String         |
|Gender           |	Gender of the customer	                          |Categorical    |
|SeniorCitizen	  |Whether the customer is a senior citizen   	      |Binary|        |
|Partner	        |Whether the customer has a partner	                |Binary         | 
|Dependents	      |Whether the customer has dependents	              |Binary         |
|Tenure	          |Number of months the customer has stayed	          |Numeric        |
|PhoneService	    |Whether the customer has phone service	            |Binary         |
|MultipleLines	  |Whether the customer has multiple lines	          |Categorical    |
|InternetService	|Type of internet service	                          |Categorical    |
|OnlineSecurity	  |Whether the customer has online security	          |Categorical    |
|OnlineBackup	    |Whether the customer has online backup	            |Categorical    |
|DeviceProtection	|Whether the customer has device protection	        |Categorical    |
|TechSupport	    |Whether the customer has tech support	            |Categorical    |
|StreamingTV	    |Whether the customer has streaming TV	            |Categorical    |
|StreamingMovies	|Whether the customer has streaming movies	        |Categorical    |
|Contract	        |Contract term (month-to-month, one year, two year)	|Categorical    |
|PaperlessBilling	|Whether the customer uses paperless billing	      |Binary         |
|PaymentMethod	  |Payment method used by the customer	              |Categorical    |
|MonthlyCharges	  |Monthly charges for services	                      |Numeric        |
|TotalCharges	    |Total charges for services	                        |Numeric        |
|Churn	          |Whether the customer churned	                      |Binary         |
---------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Steps to Reproduce** 

## Ordered List:
     1. Clone this repo.
     2. Acquire the data from SQL DB.
     3. Run data preprocessing and feature engineering scripts
     4. Explore data using provided notebooks.
     5. Train and evaluate models using the provided notebook.
     6. Replicate the churn prediction process using the provided instructions.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Recommendations**

## Actionable strategies based on project's insights:
    - &#9733; Contract Incentives
    - &#9733; Pricing Optimization
    - &#9733; Targeted Marketing
    - &#9733; Continuous Analysis
    - &#9733; Customer Support Enhancements

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Takeaways and Conclusions** 

In conclusion, this analysis sheds light on key factors influencing customer churn at the Telco company. Contract type, service quality for DSL customers, seasonality effects, and pricing structures have emerged as significant contributors to attrition. By implementing targeted strategies, such as offering incentives for longer contracts, improving DSL service quality, and optimizing pricing, the Telco can enhance customer retention and satisfaction.

It is clear that a proactive approach to customer engagement, improved communication during critical periods, and the continuous analysis of customer behavior will play a pivotal role in reducing churn and ensuring the Telco's long-term success. By leveraging these insights and implementing the recommended actions, the Telco can cultivate lasting customer relationships and achieve sustainable business growth.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


