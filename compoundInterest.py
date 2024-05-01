def compound_interest(initial_deposit, rate, years, monthly_contribution):
    years_list = []
    values_list = []
    contributions = []
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
    
    return total_value, total_contribution, years_list, values_list, contributions
