from django.http import HttpResponse
from django.shortcuts import render
from .models import Stock, StockName


# Create your views here

# Shows the portfolio of stocks.
def index(request):
    list_of_stocks = StockName.objects.filter()
    context = {
        'list_of_stocks': list_of_stocks
    }
    return render(request, 'trade_stocks/index.html', context)

# Shows information related to a specific stock: price, name, indicators, etc.
def stock_info(request, ticker_symbol):
    stock_name = StockName.objects.get(symbol=ticker_symbol.lower())
    # stock = Stock.objects.get(symbol=ticker_symbol.lower())
    # stock_info_url = '/trade/'
    context = {
        'stock_name': stock_name,
    }

    return render(request, 'trade_stocks/stock_info.html', context)
