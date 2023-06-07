import subprocess
from stock_analysis_gui import open_main_window
from data_analysis import perform_data_analysis

# Generate the CSV File
subprocess.run(['python3', 'generate_csv.py'])

# Perform data analysis and store the results
analysis_results = perform_data_analysis()

if analysis_results is not None:
    open_main_window(analysis_results)
else:
    print("Exiting program due to missing data file.")
