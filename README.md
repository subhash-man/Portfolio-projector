## Project Summary
This project is a financial analysis tool designed to simulate and evaluate different financial scenarios for a given portfolio. The tool processes input data related to a user's financial situation, including savings, expenses, tax rates, and portfolio allocations. It then applies various scenarios to this data to determine the potential outcomes and identify any years where the portfolio might fail (i.e., run out of funds).

## Key Components
- Input Data Processing (input_to_internal function in utils.py):

  - `Allocations Validation`: Ensures that the sum of equity and fixed income allocations is exactly 100%.
  - `Data Transformation`: Converts input data into an internal data structure for further processing.
  - `Savings and Expenses Handling`: Zeroes out savings if the user is retired and adds lifestyle expenses to withdrawals only once per year.

- Scenario Application (apply_scenario function in scenario.py):

  - `Initial Setup`: Initializes the financial data dictionary with the input data.
  - `Yearly Processing`: Iterates through each year, updating the portfolio value based on savings, withdrawals, and returns from equity and fixed income investments.
  - `Failure Detection`: Checks if the portfolio value becomes negative in any year, marking the scenario as failed and recording the year of failure.

- Main Execution (main function in main.py):

  - `Input Reading`: Reads input data and scenarios from specified files.
  - `Scenario Execution`: Applies each scenario to the financial data and prints the result, including the year of failure if applicable.
  - `Summary Printing`: Outputs a summary of the total number of scenarios, and how many succeeded or failed.

- Salient Points
  - `Savings`: Savings are zeroed out if the user is retired, as it is assumed that no further savings will be made post-retirement.
  - `Expenses`: Lifestyle expenses are added to withdrawals only once per year to account for the user's cost of living.
  - `Tax Rate`: The tax rate applied to the portfolio depends on whether the user is pre-retirement or post-retirement.
  - `Portfolio Allocation`: The tool ensures that the total allocation of equity and fixed income investments is 100%.
  - `Scenario Goals`: The primary goal of running multiple scenarios is to evaluate the robustness of the portfolio under different conditions and identify any potential years of failure.

- Example Usage
To run the tool, execute the main.py script with the input file and scenarios file as arguments:

```
python main.py input.json scenarios.json
```

This will process the input data, apply each scenario, and print the results along with a summary of the scenario outcomes.


## Files and Directories

- `src/`: Contains the source code for the project.
  - `main.py`: The main script to run the financial simulations.
  - `utils.py`: Utility functions for data processing.
  - `scenario.py`: Functions to apply financial scenarios.
  - `financialdata.py`: Defines the `FinancialData` class.
  - `savings.py`: Contains the `Savings` class for savings calculations.
- `tests/`: Contains unit tests for the project.
  - `test_main.py`: Unit tests for the `main.py` script.
  - `test_utils.py`: Unit tests for the utility functions.
- `test/`: Contains test input files.
  - `input.json`: Sample input data for the financial simulations.
  - `scenarios.json`: Sample scenarios data for the financial simulations.
- `README.md`: This file.

## Installation

1. Clone the repository:

  git clone https://github.com/yourusername/income-expense-scheduler.git
  cd income-expense-scheduler

2. Install the required dependencies:

  pip install -r requirements.txt

## Usage
To run the financial simulations, use the following command:

python src/main.py test/input.json test/scenarios.json

This will read the input data from input.json and the scenarios data from test/scenarios.json, and print the results to the console.

## Running Tests
To run the unit tests, use the following command:

python -m unittest discover -s tests

This will discover and run all the tests in the tests directory.

## Sample Input Data
Here is a sample input.json file:

{
    "initial_portfolio_value": 400000,
    "retirement_year": 2030,
    "pre_retirement_tax": 0.1,
    "post_retirement_tax": 0.05,
    "equity_allocation": 0.3, 
    "fixed_income_allocation": 0.7,
    "lifestyle_expenses": 30000,
    "end_analysis_year": 2055,
    "data": [
        {"years": "2023-2025", "savings": 10000, "withdrawals": 3000, "post_tax": false},
        {"years": "2024-2026", "savings": 5000, "withdrawals": 3200, "post_tax": true},
        {"years": "2025-2027", "savings": 4000, "withdrawals": 3500},
        {"years": "2026-2028", "savings": 7500, "withdrawals": 3700, "post_tax": false},
        {"years": "2027-2029", "savings": 7000, "withdrawals": 4000, "post_tax": true},
        {"years": "2028-2030", "savings": 8000, "withdrawals": 4200, "post_tax": false},
        {"years": "2029-2031", "savings": 6000, "withdrawals": 4500, "post_tax": true}
    ]
}

## Sample Scenarios Data
Here is a sample scenarios.json file:
[
    {
        "scenario_id": 1,
        "years": [
            {"year": 2023, "equity_return": 0.1, "fixed_income_return": 0.05},
            {"year": 2024, "equity_return": 0.1, "fixed_income_return": 0.05},
            {"year": 2025, "equity_return": 0.1, "fixed_income_return": 0.05}
        ]
    }
]

## License
This project is licensed under the MIT License. See the LICENSE file for details.
