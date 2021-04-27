## predicting-The-Posibity-of-a-Client-Paying-Back-Loan-in-Full-and-on-time
This is a machine learning model to predict the possibility of a client paying back their loan in full and on time. 

# Contents
- NPONTU (1).ipynb: Jupyter notebooks to walk through data cleaning, EDA, and machine learning pipeline.

- app: npontu4.py contains the source code for Streamlit app, which deploys the machine learning model and provides results from new data.
- Requirements.txt provides the required packages to deploy the streamlit app via their github sharing service.

- model output: Storing final model deployed in the application and associated model results.

- data: Contains raw data from  and cleaned dataset used for analysis

- The raw dataset is in the file "CreditScoring.csv" which contains 4455 rows and 14 columns:

# Data Descrition
- Status:	credit status
- Seniority:	job seniority (years)
- Home:	type of home ownership
- Time:	time of requested loan
- Age:	client's age
- Marital:	marital status
- Records:	existance of records
- Job:	type of job
- Expenses:	amount of expenses
- Income:	amount of income
- Assets:	amount of assets
- Debt:	amount of debt
- Amount:	amount requested of loan
- Price:	price of good
