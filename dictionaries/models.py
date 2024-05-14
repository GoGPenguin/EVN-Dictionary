from django.db import models
from vocabularies.models import Vocabulary
from accounts.models import UserAccount

# Create your models here.
class ListVocabulary(models.Model):
    list_id = models.CharField(max_length=10, primary_key=True, null=False)
    user= models.ForeignKey(UserAccount, models.CASCADE)
    vocab = models.ManyToManyField(Vocabulary)
    list_name = models.CharField(max_length=20, default='My dictionary')

    def __str__(self):
        return self.list_name

    class Meta:
        db_table = 'List_Vocabulary'