from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegistrationFormEng
from .models import User
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.language = 'ru'
            user.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def register_eng(request):
    if request.method == 'POST':
        form = RegistrationFormEng(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.language = 'en'
            user.save()
            return redirect('/')
    else:
        form = RegistrationFormEng()
    return render(request, 'register_eng.html', {'form': form})

def difficulty(request):
    return render(request, 'difficulty.html')

def sound(request):
    return render(request, 'sound.html')

def text(request):
    return render(request, 'text.html')

def themes(request):
    return render(request, 'themes.html')

def difficulty_level(request, level):
    return render(request, 'difficulty_level.html', {'level': level})

def theme_selection(request, theme):
    return render(request, 'theme_selection.html', {'theme': theme})