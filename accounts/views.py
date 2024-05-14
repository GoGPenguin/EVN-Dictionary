from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm

def user_login(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Replace '/admin' with your desired URL
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid form submission."
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})
