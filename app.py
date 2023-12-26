import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('final_df.pkl','rb'))

teams = ['Australia','India','Bangladesh','New Zealand','South Africa','England','West Indies','Afghanistan','Pakistan','Sri Lanka']

cities = ['Colombo','Johannesburg','Mirpur','Dubai','London','Auckland','Cape Town','Pallekele','Barbados','Sydney','Melbourne','Durban','Harare','St Lucia','Wellington','Lauderhill','Hamilton','Centurion','Manchester','Nottingham','Abu Dhabi','Mumbai','Chittagong','Southampton','Mount Maunganui','Kolkata','Lahore','Delhi','Nagpur','Chandigarh','Adelaide','Bangalore','St Kitts','Cardiff','Christchurch','Trinidad']

st.title("Cricket Score Predictor")

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select batting team",sorted(teams))

with col2:
    bowling_teams = st.selectbox("Select bowling team",sorted(teams))

city = st.selectbox("Select City",sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_runs = st.number_input("Current Score")

with col4:
    overs = st.number_input("Overs done(Works for overs > 5)")

with col5:
    wickets = st.number_input("Wickets Out")

last_five = st.number_input("Runs scored in last 5 overs")

if st.button("Predict Score"):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    current_run_rate = current_runs/overs

    input_df = pd.DataFrame({
        'batting_team':[batting_team],'bowling_teams':[bowling_teams],'city':[city],
        'current_runs':[current_runs],'balls_left':[balls_left],'wickets_left':[wickets_left],
        'current_run_rate':[current_run_rate],'last_five':[last_five]
    })

    result = pipe.predict(input_df)
    result = str(int(result))

    st.header("Predicted Score - " + result)