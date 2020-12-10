from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as Hasher

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm

hour = 60 * 60
cookie_age = 12 * hour

login_index = 'login/index.html'

# Create your views here.
class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('trade/')
        else:
            form = LoginForm()
            return render(request, login_index, { 'form': form })
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
                    return render(request, login_index, { 'form': LoginForm() })
            return render(request, login_index, { 'form': LoginForm() })
