from django.contrib import admin
from . import models

admin.site.register(models.Users)
admin.site.register(models.timetable)
admin.site.register(models.Jurnal)