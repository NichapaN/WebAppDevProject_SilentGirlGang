# Generated by Django 4.1.7 on 2023-05-10 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpopstore', '0006_artist_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_by',
            new_name='user',
        ),
    ]