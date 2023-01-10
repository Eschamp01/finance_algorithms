 # <div align="center"> :moneybag: Welcome to the Financial Algorithms Project :moneybag: </div>

### <div align="center"> Project Goals </div>
<!-- #### <div align="center"> Frontend and backend code will be able to: </div> -->

1. To test a given trading algorithm on past stock data, and observe its performance
2. To apply the trading algorithm to real-time stock data, making it an active strategy in a portfolio
</br>

## <div align="center"> Project Scope </div>

### Financial Analysis and Real-time Algorithm Execution

1. **Algorithms Backend** - Backend code to perform desired trading algorithms on stock data, outputting:\
    (a) The time evolution of key metrics\
    (b) The buy and sell time stamps\
    (c) The profit/loss at each sell\
    (d) The overall profit/loss
  
2. **Algorithms Frontend** - A Frontend interface is needed where the user can:\
    (a) View the real-time time-series, or processed series (e.g. returns, normalised/log)\
    (b) Select an algorithm to apply to the data\
    (c) Input/adjust algorithm parameters, and execute the strategy\
    (d) See buy and sell points for the strategy\
    (e) Display metric evolution over time, and profit/loss after sell operations\
    (f) Save algorithm execution results, which are viewable from a history page
    
3. **Real-time Prices Backend** - Backend code to connect to real-time assets, to:\
    (a) Take latest asset (stock/currency) price changes as input\
    (b) Process the price, and output a buy/sell/hold decision for the algorithm\
    (c) Output the key metric values evolution over time\
    (d) Output the profit/loss if sell decision made

### Connecting to a Trading Portfolio

4. **Portfolio Backend** - Backend for connecting to a user's asset portfolio, to:\
    (a) Track the user's current active positions\
    (b) Buy assets, and sell assets if in a position\
    (c) Store trade time and asset price data after a trade is made

5. **Portfolio Frontend** - A Frontend interface for a user's portfolio, to:\
    (a) Allow the user to specify the strategies that they wish to make active\
    (b) Manually enter/exit new positions\
    (c) View historical trade times and prices, saved to a history page
</br>

## <div align="center"> Project Implementation </div>

### Backend Functionality
Core:
- Define classes to calculate metrics for given stock data
- Define functions to execute each algorithm efficiently, outputting 1.(a)-(d) above
- Connect to real-time stock data, inputting the latest price into the active algorithms as soon as it is available

Beneficial:
- Append the lastest price to the database for the stock, updating the chart displayed
- Connect to a user's financial portfolio (need to decide which platform API to use)


### Frontend User Interfaces
Core:
- The **_stock chart analysis_** page: To test algorithms and view all performance outputs
- The __*algorithm history*__ page: To display previous algorithm testing results

Beneficial:
- The **_portfolio_** page: To see all active trades, and execute desired algorithms/trades
- The __*portfolio history*__ page: To show previous trades (and the algorithm they were activated by)
- The __*homepage*__: To display general information and navigate between the functionalities
