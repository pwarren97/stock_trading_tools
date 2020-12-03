from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as Hasher

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import LoginForm

hour = 60 * 60
cookie_age = 12 * hour

login_index = 'login/index.html'

# Create your views here.
class Index(View):
    def get(self, request):
        if valid_cookie(request):
            return redirect('trade/')
        else:
            form = LoginForm()
            return render(request, login_index, { 'form': form })
            # return redirect(request, 'trade/')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # returns the User object from the database if the credentials are correct, otherwise None
            cleaned_username = form.cleaned_data['username']
            cleaned_password = form.cleaned_data['password']
            authenticated_user = authenticate(username=cleaned_username, password=cleaned_password)

            # If they entered correct credentials
            if authenticated_user is not None:
                response = redirect('trade/')
                response = add_cookie(response, form)
                return response
            else:
                return render(request, login_index, { 'form': LoginForm() })
        return render(request, login_index, { 'form': LoginForm() })



# Checks if the cookie is valid
def valid_cookie(request):
    # cookie id should be sessionId == 'peyton'
    try:
        cookie_username = request.COOKIES['sessionId']
        user_db_entry = User.objects.get(username=cookie_username)
        return True if user_db_entry else False
    except:
        return False

def add_cookie(response, form):
    # INSECURE METHOD below, needs proper encoding
    # Create the sessionId
    response.set_cookie('sessionId', form.cleaned_data['username'], max_age=cookie_age)
    return response
