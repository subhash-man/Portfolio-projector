import json
import sys
import copy
from utils import input_to_internal, internal_to_json
from scenario import apply_scenario
from financialdata import FinancialData

def main(input_file, scenarios_file):
    # Read input from the specified input file
    with open(input_file, 'r') as file:
        input_data = json.load(file)

    # Read scenarios data from the specified scenarios file
    with open(scenarios_file, 'r') as file:
        scenarios_data = json.load(file)

    # Translate input data to internal data structure
    financial_data_dict = input_to_internal(input_data, scenarios_data[0])

    # Initialize counters for succeeded and failed scenarios
    succeeded_count = 0
    failed_count = 0

    # Apply each scenario and print the result
    for scenario in scenarios_data:
        scenario_id = scenario['scenario_id']
        scenario_years = {item['year']: item for item in scenario['years']}
        financial_data_dict_copy = copy.deepcopy(financial_data_dict)
        financial_data_dict_copy, scenario_failed, failed_year = apply_scenario(financial_data_dict_copy, scenario_years, input_data)
        if scenario_failed:
            status = f"failed in year {failed_year}"
            failed_count += 1
        else:
            status = "succeeded"
            succeeded_count += 1
        print(f"Scenario {scenario_id} {status}")

    # Print the summary of succeeded vs failed scenarios
    print(f"Total scenarios: {len(scenarios_data)}")
    print(f"Succeeded: {succeeded_count}")
    print(f"Failed: {failed_count}")

    # Print the output JSON for the last scenario
    # output_json = internal_to_json(list(financial_data_dict_copy.values()))
    # print(output_json)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])