# Generated by Django 4.1.7 on 2023-03-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uspevaimost', '0012_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='predmet',
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet6',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='predmet7',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='dz',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
