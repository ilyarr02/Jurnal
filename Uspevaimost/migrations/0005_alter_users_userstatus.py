# Generated by Django 4.1.7 on 2023-03-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0004_users_age_users_clas_users_predmet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='userStatus',
            field=models.CharField(max_length=20),
        ),
    ]