The current scope for this project is to create the frontend and backend code to be able to:
1. Test a given trading algorithm on past stock data, and observe its performance
2. Apply the trading algorithm to real-time stock data, making it an active strategy in a portfolio

In order to do this, the following steps need to be taken:

1. Backend code for the trading algorithms needs to be implemented.
2. A Frontend interface is needed where the user can:
    (a) Input/adjust algorithm parameters.
    (b) See buy and sell points for the strategy.
    (c) See the profitability of the strategy along different time steps, and the final profit/loss.
    (d) View past algorithm execution results, which are saved to a history page.
3. Backend for connecting to real-time asset (stock/currency) price changes, and processing them.
4. Backend for connecting to a user's portfolio to track and change the user's current buy and sell positions in different assets.
5. Frontend to allow the user to specify the strategies that they wish to execute in their profile, and any positions they wish to enter/exit.

In total, two main frontend user interfaces are needed, with a homepage to display general information and navigate between the functionalities. 
Backend code is needed to:
- Connect to a user's financial portfolio
- Fetch and process real-time asset information
- Execute trading algorithms


<!-- Trading Analysis
Python code for different strategies
- for each strategy, when to buy and sell
March 2021 to dec 2021, momentum trading with alpha = 0.5, beta = 1.2

Webpage to display stocks visually
- show buy and sell points, and money made

Trading Implementation
Python code for getting real time stock data, and executing trades according to the strategies
Condition = Buy when 30 day moving average > 50 day moving average.
Check if you already bought, don’t buy again etc….. complex 
Real-time stock data comes… condition = false, false, true -> execute trade


Webpage to display trades made
 -->
