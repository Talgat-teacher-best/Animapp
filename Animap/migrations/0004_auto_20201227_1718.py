# Generated by Django 3.1.1 on 2020-12-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animap', '0003_auto_20201227_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='picture',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
