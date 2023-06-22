# Generated by Django 4.1.7 on 2023-03-26 12:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0006_users_pas'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='bio',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='fizika',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='fizra',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='him',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='mat',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='obj',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='users',
            name='rus',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
    ]
