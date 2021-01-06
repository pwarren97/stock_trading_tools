from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

hour = 60 * 60
cookie_age = 12 * hour

login_template = 'login/login.html'
logout_template = 'login/logout.html'

# Create your views here.
class LogIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('trade/')
        else:
            form = LoginForm()
            return render(request, login_template, { 'form': form })
            # return redirect(request, 'trade/')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('trade/')
        else:
            form = LoginForm(request.POST)
            if form.is_valid():
                # returns the User object from the database if the credentials are correct, otherwise None
                cleaned_username = form.cleaned_data['username']
                cleaned_password = form.cleaned_data['password']
                authenticated_user = authenticate(username=cleaned_username, password=cleaned_password)

                # If they entered correct credentials
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    response = redirect('trade/')
                    return response
                else:
                    return render(request, login_template, { 'form': LoginForm() })
            return render(request, login_template, { 'form': LoginForm() })

@login_required
def log_out(request):
    logout(request) # logout function from django.contrib.aut
    return render(request, logout_template)
