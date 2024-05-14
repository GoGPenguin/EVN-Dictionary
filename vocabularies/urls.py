from django.urls import path
from .views import *

urlpatterns = [
    path('', get_vocabularies, name='home')
]