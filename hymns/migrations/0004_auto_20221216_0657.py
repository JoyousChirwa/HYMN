# Generated by Django 2.0.2 on 2022-12-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymns', '0003_auto_20221216_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='dzina',
            name='olemba',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='title',
            name='auther',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='zina',
            name='mlembi',
            field=models.CharField(default='', max_length=255),
        ),
    ]
