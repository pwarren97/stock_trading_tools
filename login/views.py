from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .forms import LoginForm

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            db_user = User.get(username=username)
        return redirect('trade/')
# def index(request):
#     if request.method == 'GET':
#         return render(request, 'login/index.html')
#     elif request.method == 'POST':
#         return render(request, 'login/index.html')
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
            # Do something if form is valid
