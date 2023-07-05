import pandas as pd

def perform_data_analysis():
    try:
        df = read_csv_data()
        clean_data(df)
        analysis_results = perform_analysis(df)
        return analysis_results
    except FileNotFoundError:
        return None

def read_csv_data():
    df = pd.read_csv('stocks.csv', sep=',')
    return df

def clean_data(df):
    numeric_columns = ['COTAÇÃO', 'P/L', 'P/VP', 'DIV.YIELD']
    df[numeric_columns] = df[numeric_columns].astype(float)

def perform_analysis(df):
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
