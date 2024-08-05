# S&P 500 Financial Sector Options Data Fetcher

## Overview

This Python program fetches options data for the top 10 S&P 500 financial sector tickers using the `yfinance` library. The options data is retrieved with the expiration date starting from the current date and is stored in a CSV file on disk.

## Features

- Fetches top 10 S&P 500 financial sector tickers.
- Retrieves options data for each ticker with expiration dates from now.
- Stores the retrieved data in a CSV file.

## Requirements

- Python 3.x
- `yfinance` library
- `pandas` library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. **Install the required Python libraries:**

   ```sh
   pip install yfinance pandas
   ```

## Usage

1. **Run the program:**

   ```sh
   python fetch_options_data.py
   ```

2. **The program will:**
   - Retrieve the top 10 S&P 500 financial sector tickers.
   - Fetch the options data for each ticker with expiration dates from the current date.
   - Store the data in a CSV file named `options_data.csv`.

## Files

- `fetch_options_data.py`: The main script to fetch and store options data.
- `options_data.csv`: The output file containing the fetched options data.

## Example

After running the script, you will find a file named `options_data.csv` in your working directory. This file will contain the options data for the top 10 S&P 500 financial sector tickers.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [yfinance](https://github.com/ranaroussi/yfinance) for providing the data fetching capabilities.
- [pandas](https://pandas.pydata.org/) for data manipulation and CSV handling.
