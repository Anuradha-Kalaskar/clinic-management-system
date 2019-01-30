from django.shortcuts import render
# from clinicapp.forms import UserForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'clinicapp/index.html')


@login_required
def special(request):
    return HttpResponse(request, 'You Are Logged In!!!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = Truemang

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Your Account Was Inactive !! ")
        else:
            print("Someone Tried To Login And Failed !!")
            print("THEY used Username: {} And Password: {}".format(username, password))
            return HttpResponse("Invalid Login Details Given !!")

    else:
        return render(request, "clinicapp/login.html",{})