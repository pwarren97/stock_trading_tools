from django.http import HttpResponse
from django.shortcuts import render
from .models import Stock, StockName
from django.contrib.auth.decorators import login_required

# Create your views here

# Shows the portfolio of stocks.
@login_required
def index(request):
    if request.user.is_authenticated:
        list_of_stocks = StockName.objects.filter()
        context = {
        'list_of_stocks': list_of_stocks
        }
        return render(request, 'trade_stocks/index.html', context)
    else:
        redirect('login/')

# Shows information related to a specific stock: price, name, indicators, etc.
@login_required
def stock_info(request, ticker_symbol):
    stock_name = StockName.objects.get(symbol=ticker_symbol.lower())
    # stock = Stock.objects.get(symbol=ticker_symbol.lower())
    # stock_info_url = '/trade/'
    context = {
        'stock_name': stock_name,
    }

    return render(request, 'trade_stocks/stock_info.html', context)
