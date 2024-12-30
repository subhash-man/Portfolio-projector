import json
import random

# Define the ranges for equity and fixed income returns
equity_return_range = (-0.25, 0.3)
fixed_income_return_range = (-0.05, 0.1)

# Generate 100 scenarios
scenarios = []
start_year = 2023
num_scenarios = 100
num_years = 100

for scenario_id in range(num_scenarios):
    years = []
    for i in range(num_years):
        year = start_year + i
        equity_return = round(random.uniform(*equity_return_range), 2)
        fixed_income_return = round(random.uniform(*fixed_income_return_range), 2)
        years.append({
            "year": year,
            "equity_return": equity_return,
            "fixed_income_return": fixed_income_return
        })
    scenarios.append({"scenario_id": scenario_id + 1, "years": years})

# Write the data to scenarios.json
with open('scenarios.json', 'w') as f:
    json.dump(scenarios, f, indent=4)