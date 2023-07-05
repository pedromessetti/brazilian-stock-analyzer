import tkinter as tk
from tkinter import ttk
from data_analysis import perform_data_analysis

analysis_results = perform_data_analysis()

def open_overvalued_stocks_window(root):
    def display_overvalued_stocks():
        n = int(overvalued_entry.get())
        overvalued_stocks = analysis_results['overvalued_stocks']['Papel'][:n]

        # Clear previous stock names if any
        for widget in overvalued_window.winfo_children():
            widget.destroy()

        # Display the overvalued stocks in the window
        overvalued_label = ttk.Label(overvalued_window, text='\n'.join(overvalued_stocks))
        overvalued_label.pack(padx=10, pady=10)

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
        command=display_overvalued_stocks
    )
    overvalued_button.pack(pady=10)
