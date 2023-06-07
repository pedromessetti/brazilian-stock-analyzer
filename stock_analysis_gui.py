import tkinter as tk
from tkinter import ttk

from undervalued_stocks import open_undervalued_stocks_window
from overvalued_stocks import open_overvalued_stocks_window
from chart_functions import display_bar_chart

def open_main_window(analysis_results):
    root = tk.Tk()
    root.title('Stock Analysis')

    # Create a label to display the general analysis
    general_analysis_label = ttk.Label(root, text='General Analysis')
    general_analysis_label.pack(pady=10)

    # Create labels to display the analysis information
    ttk.Label(root, text='Stock Count:').pack()
    ttk.Label(root, text=str(analysis_results['stock_count'])).pack()

    ttk.Label(root, text='Average Price:').pack()
    ttk.Label(root, text='{}%'.format(round(analysis_results['average_price'], 2))).pack()

    ttk.Label(root, text='Max P/E Ratio:').pack()
    ttk.Label(root, text='{} - P/E: {} - P/B: {}'.format(
        analysis_results['max_pe_stock']['Papel'],
        analysis_results['max_pe_stock']['P/L'],
        analysis_results['max_pe_stock']['P/VP']
    )).pack()

    ttk.Label(root, text='Min P/E Ratio:').pack()
    ttk.Label(root, text='{} - P/E: {} - P/B: {}'.format(
        analysis_results['min_pe_stock']['Papel'],
        analysis_results['min_pe_stock']['P/L'],
        analysis_results['min_pe_stock']['P/VP']
    )).pack()

    ttk.Label(root, text='Max P/B Ratio:').pack()
    ttk.Label(root, text='{} - P/E: {} - P/B: {}'.format(
        analysis_results['max_pb_stock']['Papel'],
        analysis_results['max_pb_stock']['P/L'],
        analysis_results['max_pb_stock']['P/VP']
    )).pack()

    ttk.Label(root, text='Min P/B Ratio:').pack()
    ttk.Label(root, text='{} - P/E: {} - P/B: {}'.format(
        analysis_results['min_pb_stock']['Papel'],
        analysis_results['min_pb_stock']['P/L'],
        analysis_results['min_pb_stock']['P/VP']
    )).pack()

    # Create a button to open the undervalued stocks window
    undervalued_button = ttk.Button(root, text='Undervalued Stocks', command=lambda: open_undervalued_stocks_window(root))
    undervalued_button.pack(pady=10)

    # Create a button to open the overvalued stocks window
    overvalued_button = ttk.Button(root, text='Overvalued Stocks', command=lambda: open_overvalued_stocks_window(root))
    overvalued_button.pack(pady=10)

    # Create a chart options combobox
    chart_options = ['Cotação', 'P/L', 'P/VP', 'Div.Yield']
    chart_combobox = ttk.Combobox(root, values=chart_options)
    chart_combobox.pack(pady=10)

    # Create an entry for the number of stocks
    chart_entry = ttk.Entry(root)
    chart_entry.pack(pady=10)

    # Function to handle the "Display Chart" button click
    def display_chart():
        chart_option = chart_options[chart_combobox.current()]
        n = int(chart_entry.get())

        chart_data = analysis_results['df'].sort_values(chart_option, ascending=False)
        display_bar_chart(chart_data, chart_option, n)

    # Create a button to display the chart
    display_chart_button = ttk.Button(root, text='Display Chart', command=display_chart)
    display_chart_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()
