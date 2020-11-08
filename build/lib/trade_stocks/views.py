from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Return account information')

def stock(request):
    return HttpResponse('Return information related to a stock')