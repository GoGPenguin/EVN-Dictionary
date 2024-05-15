from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib import messages
def get_view_login(request):
     return render(request, 'login.html')

def get_view_register(request):
     return render(request, 'register.html')

def handle_register(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail', '')  
        password = request.POST.get('inputPassword', '')  
        confirmPassword = request.POST.get('inputConfirmPassword', '') 
        
        # Kiểm tra nếu mật khẩu và xác nhận mật khẩu khớp
        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Kiểm tra nếu email đã tồn tại
        if UserAccount.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        user = UserAccount.objects.create_user(username=email,fullname= email.split('@')[0],password=password)
        if(user):
            messages.success(request, "Registration successful.")
            return redirect('login')  # Chuyển hướng tới trang chủ hoặc trang khác sau khi đăng ký thành công
    
    return render(request, 'register.html')



def handle_login(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail', '').strip()
        password = request.POST.get('inputPassword', '').strip()

        # Xác thực người dùng
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            print("Đăng nhập thành công.")
            messages.success(request, "Đăng nhập thành công.")
            return redirect('/home',{'user': user})  
        else:
            messages.error(request, "Email hoặc mật khẩu không chính xác.")
            return redirect('login')
    
    return render(request, 'login.html')

        



       
    
         





# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('login')  # Chuyển hướng đến trang chủ hoặc trang khác sau khi đăng ký thành công
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})

# def user_login(request):
#     error_message = None
#     if request.method == 'POST':
#         form = UserLoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')  # Replace '/admin' with your desired URL
#             else:
#                 error_message = "Invalid username or password."
#         else:
#             error_message = "Invalid form submission."
#     else:
#         form = UserLoginForm()
#     return render(request, 'login.html', {'form': form, 'error_message': error_message})
