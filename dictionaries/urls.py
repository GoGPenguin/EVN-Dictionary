from django.urls import path
from .views import *

app_name = 'dictionaries'
urlpatterns = [
    path('home', get_view_home, name='home'),
    path('create',get_view_create_dictionary,name='create'),
    path('handle_create',handle_create,name='handle_create'),
    path('detail/<str:dictionary_id>/', dictionary_detail, name='dictionary_detail'),
    path('edit/<str:dictionary_id>/', edit_dictionary, name='edit_dictionary'),
    path('handle_edit_dictionary',handle_edit_dictionary,name='handle_edit_dictionary'),
    path('delete/<str:dictionary_id>/', delete_dictionary, name='delete_dictionary'),
    path('logout/', handle_logout, name='logout'),
    

]