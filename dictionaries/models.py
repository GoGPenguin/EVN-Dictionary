from django.db import models
from vocabularies.models import Vocabulary
from accounts.models import UserAccount
import uuid
# Create your models here.
class ListVocabulary(models.Model):
    list_id = models.CharField(max_length=10, primary_key=True, null=False)
    # list_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user= models.ForeignKey(UserAccount, models.CASCADE)
    vocab = models.ManyToManyField(Vocabulary)
    list_name = models.CharField(max_length=20, default='My dictionary')

    def __str__(self):
        return self.list_name

    class Meta:
        db_table = 'List_Vocabulary'



class MyVocab(models.Model):
    myVocab_id = models.AutoField(primary_key=True)
    listVocab = models.ForeignKey(ListVocabulary, models.CASCADE)
    vocab_en = models.CharField(max_length=1000, null=False)
    vocab_vn = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return (f"Vocab: {self.vocab_en}, "
                f"Vocab VN: {self.vocab_vn}")

    class Meta:
        db_table = 'My_Vocabulary'