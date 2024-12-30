from financialdata import FinancialData
from datetime import datetime

def apply_scenario(financial_data_dict, scenario_data, input_data):
    initial_portfolio_value = input_data['initial_portfolio_value']
    equity_allocation = input_data['equity_allocation']
    fixed_income_allocation = input_data['fixed_income_allocation']
    pre_retirement_tax = input_data['pre_retirement_tax']
    post_retirement_tax = input_data['post_retirement_tax']
    retirement_year = input_data['retirement_year']
    lifestyle_expenses = input_data['lifestyle_expenses']
    end_analysis_year = input_data['end_analysis_year']

    previous_year_portfolio_value = initial_portfolio_value
    scenario_failed = False

    for year in range(datetime.now().year, end_analysis_year + 1):
        if year not in financial_data_dict:
            tax_rate = pre_retirement_tax if year < retirement_year else post_retirement_tax
            retired = year >= retirement_year
            financial_data_dict[year] = FinancialData(year, 0, 0, 0, retired, tax_rate, initial_portfolio_value, 0, 0, 0)
            if retired:
                financial_data_dict[year].withdrawals += lifestyle_expenses

        fd = financial_data_dict[year]
        fd.portfolio_value = previous_year_portfolio_value + fd.savings - fd.withdrawals

        if fd.portfolio_value < 0:
            fd.scenario_failed = True
            scenario_failed = True
            break

        if year in scenario_data:
            equity_return = scenario_data[year]['equity_return']
            fixed_income_return = scenario_data[year]['fixed_income_return']
        else:
            equity_return = 0
            fixed_income_return = 0

        fd.equity_value = fd.portfolio_value * equity_allocation * (1 + equity_return)
        fd.fixed_income_value = fd.portfolio_value * fixed_income_allocation * (1 + fixed_income_return)

        fd.portfolio_value = fd.equity_value + fd.fixed_income_value
        fd.portfolio_return = (fd.portfolio_value - previous_year_portfolio_value) / previous_year_portfolio_value

        previous_year_portfolio_value = fd.portfolio_value

    return financial_data_dict, scenario_failed