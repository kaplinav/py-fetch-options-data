import pandas as pd
import yfinance as yf
from datetime import datetime

# it returns the top 10 financial sector tickers in the S&P 500 index
# top 10 at 05.08.2024
def get_top10_sp500_fin_tickers():
  return ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'GS', 'SPGI', 'AXP', 'MS']


"""
Fetches options data for a given ticker with expiration dates from now using yfinance.

Parameters:
ticker (str): The stock ticker symbol for which to fetch options data.

Returns:
pd.DataFrame: A pandas DataFrame containing the options data for the specified ticker.
    
The DataFrame includes columns such as:
    - Contract Name
    - Strike
    - Last Price
    - Bid
    - Ask
    - Change
    - % Change
    - Volume
    - Open Interest
    - Implied Volatility
    
Example:
>>> options_data = fetch_options_data("AAPL")
>>> print(options_data.head())
"""
def fetch_options_data(ticker: str) -> pd.DataFrame:
  # Initialize the yfinance Ticker object
  stock = yf.Ticker(ticker)    
    
  # Get the expiration dates for the options
  expiration_dates = stock.options    
    
  # Initialize an empty DataFrame to store all options data
  all_options_data = pd.DataFrame()
      
  # Loop through each expiration date and fetch the options data
  for date in expiration_dates:
    # Get the options data for the specific expiration date
    options = stock.option_chain(date)
        
    # Concatenate calls and puts data
    calls = options.calls
    calls['type'] = 'C'
    puts = options.puts
    puts['type'] = 'P'
    options_data = pd.concat([calls, puts])    

    # Add the expiration date to the options data
    options_data['expirationDate'] = date
        
    # Append the data to the all_options_data DataFrame
    all_options_data = pd.concat([all_options_data, options_data])
    
  # Reset the index of the final DataFrame
  all_options_data.reset_index(drop=True, inplace=True)

  return all_options_data


"""
Main method to fetch options data for each ticker in a list and store the data in a CSV file.

The method:
- Defines a list of tickers.
- Calls the fetch_options_data method for each ticker.
- Aggregates the data into a single DataFrame.
- Stores the aggregated data into a CSV file.
"""
def main():
  # List of top 10 S&P 500 financial sector tickers
  #tickers = ['JPM', 'BAC', 'WFC', 'C', 'GS', 'MS', 'USB', 'PNC', 'TFC', 'BK']
   tickers = get_top10_sp500_fin_tickers()

  # Initialize an empty DataFrame to store all options data
  all_tickers_options_data = pd.DataFrame()

  # items count for each ticker
  ticker_cnt = {}

  # Loop through each ticker
  for ticker in tickers:
    print(f"Fetching options data for {ticker}...")

    # Call the fetch_options_data(ticker) method and get the options data for the current ticker
    options_data = fetch_options_data(ticker)

    # Add the number of items for the current ticker
    ticker_cnt[ticker] = options_data.shape[0]    

    # Add the ticker symbol to the options data
    options_data['Ticker'] = ticker

    # Append the data to the all_tickers_options_data DataFrame
    all_tickers_options_data = pd.concat([all_tickers_options_data, options_data])
  
  # Reset the index of the final DataFrame
  all_tickers_options_data.reset_index(drop=True, inplace=True)

  current_dateTime = datetime.now()
  file_name = f'options_data_{current_dateTime.strftime("%d%m%Y_%H%M%S")}.csv'
    
  # Show the result 
  print('Result')
  print('Ticker      Items count')
  for t in ticker_cnt:
    print(f'{t}      {ticker_cnt[t]}')
  print()    

  # Store the aggregated data into a CSV file
  all_tickers_options_data.to_csv(file_name, index=False)
  print(f"Options data has been successfully saved to {file_name}")


# Ensure the script runs only if executed directly
if __name__ == "__main__":
  main()
  
