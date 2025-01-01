import json
from datetime import datetime
from savings import Savings
from financialdata import FinancialData

# Function to translate internal data structure to JSON
def internal_to_json(financial_data_list):
    return json.dumps([fd.to_dict() for fd in financial_data_list], indent=4)

# Function to translate input data structure to internal data structure
def input_to_internal(input_data, scenario_data):
    current_year = datetime.now().year
    end_analysis_year = input_data['end_analysis_year']
    financial_data_dict = {}

    initial_portfolio_value = input_data['initial_portfolio_value']
    retirement_year = input_data['retirement_year']
    pre_retirement_tax = input_data['pre_retirement_tax']
    post_retirement_tax = input_data['post_retirement_tax']
    lifestyle_expenses = input_data['lifestyle_expenses']
    data = input_data['data']

    # Validate allocations
    equity_allocation = input_data.get('equity_allocation', 0)
    fixed_income_allocation = input_data.get('fixed_income_allocation', 0)
    total_allocation = equity_allocation + fixed_income_allocation
    if total_allocation != 1:
        raise ValueError("Total allocation of equity and fixed income must be 100%")

    for item in data:
        years = item['years']
        if '-' in years:
            # Handle range of years
            start_year, end_year = map(int, years.split('-'))
            for year in range(start_year, end_year + 1):
                if current_year <= year <= end_analysis_year:
                    tax_rate = pre_retirement_tax if year < retirement_year else post_retirement_tax
                    retired = year >= retirement_year
                    # Zero out savings if retired
                    savings = 0 if retired else item['savings']
                    savings, tax_paid = Savings.calculate_post_tax_savings(savings, item.get('post_tax', True), tax_rate, return_tax=True)
                    if year not in financial_data_dict:
                        financial_data_dict[year] = FinancialData(year, 0, 0, 0, retired, tax_rate, initial_portfolio_value, 0, 0, 0)
                    fd = financial_data_dict[year]
                    fd.savings += savings
                    fd.withdrawals += item['withdrawals']
                    fd.tax_paid += tax_paid
                    # Add lifestyle expenses to withdrawals only once per year
                    if retired and not fd.lifestyle_expenses_added:
                        fd.withdrawals += lifestyle_expenses
                        fd.lifestyle_expenses_added = True
        else:
            # Handle single year
            year = int(years)
            if current_year <= year <= end_analysis_year:
                tax_rate = pre_retirement_tax if year < retirement_year else post_retirement_tax
                retired = year >= retirement_year
                # Zero out savings if retired
                savings = 0 if retired else item['savings']
                savings, tax_paid = Savings.calculate_post_tax_savings(savings, item.get('post_tax', True), tax_rate, return_tax=True)
                if year not in financial_data_dict:
                    financial_data_dict[year] = FinancialData(year, 0, 0, 0, retired, tax_rate, initial_portfolio_value, 0, 0, 0)
                fd = financial_data_dict[year]
                fd.savings += savings
                fd.withdrawals += item['withdrawals']
                fd.tax_paid += tax_paid
                # Add lifestyle expenses to withdrawals only once per year
                if retired and not fd.lifestyle_expenses_added:
                    fd.withdrawals += lifestyle_expenses
                    fd.lifestyle_expenses_added = True

    return financial_data_dict
