import pandas as pd

def perform_data_analysis():
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv('stocks.csv', sep=',')

        # Clean up the data and convert numeric columns to the appropriate data types
        numeric_columns = ['COTAÇÃO', 'P/L', 'P/VP', 'DIV.YIELD']
        df[numeric_columns] = df[numeric_columns].astype(float)

        # Perform basic data analysis
        analysis_results = {
            'df': df,
            'stock_count': len(df),
            'max_pe_stock': df.loc[df['P/L'].idxmax()],
            'max_pe_ratio': df.loc[df['P/L'].idxmax()]['P/L'],
            'max_pb_stock': df.loc[df['P/VP'].idxmax()],
            'max_pb_ratio': df.loc[df['P/VP'].idxmax()]['P/VP'],
            'min_pe_stock': df.loc[df['P/L'].idxmin()],
            'min_pe_ratio': df.loc[df['P/L'].idxmin()]['P/L'],
            'min_pb_stock': df.loc[df['P/VP'].idxmin()],
            'min_pb_ratio': df.loc[df['P/VP'].idxmin()]['P/VP'],
            'undervalued_stocks': df[df['P/L'] < df['P/L'].median()],
            'overvalued_stocks': df[df['P/VP'] < df['P/VP'].median()]
        }

        return analysis_results
    except FileNotFoundError:
        return None
