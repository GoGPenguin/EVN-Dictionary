from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Translation, Vocabulary

# Create your views here.
def get_vocabularies(request):
    data = Translation.objects.all()
    a = Vocabulary.objects.all()
    context = {'data': data, 'a': a}
    return render(request, 'home.html', context)