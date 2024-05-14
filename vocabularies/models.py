from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    vocab_id = models.CharField(max_length=10, primary_key=True, null=False)
    vocab_en = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.vocab_en

    class Meta:
        db_table = 'Vocabulary'

class PartOfSpeech(models.Model):
    pos_id = models.CharField(max_length=10, primary_key=True, null=False)
    pos_type = models.CharField(max_length=20, null=False)
    vocab = models.ManyToManyField(Vocabulary, through='Translation')

    def __str__(self):
        return self.pos_type

    class Meta:
        db_table = 'Part_Of_Speech'

class Translation(models.Model):
    vocab = models.ForeignKey(Vocabulary, models.CASCADE)
    pos = models.ForeignKey(PartOfSpeech, models.CASCADE)
    vocab_vn = models.CharField(max_length=1000, null=False)
    definition = models.TextField(null=False)
    spelling = models.CharField(max_length=20, null=False)
    example = models.TextField(null=False)

    def __str__(self):
        return (f"Vocab: {self.vocab}, "
                f"Part of Speech: {self.pos}, "
                f"Vocab VN: {self.vocab_vn}, "
                f"Definition: {self.definition}, "
                f"Spelling: {self.spelling}, "
                f"Example: {self.example}")

    class Meta:
        verbose_name = 'translation'
        verbose_name_plural = 'translations'

    class Meta:
        db_table = 'Translation'
        unique_together = ('vocab', 'pos')
