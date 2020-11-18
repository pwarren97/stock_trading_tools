from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as Hasher

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import LoginForm

hour = 60 * 60
cookie_age = 24 * hour

# Create your views here.
class Index(View):
    def get(self, request):
        # if request.COOKIES['sessionId'] == 'peyton':
        #     return redirect('trade/index.html')
        # else:
            # Create login form
        form = LoginForm()
        return render(request, 'login/index.html', { 'form': form })
            # return redirect(request, 'trade/')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # returns the User object from the database if the credentials are correct, otherwise None
            authenticated_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            # If they entered correct credentials
            if authenticated_user is not None:
                response = redirect('trade/')
                # INSECURE METHOD below, needs proper encoding
                # Create the sessionId
                response.set_cookie('sessionId', cleaned_username, max_age=cookie_age)
                return response
            else:
                return render(request, 'login/index.html', { 'form': LoginForm() })
        return render(request, 'login/index.html', { 'form': LoginForm() })

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
