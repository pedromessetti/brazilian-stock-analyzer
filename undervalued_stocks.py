import tkinter as tk
from tkinter import ttk
from data_analysis import perform_data_analysis

analysis_results = perform_data_analysis()

def open_undervalued_stocks_window(root):
    def display_undervalued_stocks():
        n = int(undervalued_entry.get())
        undervalued_stocks = analysis_results['undervalued_stocks']['Papel'][:n]

        # Clear previous stock names if any
        for widget in undervalued_window.winfo_children():
            widget.destroy()

        # Display the undervalued stocks in the window
        undervalued_label = ttk.Label(undervalued_window, text='\n'.join(undervalued_stocks))
        undervalued_label.pack(padx=10, pady=10)

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
        command=display_undervalued_stocks
    )
    undervalued_button.pack(pady=10)
