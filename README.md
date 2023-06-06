<h1 align="center">
Brazillian Stock Analyzer
</h1>

## Index
- [Index](#index)
- [Description :clipboard:](#description-clipboard)
- [Features](#features)
- [Requirements :gear:](#requirements-gear)
- [Usage](#usage)
- [Operation :wrench:](#operation-wrench)
- [Author](#author)

## Description :clipboard:

The Brazilian Stock Analyzer is a Python program that fetches data from the "https://fundamentus.com.br" website, extracts stock information, and performs basic data analysis on the retrieved data. It generates a CSV file containing the stock data and visualizes the data through a bar chart.

## Features

- Fetches stock data from "https://fundamentus.com.br/resultado.php"
- Cleans up the data and converts numeric columns to the appropriate data types
- Performs basic data analysis, including the number of stocks, average stock price, maximum P/L ratio, and minimum P/VP ratio
- Generates a bar chart of the top 10 stocks by price (customizable)

## Requirements :gear:

- Python 3.x
- Beautiful Soup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Pandas (`pip install pandas`)
- Matplotlib (`pip install matplotlib`)

## Usage

1. Clone the repository and navigate to the project folder.
2. Run `make` in the terminal to execute the program.
1. The terminal will display basic analysis results.
2. A new window will open with a bar chart showing the top 10 stocks sorted by price.

## Operation :wrench:

The program first runs `analyzer.py`, which fetches stock data from "https://fundamentus.com.br/resultado.php", cleans up the data, and saves it to a CSV file named `tabela.csv`. Then, `analyzer.py` is executed, which reads the generated CSV file, performs basic data analysis, and prints the results to the console. It also sorts the stocks by price, generates a bar chart using the Matplotlib library, and displays it on the screen.

Note: To change the number of top stocks displayed in the bar chart, modify the `head()` method in `analyzer.py`.

## Author
| [<img src="https://avatars.githubusercontent.com/u/105685220?v=4" width="115"><br><sub>Pedro Vinicius Messetti</sub>](https://github.com/pedromessetti) |
| :---: |
