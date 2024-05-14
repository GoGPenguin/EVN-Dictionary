from django.urls import path
from .views import *

app_name = 'vocabularies'
urlpatterns = [
    path('', get_vocabularies, name='home')
]