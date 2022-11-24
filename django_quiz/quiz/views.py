from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, verifyForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from hashlib import sha256


def home_view(request):
    return render(request, 'home.html')


def signup_view_failed(request):
    return render(request, 'failed.html')


def verify(request):
    form = verifyForm()
    if form.is_valid():
        return redirect("success")
    else:
        form = verifyForm()
    return render(request, 'success.html', {'form': form})


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        response = redirect("verify")
        value = sha256(str(random.randint(1000, 9999)).encode('utf-8'))
        response.set_cookie(key="verification_code", value=value)
        return response
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
