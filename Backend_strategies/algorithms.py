# Define all algorithm code here. If it gets too long, could separate by strategy.

def moving_average(x_vals, y_vals, params):
    """Execute moving average strategy for given params. Return all desired internally calculated metrics."""
    low_ma = y_vals.rolling(window=params['low_ma']).mean()
    high_ma = y_vals.rolling(window=params['high_ma']).mean()
    # buy_dates = []
    # in_position = False
    # for date in x_vals:
    #     if not(in_position):
    #         if low_ma > high_ma:
    #             buy_dates.append(date)
    #             in_position = True
    #     else:
    #         if high_ma > low_ma:
    #             sell_dates.append(date)
    #             in_position = False

    #     if len(buy_dates) > len(sell_dates):
    #         sell_dates.pop

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


def new_algorithm(inputs):
    #logic
    return inputs