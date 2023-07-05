import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def display_bar_chart(data, option, n):
    top_stocks = data.head(n)
    
    plt.bar(top_stocks['Papel'], top_stocks[option])
    plt.xlabel('Stock')
    plt.ylabel(option)
    plt.title(f'Top {n} Stocks by {option}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
