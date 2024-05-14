# Generated by Django 5.0.6 on 2024-05-13 15:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabularies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListVocabulary',
            fields=[
                ('list_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('list_name', models.CharField(default='My dictionary', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vocab', models.ManyToManyField(to='vocabularies.vocabulary')),
            ],
            options={
                'db_table': 'List_Vocabulary',
            },
        ),
    ]
