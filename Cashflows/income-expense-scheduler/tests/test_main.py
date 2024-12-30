import unittest
import json
from unittest.mock import patch, mock_open
import sys
import os

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='{"initial_portfolio_value": 100000, "end_analysis_year": 2050, "retirement_year": 2030, "pre_retirement_tax": 0.25, "post_retirement_tax": 0.15, "equity_allocation": 0.6, "fixed_income_allocation": 0.4, "lifestyle_expenses": 30000, "data": [{"years": "2023-2025", "savings": 20000, "withdrawals": 10000, "post_tax": true}]}')
    @patch('json.load')
    @patch('sys.argv', ['main.py', 'input.json', 'scenarios.json'])
    def test_main(self, mock_json_load, mock_open):
        mock_json_load.side_effect = [
            json.loads('{"initial_portfolio_value": 100000, "end_analysis_year": 2050, "retirement_year": 2030, "pre_retirement_tax": 0.25, "post_retirement_tax": 0.15, "equity_allocation": 0.6, "fixed_income_allocation": 0.4, "lifestyle_expenses": 30000, "data": [{"years": "2023-2025", "savings": 20000, "withdrawals": 10000, "post_tax": true}]}'),
            json.loads('[{"scenario_id": 1, "years": [{"year": 2024, "equity_return": 0.1, "fixed_income_return": 0.05}, {"year": 2025, "equity_return": 0.1, "fixed_income_return": 0.05}, {"year": 2026, "equity_return": 0.1, "fixed_income_return": 0.05}]}]')
        ]
        with patch('builtins.print') as mock_print:
            main('input.json', 'scenarios.json')
            mock_print.assert_any_call('Scenario 1 succeeded')
            mock_print.assert_any_call('Total scenarios: 1')
            mock_print.assert_any_call('Succeeded: 1')
            mock_print.assert_any_call('Failed: 0')

if __name__ == '__main__':
    unittest.main()