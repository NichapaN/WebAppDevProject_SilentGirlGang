# Generated by Django 4.1.7 on 2023-05-09 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_user_email_agency'),
        ('tpopstore', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='userprofile.agency'),
        ),
    ]
