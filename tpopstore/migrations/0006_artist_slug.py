# Generated by Django 4.1.7 on 2023-05-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpopstore', '0005_artist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default='slug', max_length=255),
        ),
    ]
