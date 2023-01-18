import pdb
import yfinance as yf
from data_classes import DataParams, ModelParams, GraphParams

def get_data(data, model):
    """
    Returns any raw financial data needed from: Date, Open, High, Low, Close and Volume.
    Returns the label for the axis data.
    """
    if model == "moving_average":
        x_label = "Date"
        x_vals = data.index.tolist()
        y_label = "Closing price ($)"
        y_vals = data['Close'].tolist()
    # If data processing different for other models, process differently
    return x_label, x_vals, y_label, y_vals


def moving_average(y_vals, params):
    """Execute moving average strategy for given params. Return all desired internally calculated metrics."""
    low_ma = y_vals.rolling(window=params['low_ma']).mean()
    high_ma = y_vals.rolling(window=params['high_ma']).mean()
    # CODE HERE
    # Whenever the lower moving average crosses the higher moving average:
    # If you haven't bought yet (not in a position):
    #   If lower went from low to high, buy.
    # If you're in a position:
    #   If lower went from high to low, sell. 
    # Return metrics (lower_ma, higher_ma), buy dates, sell dates, and profit. Dummy variables assigned below:

    buy_dates = ["2022-01-15", "2022-02-15", "2022-03-15", "2022-04-15", "2022-05-15"]
    sell_dates = ["2022-01-25", "2022-02-25", "2022-03-25", "2022-04-25", "2022-05-25"]
    profit = [-10.0, 5.0, -3.0, 6.0, 4.0] # same length as sell_indices, since whebever you sell you have profit/loss

    metrics = {'low_ma': low_ma, 'high_ma': high_ma, 'buy_dates': buy_dates, \
               'sell_dates':sell_dates, 'profit':profit}
    return metrics


def get_graph_params(ticker, interval, start, end, model, params):
    data = yf.download(ticker=ticker, interval=interval, start=start, end=end)
    x_label, x_vals, y_label, y_vals = get_data(data, model)

    # Execute algorithm here. Moving average only needy y_vals and params
    metrics = moving_average(y_vals, params)
    
    graph_params = GraphParams(ticker=ticker, scale="linear", hidden_elements=[], metrics=metrics, \
                               x_vals=x_vals, x_label=x_label, y_vals=y_vals, y_label=y_label)

    return graph_params

model_params = {'low_ma':20, 'high_ma':40} # Will get this from user input. Dummy for now.

# To execute the backend code for am algorithm, only the below function needs to be called.
graph_params = get_graph_params(ticker="AAPL", 
                                interval="1h", 
                                start="2022-01-01", 
                                end="2023-01-01",
                                model="moving_average", 
                                params=model_params)

# graph_params is then used in frontend code to view strategy performance results.

pdb.set_trace()