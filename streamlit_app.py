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
total_value = compound_interest(initial, rate, years, monthly_contribution)[0]
total_contribution = compound_interest(initial, rate, years, monthly_contribution)[1]
st.write(f'After {years} years, your saving will be worth £{total_value}, having earned interest of £{total_value-total_contribution}')
df = pd.DataFrame({'Year': years_list, 'Value': values_list, 'Contribution': contributions})

plt.figure()
sns.lineplot(data=df,x='Year',y='Value', label='Total Value')
sns.lineplot(data=df, x='Year', y='Contribution', label='Total Contribution')
plt.xlabel('Year')
plt.ylabel('Total Value')
plt.show()
plt.clf()