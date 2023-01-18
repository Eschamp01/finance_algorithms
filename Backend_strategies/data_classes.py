class GraphParams:
    """Stores all parameters needed to graph a model, including the metrics and buy/sell decisions"""
    def __init__(self, ticker, scale, hidden_elements, metrics, x_vals, x_label, y_vals, y_label) -> None:
        self.ticker = ticker
        self.scale = scale
        self.hidden_elements = hidden_elements #y_axis, any metric, buy/sell points, profit/loss
        self.x_vals = x_vals
        self.x_label = x_label
        self.y_vals = y_vals
        self.y_label = y_label
        self.metrics = {}
        for name, lst in metrics.items():
                self.metrics[name] = lst # else list length not matching error

        def insert_metric(self, metric_name:str, metric_list:list, len_check=True):
            if len_check: # check list length = date length
                if len(metric_list) == len(self.x_vals):
                    self.metrics[metric_name] = metric_list
            else: # don't ensure length
                self.metrics[metric_name] = metric_list
        
        def reduce_resolution(self, max_resolution:int):
            if len(self.x_vals) > max_resolution:
                pass # can't reduce the resolution to something greater than before
            sample_spacing = int(len(self.x_vals)/max_resolution) + 1
            self.x_vals = self.x_vals[::sample_spacing]
            for lst in self.metrics.values():
                lst = lst[::sample_spacing]

# could use this, not used currently
class DataParams:
    """Contains all attributes needed to fetch data"""
    def __init__(self, ticker, start, end, interval) -> None:
        self.ticker = ticker
        self.start = start
        self.end = end
        self.interval = interval

class ModelParams:
    """To store model parameters (e.g. low_ma, high_ma for moving average model)"""
    def __init__(self) -> None:
        pass