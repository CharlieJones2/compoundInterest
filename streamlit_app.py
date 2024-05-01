import streamlit as st
from compoundInterest import compound_interest
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

years_list = []
values_list = []
contributions = []

st.title('Compound Interest Calculator')
initial = float(st.number_input("Enter initial deposit amount(£): ",min_value=0, max_value=1000000, step=1))
rate = float(st.number_input("Enter annual interest rate (%): ", min_value=0, max_value=100, value=5, step=1))
years = int(st.number_input("Enter number of years: ", min_value=1, max_value=150, step=1))
monthly_contribution = float(st.number_input("Enter monthly contribution amount(£): ", min_value=0, max_value=1000000))

# Calculate total value
if 'calculatePressed' not in st.session_state:
    st.session_state.buttonPressed = False
calculate = st.button('Calculate')
calculatePressed = False

if calculate:
    st.session_state.calculate = True
    st.session_state.calculatePressed = True

    total_value, total_contribution, years_list, values_list, contributions = compound_interest(initial, rate, years, monthly_contribution)
    st.write(f'After {years} years, your saving will be worth £{round(total_value,2)}, having earned interest of £{round(total_value-total_contribution,2)}')
    df = pd.DataFrame({'Year': years_list, 'Value': values_list, 'Contribution': contributions})

    st.line_chart(data=df,x='Year',y='Value', color="#268bd2")