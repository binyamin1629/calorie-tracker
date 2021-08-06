from django.urls import path
from . import  views


urlpatterns=[
    path('mealTypes/<int:pk>', views.get_all_mealTypes,name='mealType'),
    path('mealTypes/create/<slug:mealTypeResult>/<int:pk>', views.createmeal,name='createmeal'),
    path('mealTypes/remove/<slug:mealTypeResult>/<int:foodInMeal_id>/',views.removeFood,name='removefood'),
    path('date/<int:pk>', views.deatilsByDate,name='deatilsbydate'),
    path('mealTypes/details/type/<str:date>/<int:pk>', views.typeofmaelDetails,name='typeofmaeldetails'),
    path('mealTypes/details/date/type/<str:date>/<slug:mealType>/<int:pk>', views.detailsOfDay,name='detailsofday'),
    

]


