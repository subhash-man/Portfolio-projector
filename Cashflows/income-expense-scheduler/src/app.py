from flask import Flask, render_template, request, redirect, url_for
import json
import os
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_data = {
        "initial_portfolio_value": float(request.form['initial_portfolio_value']),
        "retirement_year": int(request.form['retirement_year']),
        "pre_retirement_tax": float(request.form['pre_retirement_tax']),
        "post_retirement_tax": float(request.form['post_retirement_tax']),
        "equity_allocation": float(request.form['equity_allocation']),
        "fixed_income_allocation": float(request.form['fixed_income_allocation']),
        "lifestyle_expenses": float(request.form['lifestyle_expenses']),
        "end_analysis_year": int(request.form['end_analysis_year']),
        "data": json.loads(request.form['data'])
    }

    with open('temp\input.json', 'w') as f:
        json.dump(input_data, f, indent=4)

    return main(input_file='temp\input.json', scenarios_file='src\scenarios.json')  # Call the main function

if __name__ == '__main__':
    app.run(debug=True)