from django.shortcuts import render
from .models import StockData
import pandas as pd
import sys
sys.path.append("../Backend_strategies")
from Backend_strategies.calculate_params import get_graph_params
import pdb

def home(request):
    return render(request, 'Strategies_Viewer/home.html')

def chart_view(request):
    stocks = StockData.objects.all().values()
    df = pd.DataFrame(stocks)
    time = df.date.tolist()
    time_isoformat = [date.isoformat() for date in time]
    close = df.close.tolist()
    ticker = df.symbol.tolist()[0]
    output_data = {'time' : time_isoformat, 'y_axis' : close, 'ticker' : ticker}

    return render(request, 'Strategies_Viewer/chart.html', output_data) 

def future_chart_view(request, data_params, model_params):
    # Remaining front-end development pipeline:
    # 1. get data_params and model_params from frontend
    # 2. develop chart options for all parameters in graph_params
    # 3. host website online, allowing link to be shared
    # 4. market research to optimise the interface (survey of friends opinions)
    # 5. implement features extracted from survey results
    data_params = {'ticker':"AAPL", 'start':"2022-01-01", 'end':"2023-01-01", 'interval':"1h"}

    model_params = {'name':"Moving Average", 'low_ma':20, 'high_ma':40}

    graph_params = get_graph_params(ticker=data_params['ticker'], 
                                    interval=data_params['interval'], 
                                    start=data_params['start'], 
                                    end=data_params['end'],
                                    model=model_params['name'], 
                                    params=model_params)

    return render(request, 'Strategies_Veiwer/chart.html', graph_params)