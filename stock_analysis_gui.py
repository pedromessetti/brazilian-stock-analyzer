import tkinter as tk
from tkinter import ttk
from undervalued_stocks import open_undervalued_stocks_window
from overvalued_stocks import open_overvalued_stocks_window
from chart_functions import display_bar_chart

def open_main_window(analysis_results):
    '''Function to generate the main window'''
    root = tk.Tk()
    root.title('Stock Analysis')

    # Display the analysis information
    ttk.Label(root, text='{} stocks analyzed\n'.format(str(analysis_results['stock_count']))).pack(pady=10)

    ttk.Label(root, text='Max P/L').pack()
    ttk.Label(root, text='{} = {}'.format(
        analysis_results['max_pe_stock']['Papel'],
        analysis_results['max_pe_stock']['P/L']
    )).pack()

    ttk.Label(root, text='Min P/L').pack()
    ttk.Label(root, text='{} = {}\n\n'.format(
        analysis_results['min_pe_stock']['Papel'],
        analysis_results['min_pe_stock']['P/L']
    )).pack()

    ttk.Label(root, text='Max P/VP').pack()
    ttk.Label(root, text='{} = {}'.format(
        analysis_results['max_pb_stock']['Papel'],
        analysis_results['max_pb_stock']['P/VP']
    )).pack()

    ttk.Label(root, text='Min P/VP').pack()
    ttk.Label(root, text='{} = {}\n'.format(
        analysis_results['min_pb_stock']['Papel'],
        analysis_results['min_pb_stock']['P/VP']
    )).pack()

    # Button to open the undervalued stocks window
    undervalued_button = ttk.Button(root, text='Undervalued Stocks', command=lambda: open_undervalued_stocks_window(root))
    undervalued_button.pack(pady=10)

    # Button to open the overvalued stocks window
    overvalued_button = ttk.Button(root, text='Overvalued Stocks', command=lambda: open_overvalued_stocks_window(root))
    overvalued_button.pack(pady=10)


    # Chart options combobox
    ttk.Label(root, text='Chart Option:').pack()
    chart_options = ['Cotação', 'P/L', 'P/VP', 'Div.Yield']
    chart_combobox = ttk.Combobox(root, values=chart_options)
    chart_combobox.pack(pady=5)

    # Input for the number of stocks
    ttk.Label(root, text='Number of Stocks:').pack()
    chart_entry = ttk.Entry(root)
    chart_entry.pack(pady=5)

    def display_chart():
        '''Function to handle the "Display Chart" button click'''
        chart_option = chart_options[chart_combobox.current()]
        n = int(chart_entry.get())

        chart_data = analysis_results['df'].sort_values(chart_option, ascending=False)
        display_bar_chart(chart_data, chart_option, n)

    # Button to display the chart
    display_chart_button = ttk.Button(root, text='Display Chart', command=display_chart)
    display_chart_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()
