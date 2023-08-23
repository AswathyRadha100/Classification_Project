SELECT * FROM telco_churn.contract_types;

SELECT * FROM customers
                        LEFT JOIN contract_types
                        USING(contract_type_id)
                        LEFT JOIN internet_service_types
                        USING(internet_service_type_id)
                        LEFT JOIN payment_types
                        USING(payment_type_id)