# Generated by Django 4.1.7 on 2023-03-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0013_remove_timetable_predmet_timetable_predmet1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]