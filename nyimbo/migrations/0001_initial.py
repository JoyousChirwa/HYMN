# Generated by Django 3.0.7 on 2022-12-21 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dzina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nambara_ya_nyimbo', models.IntegerField(default=0)),
                ('dzina_la_nyimbo', models.CharField(max_length=255)),
                ('olemba', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MutuNyimbo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutu_wa_nyimbo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ndime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nambara', models.IntegerField(default=0)),
                ('ndime', models.TextField()),
                ('dzina_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyimbo.Dzina')),
                ('mutu_nyimbo_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nyimbo.MutuNyimbo')),
            ],
        ),
        migrations.AddField(
            model_name='dzina',
            name='mutu_nyimbo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyimbo.MutuNyimbo'),
        ),
    ]