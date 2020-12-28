# Generated by Django 3.1.1 on 2020-12-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animap', '0002_auto_20201214_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='age',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(blank=True, help_text='количество эпизодов имнно в этой части, а не во всех', null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='Animap.Genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='studia',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
