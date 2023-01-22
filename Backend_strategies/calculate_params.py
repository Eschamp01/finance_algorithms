import pdb
import yfinance as yf
import sys
sys.path.append(".")
import data_classes
import algorithms
# from . import data_classes
# from . import algorithms

def get_data(data, model):
    """
    Returns any raw financial data needed from: Date, Open, High, Low, Close and Volume.
    Returns the label for the axis data.
    """
    if model == "Moving Average":
        x_label = "Date"
        x_vals = data.index
        y_label = "Closing price ($)"
        y_vals = data['Close']
    # If data processing different for other models, process differently
    return x_label, x_vals, y_label, y_vals


def get_graph_params(ticker, interval, start, end, model, params):
    "Returns all required graph parameters. Backend algorithm execution master function."
    data = yf.download(ticker, interval=interval, start=start, end=end)
    x_label, x_vals, y_label, y_vals = get_data(data, model)

    # Execute algorithm here. Moving average only needy y_vals and params
    if model == "Moving Average":
        metrics = algorithms.moving_average(x_vals, y_vals, params)
    elif model == "other model":
        return 1
    
    graph_params = data_classes.GraphParams(ticker=ticker, scale="linear", hidden_elements=[], metrics=metrics, \
                               x_vals=x_vals, x_label=x_label, y_vals=y_vals, y_label=y_label)

    return graph_params

model_params = {'low_ma':20, 'high_ma':40} # Will get this from user input. Dummy for now.

# To execute the backend code for am algorithm, only the below function needs to be called.
graph_params = get_graph_params(ticker="AAPL", 
                                interval="1h", 
                                start="2022-01-01", 
                                end="2023-01-01",
                                model="Moving Average", 
                                params=model_params)

# graph_params is then used in frontend code to view strategy performance results.

pdb.set_trace()