
class FetchOptionResult():
    '''
    This class stores and displays the result of fetching  options data 
    '''
  
    def __init__(self):
        self.__result = [['Ticker', 'Count']]


    def add(self, ticker, count):
        '''
        This method adds the number of option contracts for a given ticker 
        '''
        self.__result.append([ticker, count])


    def show(self):
        '''
        This method shows the number of option contracts for each ticker
        Example:
        | Ticker | Count  |
        | AAPL   | 55     |
        | JPM    | 1249   |
        '''
        
        # max length of cell
        maxLen = 1

        for row in self.__result:
            for col in row:
                if len(str(col)) > maxLen:
                    maxLen = len(str(col))   

        # number of columns in output
        columns = 2
        row_format = f'| {{:<{maxLen}}} ' * columns
        row_format = row_format + '|'

        for row in self.__result:
            print(row_format.format(*row))
