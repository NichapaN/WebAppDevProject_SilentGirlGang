# Generated by Django 4.1.7 on 2023-04-21 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'ordering': ['agency_name'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.IntegerField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('A', 'Album'), ('M', 'Merchandise')], default='A', max_length=1)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sellers.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sellers.agency')),
            ],
            options={
                'ordering': ['artist_name'],
            },
        ),
    ]
