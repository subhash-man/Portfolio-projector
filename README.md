# Income Expense Scheduler

This project is designed to simulate financial scenarios based on input data and various financial parameters. It calculates the financial outcomes for different scenarios and provides a summary of the results.

## Project Structure

income-expense-scheduler/ 
│ ├── src/ 
  │ ├── main.py 
  │ ├── utils.py 
  │ ├── scenario.py 
  │ ├── financialdata.py 
  │ └── savings.py 
  │ ├── tests/ 
  │ ├── test_main.py 
  │ └── test_utils.py 
  │ ├── test/ 
  │ ├── input.json 
  │ └── scenarios.json 
  │ └── README.md

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
