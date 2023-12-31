# Generated by Django 4.1.7 on 2023-03-26 13:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0008_alter_users_bio_alter_users_fizika_alter_users_fizra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='bio',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='fizika',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='fizra',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='him',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='mat',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='obj',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='rus',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
    ]
