import streamlit as st
from compoundInterest import compound_interest
import pandas as pd

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
    st.write(f'After {years} years, your saving will be worth £{total_value:,.2f}, having earned interest of £{total_value-total_contribution:,.2f}')
    df = pd.DataFrame({'Year': years_list, 'Value': values_list, 'Contribution': contributions})

    st.line_chart(data=df,x='Year',y=['Value','Contribution'], color=["#268bd2","#657b83"])
    
    values_list_form = [f'£{value:,.2f}' for value in values_list]
    contributions_form = [f'£{contribution:,.2f}' for contribution in contributions]
    df_form = pd.DataFrame({'Year': years_list, 'Value': values_list_form, 'Contribution': contributions_form}, index='Year')
    st.write(df_form)
    