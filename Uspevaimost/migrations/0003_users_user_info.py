# Generated by Django 4.1.7 on 2023-03-24 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Uspevaimost', '0002_remove_users_login_remove_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_info',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
