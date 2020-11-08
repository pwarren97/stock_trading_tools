from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.models import User
from .forms import LoginForm

hour = 60 * 60
cookie_age = 24 * hour

# Create your views here.
class Index(View):
    def get(self, request):
        if valid_cookie(request):
            return redirect('trade/')
        else:
            # Create login form
            form = LoginForm()
            return render(request, 'login/index.html', { 'form': form })
            # return redirect(request, 'trade/')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # Clean the input
            cleaned_username = form.cleaned_data['username']
            cleaned_password = form.cleaned_data['password']

            # pull entry for the specified username
            db_entry = User.objects.get(username=cleaned_username)

            # If the entered the correct password
            if cleaned_password == db_entry.password:
                response = redirect('trade/')
                response.set_cookie('user', cleaned_username, max_age=cookie_age)
                response.set_cookie('pass', cleaned_password, max_age=cookie_age)
                return response
        form = LoginForm()
        return render(request, 'login/index.html', { 'form': form })

def valid_cookie(request):
    return False
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
