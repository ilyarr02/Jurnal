# Generated by Django 4.1.7 on 2023-03-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='login',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
    ]
