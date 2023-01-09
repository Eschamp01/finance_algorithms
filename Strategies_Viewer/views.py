from django.shortcuts import render
from .models import StockData
import pandas as pd
import pdb


def home(request):
    return render(request, 'Strategies_Viewer/home.html')

def chart_view(request):
    # data_type = 'close'
    # time = StockData.objects.all().filter(symbol='AAPL').values_list('date', flat=True)
    # y_axis = StockData.objects.all().filter(symbol='AAPL').values_list(data_type, flat=True)

    # time_vals = []
    # close_vals = []
    # for stock in StockData.objects.all():
    #     time_vals.append(stock.date)
    #     close_vals.append(stock.close)

    # return render(request, 'Strategies_Viewer/chart.html', {
    #     'time': time_vals,
    #     'y_axis': close_vals,
    #     })

    stocks = StockData.objects.all().values()
    df = pd.DataFrame(stocks)
    time = df.date.tolist()
    time_isoformat = [date.isoformat() for date in time]
    close = df.close.tolist()
    ticker = df.symbol.tolist()[0]
    output_data = {'time' : time_isoformat, 'y_axis' : close, 'ticker' : ticker}
    return render(request, 'Strategies_Viewer/chart.html', output_data)



