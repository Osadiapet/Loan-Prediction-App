
import pickle
import streamlit as st

st.title('Loan Prediction Assistant')

st.markdown('This application is meant to assist banks in giving loans to clients, whether a client will repay loan on time or not based on certain factors ')
st.markdown('Please Enter the below details to know the results')

 
# loading the trained model
pickle_in = open('npontu.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Seniority, Home, Time, Age, Marital, Records, Job, Expenses, Income, Assets, Debts, Amount, Price):   
 
    # Pre-processing user input    
    if Home == 'owner':
        Home = 0
    elif Home== 'rent':
        Home=1
    elif Home == 'parent':
        Home = 2
    elif Home == 'other':
        Home = 3
    elif Home == 'priv':
        Home=4
    else:
        Home=5

    if Job == 'fixed':
        Job = 0
    elif Job == 'freelance':
        Job=1
    elif Job == 'partime':
        Job=2
    else:
        Job=3

    if Marital  == "married":
        Marital = 0
    elif Marital == 'single':
        Marital =1
    elif Marital == 'seperated':
        Marital = 2
    else:
        Marital=5


    if Records == "yes_rec":
        Records = 1
    else:
        Records = 0
 
 
    
 
    # Making predictions 
    prediction = classifier.predict([[Seniority, Home, Time, Age, Marital, Records, Job, Expenses, Income, Assets, Debts, Amount, Price]])
     
    if prediction == 0:
        pred = 'is not likely to repay loan in full and on time'
    else:
        pred = 'is likely to repay loan in full and on time '
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Osadiapet Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Seniority = st.number_input("Job Seniority (Years)")
    Home = st.selectbox("Type of Home Ownership",('Owner', 'Rent', 'Parents House', 'Other', 'Priv', 'Ignore'))
    Time=st.number_input('Time of requested loan')
    Age=st.number_input('Age (Years)')
    Marital = st.selectbox("Marital Status",('Married', 'Single', 'Seperated', 'Divorced'))
    Job = st.selectbox("Type of Job",('Fixed', 'Freelance', 'Partime', 'Others'))
    Records = st.selectbox("Existence of Records",('Yes', 'No'))
    Expenses=st.number_input('Amount of Expenses')
    Income=st.number_input('Amount of Income')
    Assets=st.number_input('Amount of Assets')
    Debts =st.number_input('Amount of Debts')
    Amount=st.number_input('Amount Requested of Loan')
    Price=st.number_input('Price of Goods')
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Seniority, Home, Time, Age, Marital, Records, Job, Expenses, Income, Assets, Debts, Amount, Price) 
        st.success('This applicant {}'.format(result))
       
if __name__=='__main__': 
    main()