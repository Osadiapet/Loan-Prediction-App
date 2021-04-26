# predicting-The-Posibity-of-a-Client-Paying-Back-Loan-in-Full-and-on-time
This is a machine learning model to predict the possibility of a client paying back their loan in full and on time. 

#Contents
notebooks: Jupyter notebooks to walk through data cleaning, EDA, and machine learning pipeline.

app: live_app.py contains the source code for Streamlit app, which deploys the machine learning model and provides results from new data. Requirements.txt provides the required packages to deploy the streamlit app via their github sharing service.

model output: Storing final model deployed in the application and associated model results.

data: Contains raw data from  and cleaned dataset used for analysis

The raw dataset is in the file "CreditScoring.csv" which contains 4455 rows and 14 columns:

#Data Descrition
1 Status:	credit status
2 Seniority:	job seniority (years)
3 Home:	type of home ownership
4 Time:	time of requested loan
5 Age:	client's age
6 Marital:	marital status
7 Records:	existance of records
8 Job:	type of job
9 Expenses:	amount of expenses
10 Income:	amount of income
11 Assets:	amount of assets
12 Debt:	amount of debt
13 Amount:	amount requested of loan
14 Price:	price of good
