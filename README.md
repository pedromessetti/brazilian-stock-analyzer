<h1 align="center">
    Brazilian Stock Analyzer
</h1>

<p>

This project is a stock analysis software developed in Python that allows users to analyze stock market data, identify undervalued and overvalued stocks, and visualize data through charts. The software utilizes web scraping to fetch stock data from the "https://fundamentus.com.br" website, performs data analysis using Pandas, and provides a user-friendly GUI using Tkinter.

</p>

## Index
- [Index](#index)
- [Feauteres](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)


## Features

- Generate CSV file: The program scrapes stock data from the provided website and generates a CSV file ("stocks.csv") containing the fetched data.

- Data Analysis: The program performs basic data analysis on the stock data, including calculating various ratios and identifying undervalued and overvalued stocks based on specific criteria.

- GUI Interface: The software provides a graphical user interface using Tkinter, allowing users to view analysis results, display lists of undervalued and overvalued stocks, and visualize data through interactive charts.

## Usage

To use, follow these steps:

1. Clone the repository:

        git clone https://github.com/pedromessetti/brazilian-stock-analyzer.git

3. Install the required dependencies by running the following command:

        pip3 install pandas beautifulsoup4 requests matplotlib

2. `cd` to the project directory

4. Run the following command-line to generate the CSV file, perform data analysis, and open the main GUI window.

        python3 main.py

In the window, you can view the analysis results, including the total number of analyzed stocks, maximum and minimum P/L and P/VP ratios, and more.

- Click on the "Undervalued Stocks" or "Overvalued Stocks" button to open a new window displaying the respective list of stocks.

- Select a chart option from the dropdown menu and enter the desired number of stocks in the corresponding input field.

- Click the "Display Chart" button to generate and display a bar chart of the top N stocks based on the selected option.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author
| [<img src="https://avatars.githubusercontent.com/u/105685220?v=4" width=115><br><sub>Pedro Vinicius Messetti</sub>](https://github.com/pedromessetti) |
|:---------------------------------------------------------------------------------------------------------------------------------------------------: |
