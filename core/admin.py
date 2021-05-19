from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=("name","mail","balance")


class HistoryAdmin(admin.ModelAdmin):
    list_display=("transferto","transferby","amount")


admin.site.register(Customer,CustomerAdmin)
admin.site.register(History,HistoryAdmin)

