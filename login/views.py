from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

from .models import User
from .forms import LoginForm


# Create your views here.
class Index(View):
    def get(self, request):
        # Create login form
        form = LoginForm()

        if not request.cookie:
            # Return the login page with the form filled in
            return render(request, 'login/index.html', { 'form': form })
        else:
            return redirect('trade/')

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
                response.set_cookie('user', cleaned_username)
                return response
        return render(request, 'login/index.html')
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
