import tkinter as tk
from tkinter import ttk
from chart_functions import display_bar_chart
from data_analysis import perform_data_analysis

# Perform data analysis and store the results
analysis_results = perform_data_analysis()

# Function to open a new window displaying undervalued stocks
def open_undervalued_stocks_window():
    # Create a new window for undervalued stocks
    undervalued_window = tk.Toplevel(root)
    undervalued_window.title('Undervalued Stocks')

    # Create a label and entry for the number of undervalued stocks to display
    ttk.Label(undervalued_window, text='Number of Stocks:').pack()
    undervalued_entry = ttk.Entry(undervalued_window)
    undervalued_entry.pack()

    # Create a button to display the undervalued stocks
    undervalued_button = ttk.Button(
        undervalued_window, 
        text='Display Undervalued Stocks', 
        command=lambda: display_undervalued_stocks(undervalued_window, int(undervalued_entry.get()))
    )
    undervalued_button.pack(pady=10)

def display_undervalued_stocks(window, n):
    undervalued_stocks = analysis_results['undervalued_stocks']['Papel'][:n]

    # Clear previous stock names if any
    for widget in window.winfo_children():
        widget.destroy()

    # Display the undervalued stocks in the window
    undervalued_label = ttk.Label(window, text='\n'.join(undervalued_stocks))
    undervalued_label.pack(padx=10, pady=10)


# Function to open a new window displaying overvalued stocks
def open_overvalued_stocks_window():
    # Create a new window for overvalued stocks
    overvalued_window = tk.Toplevel(root)
    overvalued_window.title('Overvalued Stocks')

    # Create a label and entry for the number of overvalued stocks to display
    ttk.Label(overvalued_window, text='Number of Stocks:').pack()
    overvalued_entry = ttk.Entry(overvalued_window)
    overvalued_entry.pack()

    # Create a button to display the overvalued stocks
    overvalued_button = ttk.Button(
        overvalued_window, 
        text='Display Overvalued Stocks', 
        command=lambda: display_overvalued_stocks(overvalued_window, int(overvalued_entry.get()))
    )
    overvalued_button.pack(pady=10)

def display_overvalued_stocks(window, n):
    overvalued_stocks = analysis_results['overvalued_stocks']['Papel'][:n]

    # Clear previous stock names if any
    for widget in window.winfo_children():
        widget.destroy()

    # Display the overvalued stocks in the window
    overvalued_label = ttk.Label(window, text='\n'.join(overvalued_stocks))
    overvalued_label.pack(padx=10, pady=10)


# Create the main window
root = tk.Tk()
root.title('Stock Analysis')


# Start the main event loop
root.mainloop()
