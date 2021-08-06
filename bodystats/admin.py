from django.contrib import admin
from .models import BodyStatus
# Register your models here.


class BodyStatsAdmin(admin.ModelAdmin):
    readonly_fields=('totoalCaloriesPerDay',)
admin.site.register(BodyStatus,BodyStatsAdmin)