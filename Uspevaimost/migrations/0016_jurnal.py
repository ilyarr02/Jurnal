# Generated by Django 4.1.7 on 2023-03-29 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Uspevaimost', '0015_rename_dz_timetable_dz1_remove_timetable_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('predmet', models.CharField(blank=True, max_length=20, null=True)),
                ('num', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
