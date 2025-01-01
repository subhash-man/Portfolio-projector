import unittest
import sys
import os

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import input_to_internal, internal_to_json
from financialdata import FinancialData

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.input_data = {
            "initial_portfolio_value": 100000,
            "end_analysis_year": 2050,
            "retirement_year": 2030,
            "pre_retirement_tax": 0.25,
            "post_retirement_tax": 0.15,
            "equity_allocation": 0.6,
            "fixed_income_allocation": 0.4,
            "lifestyle_expenses": 30000,
            "data": [{"years": "2023-2025", "savings": 20000, "withdrawals": 10000, "post_tax": True}]
        }
        self.scenario_data = {
            "years": [
                {"year": 2023, "equity_return": 0.1, "fixed_income_return": 0.05},
                {"year": 2024, "equity_return": 0.1, "fixed_income_return": 0.05},
                {"year": 2025, "equity_return": 0.1, "fixed_income_return": 0.05}
            ]
        }

    def test_input_to_internal(self):
        financial_data_dict = input_to_internal(self.input_data, self.scenario_data)
        self.assertEqual(len(financial_data_dict), 1)
        self.assertIsInstance(financial_data_dict[2025], FinancialData)
        self.assertEqual(financial_data_dict[2025].savings, 20000)
        self.assertEqual(financial_data_dict[2025].withdrawals, 10000)

    def test_internal_to_json(self):
        financial_data_dict = input_to_internal(self.input_data, self.scenario_data)
        financial_data_list = list(financial_data_dict.values())
        json_output = internal_to_json(financial_data_list)
        self.assertIn('"year": 2025', json_output)
        self.assertIn('"savings": 20000', json_output)
        self.assertIn('"withdrawals": 10000', json_output)

if __name__ == '__main__':
    unittest.main()