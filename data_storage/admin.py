from django.contrib import admin
from data_storage.models import Data


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass
