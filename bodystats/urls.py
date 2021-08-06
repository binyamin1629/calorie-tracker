from django.urls import path
from . import  views


urlpatterns=[
    path('body-stats/<int:pk>', views.cratebodystats,name='cratebodystats'),
    path('body-stats/details/<int:pk>', views.bodystatusDetails,name='bodystatusDetails'),
    
]

