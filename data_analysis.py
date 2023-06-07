import pandas as pd

def perform_data_analysis():
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv('tabela.csv', sep=',')
    except FileNotFoundError:
        return None

    # Clean up the data and convert numeric columns to the appropriate data types
    numeric_columns = ['Cotação', 'P/L', 'P/VP', 'Div.Yield']
    df[numeric_columns] = df[numeric_columns].astype(float)

    # Perform basic data analysis
    stock_count = len(df)
    max_pe_stock = df.loc[df['P/L'].idxmax()]
    max_pe_ratio = max_pe_stock['P/L']
    max_pb_stock = df.loc[df['P/VP'].idxmax()]
    max_pb_ratio = max_pb_stock['P/VP']
    min_pe_stock = df.loc[df['P/L'].idxmin()]
    min_pe_ratio = min_pe_stock['P/L']
    min_pb_stock = df.loc[df['P/VP'].idxmin()]
    min_pb_ratio = min_pb_stock['P/VP']

    # Additional analysis
    undervalued_stocks = df[df['P/L'] < df['P/L'].median()]
    overvalued_stocks = df[df['P/VP'] > df['P/VP'].median()]

    analysis_results = {
        'df': df,
        'stock_count': stock_count,
        'max_pe_stock': max_pe_stock,
        'max_pe_ratio': max_pe_ratio,
        'max_pb_stock': max_pb_stock,
        'max_pb_ratio': max_pb_ratio,
        'min_pe_stock': min_pe_stock,
        'min_pe_ratio': min_pe_ratio,
        'min_pb_stock': min_pb_stock,
        'min_pb_ratio': min_pb_ratio,
        'undervalued_stocks': undervalued_stocks,
        'overvalued_stocks': overvalued_stocks
    }

    return analysis_results
