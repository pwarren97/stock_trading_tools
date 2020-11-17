from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

# Shows the portfolio of stocks.
def index(request):
    return render(request, 'trade_stocks/index.html')

# Shows information related to a specific stock: price, name, indicators, etc.
def stock_info(request, ticker_symbol):
    # return HttpResponse('Return information related to a stock')
    context = {
        'ticker_symbol': ticker_symbol
    }
    return render(request, 'trade_stocks/stock_info.html', context)
