from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.stock_data)
admin.site.register(models.Sectorwise)
