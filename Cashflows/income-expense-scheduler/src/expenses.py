class Expenses:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, year, amount):
        if year in self.expenses:
            self.expenses[year] += amount
        else:
            self.expenses[year] = amount

    def get_total_expenses(self):
        return sum(self.expenses.values())

    def get_expenses_by_year(self):
        return self.expenses