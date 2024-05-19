from django.urls import path
from .views import *

app_name = 'vocabularies'
urlpatterns = [
    path('', get_index_page, name='index'),
    # path('home', get_vocabularies, name='home'),
    path('search', search_view, name='search_view'),
    
]