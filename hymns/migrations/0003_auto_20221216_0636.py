# Generated by Django 2.0.2 on 2022-12-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymns', '0002_auto_20221216_0624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='title_text',
            new_name='hymn_title',
        ),
        migrations.AddField(
            model_name='dzina',
            name='nambara_ya_nyimbo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='title',
            name='hymn_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='zina',
            name='nambala_ya_sumu',
            field=models.IntegerField(default=0),
        ),
    ]
