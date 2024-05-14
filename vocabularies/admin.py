from django.contrib import admin
from .models import Vocabulary, Translation, PartOfSpeech

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Translation)
admin.site.register(PartOfSpeech)
