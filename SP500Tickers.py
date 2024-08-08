class SP500Tickers:
    """
    A class to represent the S&P 500 tickers
    """

    def getTop10Tickers():
        """
        Returns a list of the top 10 S&P 500 financial sector tickers.

        The list is hardcoded based on the current leading companies in the financial sector (top 10 at 05.08.2024).

        Returns:
        list: A list of ticker symbols representing the top 10 financial sector companies.
        
        Example:
        >>> tickers = SP500Tickers.getTop10Tickers()
        >>> print(tickers)
        ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'GS', 'SPGI', 'AXP', 'MS']
        """
        
        # List of top 10 financial sector tickers in the S&P 500
        top10Tickers = ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'GS', 'SPGI', 'AXP', 'MS']
        
        return top10Tickers
