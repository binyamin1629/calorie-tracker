from django.contrib import admin
from .models import mealTypes,MyMeal,food,foodInMeal,totalCalosPerMeal,totalCalosPerDay

# Register your models here.
class mealTypeAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}



admin.site.register(mealTypes,mealTypeAdmin)    
admin.site.register(MyMeal) 
admin.site.register(food) 
admin.site.register(foodInMeal) 
admin.site.register(totalCalosPerMeal)
admin.site.register(totalCalosPerDay)