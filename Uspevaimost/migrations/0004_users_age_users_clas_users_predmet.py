# Generated by Django 4.1.7 on 2023-03-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0003_users_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='clas',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='predmet',
            field=models.CharField(max_length=20, null=True),
        ),
    ]