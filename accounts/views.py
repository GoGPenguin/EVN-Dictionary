from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('https://www.facebook.com/')  # Replace 'home' with your desired URL name
            else:
                # Invalid login
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})