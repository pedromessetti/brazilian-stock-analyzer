import subprocess

# Generate the CSV File
subprocess.run(['python3', 'generate_csv.py'])

from data_analysis import perform_data_analysis
from stock_analysis_gui import open_main_window

# Perform data analysis and store the results
analysis_results = perform_data_analysis()

# Open the main window with the analysis results
open_main_window(analysis_results)
