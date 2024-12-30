class FinancialData:
    __slots__ = ['year', 'savings', 'withdrawals', 'tax_paid', 'retired', 'tax_rate', 'portfolio_value', 'portfolio_return', 'equity_value', 'fixed_income_value', 'scenario_failed', 'lifestyle_expenses_added']

    def __init__(self, year, savings, withdrawals, tax_paid, retired, tax_rate, portfolio_value, portfolio_return, equity_value, fixed_income_value, scenario_failed=False):
        self.year = year
        self.savings = savings
        self.withdrawals = withdrawals
        self.tax_paid = tax_paid
        self.retired = retired
        self.tax_rate = tax_rate
        self.portfolio_value = portfolio_value
        self.portfolio_return = portfolio_return
        self.equity_value = equity_value
        self.fixed_income_value = fixed_income_value
        self.scenario_failed = scenario_failed
        self.lifestyle_expenses_added = False

    def to_dict(self):
        return {
            "year": self.year,
            "savings": self.savings,
            "withdrawals": self.withdrawals,
            "tax_paid": self.tax_paid,
            "retired": self.retired,
            "tax_rate": self.tax_rate,
            "portfolio_value": self.portfolio_value,
            "portfolio_return": self.portfolio_return,
            "equity_value": self.equity_value,
            "fixed_income_value": self.fixed_income_value,
            "scenario_failed": self.scenario_failed,
            "lifestyle_expenses_added": self.lifestyle_expenses_added
        }