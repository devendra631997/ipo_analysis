import functools
import sys

def capture_print_to_file(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Backup the original stdout
            original_stdout = sys.stdout

            # Open the file in append mode
            with open(filename, 'w') as file:
                # Redirect stdout to the file
                sys.stdout = file
                try:
                    # Call the original function
                    result = func(*args, **kwargs)
                finally:
                    # Restore the original stdout after function call
                    sys.stdout = original_stdout

            return result
        return wrapper
    return decorator




import pandas as pd

from calc import basic_parameter_calculation
from file_operation import con
from evaluateInvestmentDecision import evaluate_investment, read_data_from_csv

@capture_print_to_file('log.md')
def main():
    con()
    df = pd.read_csv('input_data/company_details.csv')
    results_df = basic_parameter_calculation(df)
    # Save the results to a new Excel file
    results_df.to_excel('output/ipo_analysis_results_data.xlsx', index=False)
    results_df.to_csv('output/ipo_analysis_results_data.csv', index=False)
    # Display the results
    read_data_from_csv('output/ipo_analysis_results_data.csv')

# Run the main function
if __name__ == "__main__":
    main()
