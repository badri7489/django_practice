from django.contrib import admin
from app_one import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.Webpage)
admin.site.register(models.AccessRecord)
