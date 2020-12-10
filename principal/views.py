from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout

from . import models
from .forms import CreateUserForm

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pagina2(request):
    return render(request, 'pagina2.html')



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'usuario o contaseña es incorrecta')
            
    
    return render(request, template_name="Login.html", context={})

def logoutuser(request):
    logout(request)
    messages.info(request, 'se ha desconectado')
    return redirect('login')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'la cuenta '+ user + ' fue creada exitosamente')
            return redirect('login')

    context = {'form': form}
    return render(request, 'Register.html', context)
