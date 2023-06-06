import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv('tabela.csv', sep=',')

# Clean up the data and convert numeric columns to the appropriate data types
numeric_columns = ['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro', 'P/EBIT',
                   'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit', 'Mrg. Líq.', 'Liq. Corr.',
                   'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq', 'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']
df[numeric_columns] = df[numeric_columns].astype(float)



# Perform basic data analysis
print('Data Analysis:')
print('-------------')
print('Number of stocks:', len(df))
print('Average stock price:', df['Cotação'].mean())
print('Maximum P/L ratio:', df['P/L'].max())
print('Minimum P/VP ratio:', df['P/VP'].min())

# Generate a bar chart of stock prices
df = df.sort_values('Cotação', ascending=False)
top_10_stocks = df.head(10)
plt.bar(top_10_stocks['Papel'], top_10_stocks['Cotação'])
plt.xlabel('Stock')
plt.ylabel('Price')
plt.title('Top 10 Stocks by Price')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
