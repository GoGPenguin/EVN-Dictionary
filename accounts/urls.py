from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('login', views.get_view_login, name='login'),
    path('register', views.get_view_register, name='register'),
    path('handle_register', views.handle_register, name='handle_register'),
    path('handle_login', views.handle_login, name='handle_login')
    
]