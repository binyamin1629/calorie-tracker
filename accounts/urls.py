from django.urls import path
from . import  views


urlpatterns=[
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('profile-details/<int:pk>', views.profileDetails,name='profileDetails'),
    path('edit-profile/<int:pk>', views.editprofile,name='editprofile'),
]

