from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.
def index(request):
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
            # Do something if form is valid
    return render(request, 'login/index.html')

def results(request, user):
    return HttpResponse('the use is : ' + user)
