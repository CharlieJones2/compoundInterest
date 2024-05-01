import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

years_list = []
values_list = []
contributions = []

def compound_interest(initial_deposit, rate, years, monthly_contribution):
    # Convert years to months
    rate = rate / 100
    
    # Initialize total value
    total_value = initial_deposit
    total_contribution = initial_deposit
    
    # Calculate compound interest with monthly contributions
    for i in range(years):
        years_list.append(str(i+1))
        for j in range(12):
            total_value += monthly_contribution
            total_contribution += monthly_contribution
        contributions.append(total_contribution)
        total_value *= (1 + rate)
        values_list.append(total_value)
    
    return total_value

# Get input from the user
initial = float(input("Enter initial deposit amount: £"))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))
monthly_contribution = float(input("Enter monthly contribution amount: £"))

# Calculate total value
total_value = compound_interest(initial, rate, years, monthly_contribution)

print(f"Total value after {years} years: £{round(total_value, 2)}")
print(years_list)
print(values_list)

df = pd.DataFrame({'Year': years_list, 'Value': values_list, 'Contribution': contributions})

plt.figure()
sns.lineplot(data=df,x='Year',y='Value', label='Total Value')
sns.lineplot(data=df, x='Year', y='Contribution', label='Total Contribution')
plt.xlabel('Year')
plt.ylabel('Total Value')
plt.show()
plt.clf()