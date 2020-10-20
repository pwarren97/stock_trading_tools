from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.
def index(request):
    
    data = {

    }
    return HttpResponse(render(request, 'login/index.html', data))
